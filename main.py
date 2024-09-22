x = 5
if (type(x)is int):
    print("true")
else:
    print("false")
x= 5.0
if (type(x)is not float):
    print("true")
else:
    print("false")
x = 20
y = 20
if ( x is y ):
    print("x & y same identity")
y=30
if( x is not y):
     print("x & y have different identity")
a = 10
b = -10
print("a >>  1 =", a >> 1)
print("b >>  1 =", b >> 1)
a = 5
b = -10
print("a <<  1 =", a << 1)
print("a <<  1 =", a << 1)
print("enter maks obtainef in 5 subject: ")
markone = int(input())
marktwo = int(input())
markthree = int(input())
tot = markone+marktwo+markthree
avg = tot/3
if avg>=91 and avg<=100:
    print("your grade is a1")
elif avg>=81 and avg<=91:
    print("your grade is a2")
elif avg>=71 and avg<=81:
    print("your grade is b1")
elif avg>=61 and avg<=71:
    print("your grade is b2")
elif avg>=51 and avg<=61:
    print("your grade is c1")
elif avg>=41 and avg<=51:
    print("your grade is c2")
elif avg>=31 and avg<=41:
    print("your grade is d")
elif avg>=21 and avg<=31:
    print("your grade is e1")
elif avg>=11 and avg<=21:
    print("your grade is e2")
else:
    print("invalid input")