while True:
    a = int(input("a = "))
    b = int(input("b = "))
    if(a < 1 or b < 1):
        print("the program is terminated ")
        break
    if(a < b ):
        temp = a
        a = b
        b = temp
    while (b != 0 ):
        r = a % b
        a = b
        b = r
    print( " bmm (a,b = ", a )