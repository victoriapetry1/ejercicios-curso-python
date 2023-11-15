n=int(input())
diamantes=[str()for i in range(n)]

for i in range(n):
    var =str(input())
    vec =[]
    for j in range(len(var)):
        vec.append(var[j])
    diamantes[i] = vec

print(diamantes)


for i in range(len(diamantes)):
    c1=0
    for a in range(len(diamantes[i])):
            if diamantes[i][a]=="<":
                for j in range((len(diamantes[i]))-1,a,-1):
                    if diamantes[i][j]==">":
                        diamantes[i][j]="."
                        c1= c1 + 1
    print(c1)


#caso prueba

""" 2
<..><.<..>>
<<<..<......<<<<....> """



