# 請撰寫一段程式，能在輸入整數 a, b, c 後
# 判斷 ax^2+bx+c=0 有多少實數解，並把這些解算出來
# 注意：你需要自行思考有哪些邊緣條件要檢查，並在你的程式設置適當的處理

# 輸入數字
print("ax^2+bx+c=0 有多少實數解？解為？" )
a = int(input('請輸入整數 a：'))
b = int(input('請輸入整數 b：'))
c = int(input('請輸入整數 c：'))


print('\n'
      '✧---✧ 計算魔法 (ﾉ◕ヮ◕)／*:･ﾟ✧---✧\n')

# 判斷實數解
# a,'x^2+',b,'x+',c,'=0 
Δ = b **2 - 4*a*c
if Δ > 0 :
    print('此方程式有 2 個不相等的實數解')
elif Δ == 0:
    print('此方程式有 1 個實數解')
else :
    print('此方程式無實數解')
    
# 求解
import math

if Δ > 0 :
    x = (- b - math.sqrt(Δ) )/ (2 * a)
    x2 = (- b + math.sqrt(Δ)) /(2 * a)
    print('解為',x,',',x2)
elif Δ == 0:
    x = - b / (2 * a)
    print('解為',x,)
else :
    print()

# 輸出回應
print('\n'"a 不可為 0" if a == 0  else "")

#測試