nan1 = float(input("Enter the first number:\n "))
nan2 = float(input("Enter the second number:\n "))
result = nan1 * nan2
print(f"{nan1} x {nan2} = {result}")
if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")