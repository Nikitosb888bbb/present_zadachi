side_a=float(input('Введите длину стороны А: '))
side_b=float(input('Введите длину стороны B: '))
side_c=float(input('Введите длину стороны C: '))

if side_a + side_c > side_b and side_a + side_b > c and side_b + side_c > side_a:
    if side_a == side_b == side_c:
        print('Треугольник равносторонний')
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Треугольника не существует')

