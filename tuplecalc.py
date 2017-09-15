#there are two types of tuples as used in this calculator: containers and numbers
#a container has at least two number types and nothing else
#containers cannot store other containers
#numbers are either empty (for 0) or contain a single number (it's predecessor)
#there are no exceptions, even within functions
#passing a single number to *args will yield it's successor, not a container with only that number
#however, algorithms that treat this as a container with one element are acceptable, see add() for example
#passing a container to *args is not allowed as whis would create a container with a sinle container element
#adding container tuples to merge is considered cheating


#takes a single container or 1 or more numbers
def add(tup1, *args):
    if not args:
        if getlen(tup1):
            sum = ()
            for i in tup1:
                sum = add(sum, i)
            return sum
        else:
            return tup1
    for temp in args:
        while temp:
            tup1 = (tup1,)
            for i in temp:
                temp = i
    return tup1

#takes 2 numbers
def sub(tup1, tup2):
    while tup2:
        for i in tup1:
            tup1 = i
        for i in tup2:
            tup2 = i
        if not tup1 and tup2:
            break
    else:
        return tup1
    #forces an exception when subtracting by a larger number
    tup1[()]

def mul(tup1, *args):
    prod = ()
    for j in args:
        while j:
            temp = tup1
            while temp:
                prod = (prod,)
                for i in temp:
                    temp = i
            for i in j:
                j = i
    return prod

def div(tup1, tup2):
    quo = ()
    while True:
        rem = ()
        temp = tup2
        while temp:
            if not tup1:
                break
            rem = (rem,)
            for i in temp:
                temp = i
            for i in tup1:
                tup1 = i
        else:
            quo = (quo,)
            continue
        break
    return (quo, rem)

#returns tup1**tup2
def exp(tup1, tup2):
    #forces an exception for 0**0
    if not tup1 and not tup2:
        tup1[()]
    res = ((),)
    while tup2:
        res = mul(res, tup1)
        for i in tup2:
            tup2 = i
    return res

def fact(tup):
    if not tup:
        return ((),)
    else:
        for i in tup:
            dec = i
        return mul(tup, fact(dec))

def perm(tup1, tup2):
    sol = div(fact(tup1),fact(sub(tup1,tup2)))
    for i in sol:
        sol = i
        break
    return sol

def comb(tup1, tup2):
    sol = div(perm(tup1,tup2),fact(tup2))
    for i in sol:
        sol = i
        break
    return sol

#returns () for numbers or the number of elements for containers
#can also be used as iscontainer() for flow control
def getlen(tup):
    length = ()
    #gets the length
    for i in tup:
        length = (length,)
    #decrements
    for i in length:
        length = i
    #if the decremented value is () (meaning tup was a number) return ()
    if not length:
        return length
    #otherwise return the reincremented value
    return (length,)

#indexes a container
def getind(tup, ind):
    for i in tup:
        if not ind:
            return i
        for j in ind:
            ind = j

#these are just for testing, they don't count
#generates a nested tuple val deep
def gen(val):
    if isinstance(val, int):
        tup = ()
        for i in range(val):
            tup = (tup,)
        return tup
    elif isinstance(val, tuple):
        tup = ()
        for i in val:
            tup += (gen(i),)
        return tup

#turns a nested tuple into an integer
def rev(tup):
    if len(tup) <=1:
        val = 0
        while tup:
            val += 1
            tup = tup[0]
        return val
    else:
        val = ()
        for i in tup:
            val += (rev(i),)
        return val