a =100
b=200
c=300
def processor(arg):
    print('processing file')
    global a
    global b
    global c
    c += arg+b+a
    print(c)
processor(10)
