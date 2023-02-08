bentuk = int(input("Masukan angka : "))
print()

for i in range(bentuk):
    for j in range(bentuk-i):
     print('  ',end='')

for k in range(i+1):
    print('*  ',end='')
print()

for i in range(1,bentuk):
    for j in range(i+1):
     print('  ',end='')

for k in range(bentuk-i):
    print('*  ',end='')
print()
