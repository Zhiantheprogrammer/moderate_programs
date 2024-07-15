a=str(input("input a string"))
b="cap"#you can replace this with whatever you want
s=[]
q=0
d=""
p=0
for x in(a):
    s.append(x)
    p=p+1
    if p>=3:
        e=s[0]+s[1]+s[2]
        if e==b:
            q=q+1
        s.pop(0)
if q>=1:
    print("the word ",b,"is present in the string you gave is reapeting",q,"time/s")
    quit()
else:
    print("the word ",b,"is not present in the string you gave")
