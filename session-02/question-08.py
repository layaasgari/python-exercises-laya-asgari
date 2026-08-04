a=float(input('لطفا ساعت مد نظر خود را وارد نمایید: '))
if 4<=a<=10:
    print('صبح')
elif 10<a<16:
    print('ظهر')
elif 16<=a<20:
    print('عصر')
elif 20<=a<=23 or 0<=a<4:
    print('شب')
else:
    print('لطفا در بازه زمانی 0 تا 23 وارد نمایید')