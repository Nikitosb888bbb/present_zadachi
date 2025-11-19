month=int(input('Введите порядковый номер месяца: '))
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
    print('В месяце 31 день')
elif month==4 or month==6 or month==9 or month==11:
    print('В месяце 30 дней')
else:
    print('В месяце 28 дней')