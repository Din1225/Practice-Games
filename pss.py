# 剪刀、石頭、布
from random import randint

#初始資料設定
window = 1 
#List會自動全域
user_name = ["Din","Cyan","Steven"]
user_password = ["din123","cyan123" ,"steven123" ]
player = [0,0]
computer = [0,0]

#遊戲主體
def game_run() :

    global window
    count = { "win":0 , "lose":0 , "tie":0 }   
    print("---歡迎來到剪刀石頭布!---")
    for i in range (1,4) :
        #玩家出拳(防呆機制)
        while True :
            try :
                player[0] = int(input("請出拳 : (1) 剪刀 (2) 石頭 (3) 布 "))
                if player[0] == 1 or player[0] == 2 or player[0] == 3 :
                    break
                else :
                    print("請確定您輸入的是數字1~3")
            except :
                 print("請確定您輸入的是數字")

        #電腦出拳(使用隨機)
        computer[0] = randint(1,3)

        #1~3 轉 剪刀石頭布
        if player[0] == 1 :
            player[1] = "剪刀"
        elif player[0] == 2 :
            player[1] = "石頭"
        elif player[0] == 3 :
            player[1] = "布"
        if computer[0] == 1 :
            computer[1] = "剪刀"
        elif computer[0] == 2 :
            computer[1] = "石頭"
        elif computer[0] == 3 :
            computer[1] = "布"
        print( name + "出了 : " + player[1] + ", 電腦出了 : " + computer[1] )

        #遊戲結果的判定
        if player[0] == computer[0]:
            count["tie"] += 1
            print("平手\n")
        elif (player[0],computer[0]) in [(3,2),(1,3),(2,1)] :
            count["win"] += 1
            print("你贏了\n")
        else :
            count["lose"] += 1
            print("你輸了\n")
        print("========================")

        #結算全部的遊戲結果
        if i == 3 :
            print("你贏"+ str(count["win"]) +"把")
            print("電腦贏"+ str(count["lose"]) +"把")
            print("平手"+ str(count["tie"]) +"把\n")

    #自創評語
    if int(count["win"]) == 0 :
        print("你今天的運氣跟狗屎一樣")
    elif int(count["win"]) == 1 :
        print("你今天的運氣有好一點...就一點")
    elif int(count["win"]) == 2 :
        print("你今天的運氣好像不錯")
    elif int(count["win"]) ==3 :
        print("你今天的運氣爆棚")
    #遊戲結束後可選擇再繼續玩或關閉遊戲
    while True :
        esc = input("\na:登出並回到主選單 / b:關閉遊戲 :")
        if esc == "a" :
            window = 1
            menu()
            break
        elif esc == "b" :
            print("下次再玩吧!")
            break
        else :
            print("請輸入a或b")

#註冊            
def register() :

    global window   
    while True :
        new_name = input("請輸入你的新使用者名稱(限英文): ")
        new_password = input("請輸入你的新密碼: ")
        if new_name in user_name :
            print("此名稱已被使用")
        else :
            user_name.append(new_name)
            user_password.append(new_password)
            print("註冊成功")
            print("-----回到主選單-----")
            window = 1
            break

#主選單            
def menu() :

    global window
    global name
    global password   
    while window == 1 :
        action = input("請選擇你要 登入(login),註冊(register),離開(exit) :\n")
        if action == "login" :
            name = input("請輸入你的使用者名稱 : ")
            password = input("請輸入你的密碼 : ")
            check()
            break
        elif action == "register" :
            register()
            window = 1
        elif action == "exit" :
            print("下次再玩吧!")
            break
        else :
            print("不要鬧喔! 請輸入login, register, exit")

#帳密判斷          
def check() :

    global name
    global password
    global window
    temp = "-1"    
    if not(name in user_name) :
        temp = "not register"
    elif password != user_password[user_name.index(name)] :
        temp = "wrong"
    elif (name in user_name) and (password == user_password[user_name.index(name)]) :
        temp ="ok"          
    if temp == "ok":
        game_run()
    elif temp == "wrong" :
        print("使用者名稱或密碼有誤")
        act = input("重新輸入(relogin)或是離開(exit): ")
        if act == "relogin" :
            name = input("請輸入你的使用者名稱 : ")
            password = input("請輸入你的密碼 : ")
            check()
        elif act == "exit" :
            print("下次再玩吧!")
        else:
            print("請輸入relogin或exit !")
    elif temp == "not register" :
        act = input("此用戶名尚未註冊，重新輸入(relogin),註冊(register)或是離開(exit): ")
        if act == "relogin" :
            name = input("請輸入你的使用者名稱 : ")
            password = input("請輸入你的密碼 : ")
            check()
        elif act == "register" :
            register()
            menu(window)
        elif act == "exit" :
            print("下次再玩吧!")
        else :
            print("請輸入relogin,register或exit !")

            
#啟動遊戲
menu()