from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import autho  # 驗證碼
from tkinter import ttk
import tkinter as tk
import onnxruntime


# ------------------------------------function-----------------------------------------
class window(tk.Frame):
    def __init__(self, win):
        super().__init__(win)
        self.win = win
        self.win.title("NPTU期中期末意見調查")
        self.win.geometry("580x450")
        self.win.config(bg="#e2e2e2")

        self.ac = tk.Label(self.win, text="帳號")
        self.ac.place(x=40, y=30)
        self.ACentry = tk.Entry(self.win, width=50)
        self.ACentry.place(x=80, y=30)

        self.pw = tk.Label(self.win, text="密碼")
        self.pw.place(x=40, y=75)
        self.PWentry = tk.Entry(self.win, show="*", width=50)
        self.PWentry.place(x=80, y=75)
        self.study = "必修"
        self.attitude = "非常認真"
        self.absent = "從未缺席"
        self.preScore = "90 分以上"
        self.copyRight = "是"

        self.btn1 = tk.Button(
            self.win,
            height=1,
            width=10,
            text="開始執行",
            command=lambda: self.start(
                self.ACentry.get(),
                self.PWentry.get(),
                self.midfin.get(),
                self.evaluation.get(),
                self.Grade.get(),
                self.sex.get(),
                self.study,
                self.attitude,
                self.absent,
                self.preScore,
                self.copyRight,
            ),
        )
        self.btn1.place(x=380, y=385)
        self.MIDofFIN()
        self.evaluations()
        self.FianlGrade()
        self.SEX()
        # self.Study()

    def MIDofFIN(
        self,
    ):
        self.midfin = tk.IntVar()
        self.radio1 = tk.Radiobutton(win, text="期中 意見調查", variable=self.midfin, value=1)
        self.radio1.place(x=40, y=145)
        self.radio2 = tk.Radiobutton(win, text="期末 意見調查", variable=self.midfin, value=2)
        self.radio2.place(x=40, y=205)

    def evaluations(self):
        self.evaluation = tk.IntVar()
        self.radio_button_3 = tk.Radiobutton(
            self.win, text="非常滿意", variable=self.evaluation, value=5
        )
        self.radio_button_3.place(x=170, y=145)

        self.radio_button_4 = tk.Radiobutton(
            self.win, text="滿意", variable=self.evaluation, value=4
        )
        self.radio_button_4.place(x=170, y=205)

        self.radio_button_5 = tk.Radiobutton(
            self.win, text="普通", variable=self.evaluation, value=3
        )
        self.radio_button_5.place(x=170, y=265)

        self.radio_button_6 = tk.Radiobutton(
            self.win, text="不滿意", variable=self.evaluation, value=2
        )
        self.radio_button_6.place(x=170, y=325)

        self.radio_button_7 = tk.Radiobutton(
            self.win, text="非常不滿意", variable=self.evaluation, value=1
        )
        self.radio_button_7.place(x=170, y=385)

    def FianlGrade(self):
        self.Grade = tk.IntVar()
        self.grade1 = tk.Radiobutton(self.win, text="大一", variable=self.Grade, value=1)
        self.grade1.place(x=280, y=145)
        self.grade2 = tk.Radiobutton(self.win, text="大二", variable=self.Grade, value=2)
        self.grade2.place(x=280, y=205)
        self.grade3 = tk.Radiobutton(self.win, text="大三", variable=self.Grade, value=3)
        self.grade3.place(x=280, y=265)
        self.grade4 = tk.Radiobutton(self.win, text="大四", variable=self.Grade, value=4)
        self.grade4.place(x=280, y=325)
        self.grade5 = tk.Radiobutton(self.win, text="研究所", variable=self.Grade, value=5)
        self.grade5.place(x=280, y=385)

    def SEX(self):
        self.sex = tk.IntVar()
        self.sex1 = tk.Radiobutton(self.win, text="男", variable=self.sex, value=1)
        self.sex1.place(x=370, y=145)
        self.sex2 = tk.Radiobutton(self.win, text="女", variable=self.sex, value=2)
        self.sex2.place(x=370, y=205)


    # ===================================================================================================================================================================

    def close_window():
        window.destroy()

    def start(
        self,
        account,
        ACpassword,
        midfin,
        evalution,
        grade,
        sex,
        study,
        attitude,
        absent,
        preScore,
        copyRight,
    ):
        # 設定google driver的路徑檔案2
        # print(account, ACpassword, midfin, evalution)
        # print(type(account), type(ACpassword), type(midfin), type(evalution))
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option(
            "prefs",
            {
                "profile.password_manager_enabled": False,
                "credentials_enable_service": False,
            },
        )
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        # options.use_chromium = True
        driver = webdriver.Chrome(
            options=options, service=Service("./chromedriver.exe")
        )
        driver.maximize_window()

        driver.get("https://webap.nptu.edu.tw/Web/Secure/default.aspx")
        # ----------------login-----------------
        fullpage = 0
        logout = 0
        sleep(0.2)
        student = WebDriverWait(driver, 10)
        student = student.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/form/table/tbody/tr[1]/td/table[2]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td[2]/table/tbody/tr/td[1]/input",
                )
            )
        ).click()

        sleep(0.1)
        ac = WebDriverWait(driver, 10)
        ac = ac.until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input",
                )
            )
        )
        sleep(0.1)
        ac = driver.find_element(
            By.XPATH,
            "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[2]/input",
        )
        ac.send_keys(account)  # your account
        sleep(0.1)
        flag = True
        while flag:
            password = driver.find_element(
                By.XPATH,
                "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/input",
            )
            password.send_keys(ACpassword)  # your password
            sleep(0.1)
            atho = driver.find_element(
                By.XPATH,
                "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/img",
            )
            atho.screenshot("code.png")
            sleep(1)
            ocr = autho.DdddOcr()
            with open("code.png", "rb") as f:
                img_bytes = f.read()

            res = ocr.classification(img_bytes)
            # print(res)
            sleep(0.2)
            keyAtho = driver.find_element(
                By.XPATH,
                "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[3]/td[2]/input",
            )
            keyAtho.send_keys(res)
            sleep(0.1)
            Login = driver.find_element(
                By.XPATH,
                "/html/body/form/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/table[1]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[1]/td[3]/input",
            )
            Login.click()
            sleep(0.3)

            try:
                alert = Alert(driver)
                print(alert.text)
                if alert.text == "帳號或密碼錯誤，無法登入!!":
                    self.close_window()
                    flag = False
                    break
                elif alert.text == "驗證碼不符!!":
                    alert.accept()
                    sleep(0.3)
                else:
                    flag = False

                    break
            except:
                flag = False
        sleep(1)
        try:
            alert=Alert(driver)
            alert.accept()
        except:
            pass
        alert = WebDriverWait(driver, 1).until(EC.alert_is_present())
        # print("break")
        frames = driver.find_elements(By.TAG_NAME, "frame")

        frame1 = frames[0]  # 這是對付html內的#document左半
        frame2 = frames[1]  # 這是對付html內的#document右半
        try:  # 萬一出錯直接用登出 不要要我等5分鐘
            # 登入後
            driver.switch_to.frame(frame2)
            logout = driver.find_element(By.ID, "CommonHeader_ibtLogOut")
            print("1")
            body = driver.find_element(By.TAG_NAME, "body")
            body.send_keys(Keys.PAGE_DOWN)
            sleep(0.3)
            print("2")
            survey = driver.find_element(
                By.ID, "MenuDefault_dgData_ibtMENU_ID_8"
            ).click()  # 03/22
            print("3")
            sleep(0.3)
            # 開始找意見調查
            if midfin == 1:
                driver.find_element(By.LINK_TEXT, "[A1007S]_期中學習意見調查").click()  # mid
                button_elements = driver.find_elements(
                    By.XPATH, '//td[@class="TDItemStyle"]/input[@type="submit"]'
                )
                buttonNum = len(button_elements)
                for _ in range(0, buttonNum):
                    button_elements = driver.find_elements(
                        By.XPATH, '//td[@class="TDItemStyle"]/input[@type="submit"]'
                    )
                    for button_element in button_elements:
                        # 检查按钮的disabled属性是否为true
                        is_disabled = button_element.get_attribute("disabled")
                        if is_disabled != "true":
                            button_element.click()  # 點進去填表單葉面
                            sleep(0.2)
                            alert = Alert(driver)
                            alert.accept()
                            sleep(0.3)
                            # 尋找 非常同意
                            radios = driver.find_elements(
                                By.XPATH,
                                f'//span[@style="font-size:10pt;"]/input[@type="radio" and @value="{evalution}"]',
                            )  # 找到非常同意
                            for radio in radios:
                                radio.click()

                            # 尋找 存檔
                            save = driver.find_element(By.XPATH, '//input[@title="存檔"]')
                            save.click()
                            alert = Alert(driver)
                            alert.accept()
                            sleep(0.3)

                            # cancel = driver.find_element(By.XPATH,'//input[@title="取消"]')
                            # cancel.click()
                            break
                        else:
                            pass
            elif midfin == 2:
                gradeList=['大一','大二','大三','大四','研究所']
                sexList=['男','女']
                evalutionList=['非常不同意','不同意',"普通",'同意','非常同意']
                driver.find_element(By.LINK_TEXT, "[A1014S]_期末學習意見調查").click()  # fin
                # start
                button_elements = driver.find_elements(
                    By.XPATH, '//td[@class="TDItemStyle"]/input[@type="submit"]'
                )
                buttonNum = len(button_elements)
                for _ in range(0, buttonNum):
                    button_elements = driver.find_elements(
                        By.XPATH, '//td[@class="TDItemStyle"]/input[@type="submit"]'
                    )
                    for button_element in button_elements:
                        # 检查按钮的disabled属性是否为true
                        is_disabled = button_element.get_attribute("disabled")
                        if is_disabled != "true":
                            button_element.click()  # 點進去填表單葉面
                            sleep(0.2)
                            alert = Alert(driver)
                            alert.accept()
                            sleep(1)
                            # 基本資料
                            print("開始基本資料")
                            driver.find_element(By.XPATH,f'//label[text()="{gradeList[grade-1]}"]').click() 
                            driver.find_element(By.XPATH,f'//label[text()="{sexList[sex-1]}"]').click() 
                            driver.find_element(By.XPATH,f'//label[text()="{study}"]').click() 
                            driver.find_element(By.XPATH,f'//label[text()="{attitude}"]').click() 
                            driver.find_element(By.XPATH,f'//label[text()="{absent}"]').click() 
                            driver.find_element(By.XPATH,f'//label[text()="{preScore}"]').click() 
                            driver.find_element(By.XPATH,f'//label[text()="{copyRight}"]').click() 


                            # 尋找 非常同意
                            radios = driver.find_elements(
                                By.XPATH,f'//label[text()="{evalutionList[evalution-1]}"]')  # 找到非常同意
                            for radio in radios:
                                radio.click()

                            # 尋找 存檔
                            save = driver.find_element(By.XPATH, '//input[@title="存檔"]')
                            save.click()
                            alert = Alert(driver)
                            alert.accept()
                            sleep(0.3)

                            # cancel = driver.find_element(By.XPATH,'//input[@title="取消"]')
                            # cancel.click()
                            break
                        else:
                            pass

            sleep(1)

        finally:
            i = 0
            while i < 3:
                try:
                    logout = WebDriverWait(driver, 5)
                    logout = logout.until(
                        EC.visibility_of_element_located(
                            (By.ID, "CommonHeader_ibtLogOut")
                        )
                    ).click()
                    sleep(1)
                    alert = Alert(driver)
                    alert.accept()
                    print("done")
                except:
                    print("not found logout button")
                finally:
                    i += 1


# =================================================================================================================================================

win = tk.Tk()
window(win)

style = ttk.Style()
style.theme_use("default")
win.mainloop()
