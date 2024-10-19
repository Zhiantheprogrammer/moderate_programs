a = str(input("give a name"))
u = str(input("give a str to search in the name you gave"))
a = a.lower()
l = 0
e = u
b = 0
c = []
o = 0
s = 0
w  = 0
t = ""
for ti in (u):
    w += 1
    
for q in (u):
    s+=1


    
for x in (a):
    c.append(x)

    b = b + 1
    
    if b==s:
        t = ""
        b = b-1 
        for op in range(w):
            t = t+c[op]
            
        if e == t:
            l += 1
        c.pop(0)
        
            
if l>=1:
    print("the str  ",u," is there in the name you gave and it is repeating",l,"times")
else:
    print("the str ",u," is not found in the given name")

            






























