side_a=float(input('Введите длину стороны А: '))
side_b=float(input('Введите длину стороны B: '))
side_c=float(input('Введите длину стороны C: '))

if a + c > b and a + b > c and b + c > a:
    if side_a == side_b == side_c:
        print('Треугольник равносторонний')
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольника не существует')
