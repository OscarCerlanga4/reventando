#! C:\Users\alumno24\AppData\Local\Microsoft\WindowsApps\python.exe




lista = list(range(1000000000))
print(lista)
print(len(lista))

for pos in range(len(lista)):
    print(pos)
    if pos == 0:
        pass
    else:
        lista[pos] += lista[pos-1]
        
print(lista)