
# Online Python - IDE, Editor, Compiler, Interpreter
s=input()
g=''

s=s.replace(str(chr(39)),str(chr(34)))


for i in range(len(s)):
    if s[i] == str(chr(34)):
        g+=str(chr(34))
    else:
        if s.count(s[i])>=2:
            g+=str(chr(41))
        else:
            g+=str(chr(40))
print(g)