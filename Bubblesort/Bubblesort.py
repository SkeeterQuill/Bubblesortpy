def bubble(list):
    n = len(list)
    changes = 1
    
    while changes > 0:
        changes = 0
        for i in range(n-1):
            if list[i] > list[i+1]:
                a = list[i]
                b = list[i+1]
                list[i]=b
                list[i+1]=a
                changes = changes + 1
                
list = [6,34,7,45,3,98]

bubble(list)

for i in range(len(list)):
    print(list[i])
