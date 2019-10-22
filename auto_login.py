# coding: UTF-8
import time
from selenium import webdriver

#ログイン情報
gakuseki = "学籍番号"
pas = "パスワード"

#マトリクスコード
A = ["a", "b", "c", "d", "e", "f", "g"]
B = ["a", "b", "c", "d", "e", "f", "g"]
C = ["a", "b", "c", "d", "e", "f", "g"]
D = ["a", "b", "c", "d", "e", "f", "g"]
E = ["a", "b", "c", "d", "e", "f", "g"]
F = ["a", "b", "c", "d", "e", "f", "g"]
G = ["a", "b", "c", "d", "e", "f", "g"]
H = ["a", "b", "c", "d", "e", "f", "g"]
I = ["a", "b", "c", "d", "e", "f", "g"]
J = ["a", "b", "c", "d", "e", "f", "g"]
mat = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H, "I": I, "J": J}

#ログインページを取得

driver = webdriver.Chrome('chromedriverのpath')
driver.get("https://portal.nap.gsic.titech.ac.jp/GetAccess/Login?Template=userpass_key&AUTHMETHOD=UserPassword")

time.sleep(1)

#ログイン情報を入れる
elem = driver.find_element_by_name("usr_name")  #
elem.clear
elem.send_keys(gakuseki)

elem = driver.find_element_by_name("usr_password")
elem.clear
elem.send_keys(pas)

driver.find_element_by_name("OK").click()  #

time.sleep(1)

# テキストとして情報を取得
elem1 = driver.find_element_by_id("authentication").text
# アルファベットを取得
alpha1, alpha2, alpha3 = elem1[29], elem1[35], elem1[41]


#数字を取得
num1, num2, num3 = int(elem1[31]), int(elem1[37]), int(elem1[43])


#パスワードをマトリクスコードから入力 
for alpha in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
    if alpha == alpha1:
        code = mat[alpha][num1 - 1]
        elem = driver.find_element_by_name("message3")
        elem.clear
        elem.send_keys(code)


for alpha in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
    if alpha == alpha2:
        code = mat[alpha][num2 - 1]
        elem = driver.find_element_by_name("message4")
        elem.clear
        elem.send_keys(code)


for alpha in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]:
    if alpha == alpha3:
        code = mat[alpha][num3 - 1]
        elem = driver.find_element_by_name("message5")
        elem.clear
        elem.send_keys(code)

#okボタンをクリック
driver.find_element_by_name("OK").click()

