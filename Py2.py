#1
x = 1
y = 2
print(x + y)

#2
x = 3
y = 100
z = x * y
if z >= 1000:
    print(z)
elif z < 1000:
    print(x + y)

#3
rows=10 
columns=10
for i in range(1,rows+1):
    for j in range(1,columns+1):
        c=i*j
        print("{:2d} ".format(c),end='')
    print("\n") 

#4
rows = 5
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")
    print("\n")