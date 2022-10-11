num_inputs = []
for i in range(10):
    num = int(input("Enter a number: "))
    num_inputs.append(num)
avg = sum(num_inputs)/10
for i in num_inputs:

    print(f'{abs(avg-i):.2f}', end=" ")
