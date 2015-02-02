def vytvor_list_and_tuple():
    """nacita sekvenciu cisel oddelenzch ciarkami a vytvori list
        a tuple"""
    values = input()
    l = values.split(",")
    del values
    t = tuple(l)
    print (l)
    print(t)

def square_root():
    """vypocita hodnotu pre zadanu sekvenciu cisel"""
    import math
    c = 50
    h = 30
    values = []
    d = input().split(",")
    for x in d:
        q = int(math.sqrt((2*c*int(x))/h))
        values.append(q)
    print(values)
