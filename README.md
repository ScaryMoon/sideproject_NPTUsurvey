!!!不可以登入時有出現超過很久未更改密碼的警告出現!!!(就是叫你換密碼)
先看自己googleChorme的版本(右邊三個點->設定->關於Chrome)找到版本111.0.5XXXX(只要看前面5位數字就行)
找到相對應的版本https://chromedriver.chromium.org/downloads
下載後解壓縮(取代掉此資料夾的chromedriver.exe
放到此檔案資料夾裡即可執行程式
打包pyinstaller -F -w  .\X.py .\Y.py --add-data ".\c2.onnx" --add-data ".\c1.onnx"  --icon=i.ico  