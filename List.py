ls = [0, 20, 30, 40, 0, 100, 10]
ls1 = []
ls2 = []

for l in ls:
    if l != 0:
        ls1.append(l)
    else:
        ls2.append(l)

print("List1 of output ", ls1)
print("List2 of output ", ls2)

output = ls1+ls2
print(output)

