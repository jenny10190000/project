#輸入兩整數m,n(m>n)，請依序印出m和n的最大公因數與最小公倍數
print('假定m>n')
m=eval(input('m='))
n=eval(input('n='))

if m>n:
    a=m
    b=n
else:
    b=n
    a=m
#最大公因數
for i in range(b+1,0,-1):
    if a%i==0 and b%i==0 and i!=1:
        print('最大公因數:',i)
        break
    elif a%i==0 and b%i==0 and i==1:
        print('最大公因數:互質')
        break
#最小公倍數
for q in range(2,a*b+1,1):
    if q%a==0 and q%b==0:
        print('最小公倍數:',q)
        break
print("add 1 line")

