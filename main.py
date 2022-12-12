
num = list(map(int,input("Enter a number: ").split()))
avg = sum(num)/10
for i in num:

    print(f'{abs(avg-i):.2f}', end=" ")
