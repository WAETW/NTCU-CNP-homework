import random

start = input('輸入Y開始拉霸遊戲:')

if start == 'Y':
    print('遊戲開始')
else:
    exit()

money = input('輸入金額:')
money = int(money)

num1 = random.randrange(1,6)
num2 = random.randrange(1,6)
num3 = random.randrange(1,6)

print(num1,num2,num3)

if num1==num2 and num1==num3 and num2==num1 and num2==num3 and num3==num2 and num3==num1:
    money=money*1.5
    print('你贏了!獲得:%d%money')
else:
    print('噴了%d'%money)
