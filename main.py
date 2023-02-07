a= int(input("Enter a: "))
b= int(input("Enter b: "))

for i in range(a, b+1):
    divisors = []
    sum = 0
    for j in range(1, i):
        if i % j== 0:
            divisors.append(j)
            sum =sum+ j
            if sum == i:
                print(i, "is a perfect number and its divisors are", divisors)