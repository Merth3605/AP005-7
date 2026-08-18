precio = int(input ('Ingerese un numero'))
if precio <= 1000:
    print ('Barato')
elif precio > 1000 and precio <= 2000:
    print ('Precio medaianamente barato')
elif precio > 2000 and precio <= 3000:
    print ('Precio medaianamente caro')
else:
    print('Caro')
