import random

con = 'Y'

start = input('輸入Y開始拉霸遊戲:')
if start == 'Y':
    print('遊戲開始')
else:
    exit()
totalmoney = int(input('輸入金額:'))
tempmoney = totalmoney
while con == 'Y':
    num1 = random.randrange(1,6)
    num2 = random.randrange(1,6)
    num3 = random.randrange(1,6)
    money = 100

    print(num1,num2,num3)
    totalmoney = totalmoney - money
    if (num1==num2 and num1==num3):
        money=money*2
        print('你贏了!獲得:%d'%money)
        totalmoney = totalmoney + money
        print('總獎金:%d'%totalmoney)
    elif (num1==num2 and num1!=num3) or (num1==num3 and num2!=num3) or (num3==num2 and num3!=num1):
        money=money*1.5
        print('你贏了!獲得:%d'%money)
        totalmoney = totalmoney + money
        print('總獎金:%d'%totalmoney)
    else:
        print('噴了%d'%money)
        print('總獎金:%d'%totalmoney)
    if totalmoney/100>=1:
        con = input('是否繼續(Y/N):')
        if con == 'Y':
            con = 'Y'
            continue
        elif con =='N':
            if totalmoney>tempmoney:
                print('你贏了!獲得:%d'%totalmoney)
            elif totalmoney == tempmoney:
                print('平手取回:%d'%totalmoney)
            else:
                tempmoney = tempmoney - totalmoney
                print('GG!你輸了:%d'%tempmoney)
            exit()
    elif totalmoney/100 == 0:
        print('GG!你破產了剩餘金額:%d'%totalmoney)
        exit()
