a=float(input('مبلغ را وارد نمایید: '))
if a>=1000000:
    discount=a*0.15
    print(discount)
elif 500000<=a<1000000:
    discount=a*0.10
    print(discount)
else: a<500000
print('شامل تخفیف نمیباشد',a)
    

    
