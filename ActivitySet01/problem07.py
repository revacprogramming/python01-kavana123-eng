#Loops and iterations

largest = None
smallest = None

while True:
    num = input("Enter a number:")
    if num == 'done':
        break;
    try:
        n = int(num)
    except:
        print("Invalid input")
        
        
    if largest is None:
            largest = n
    elif n>largest:
            largest = n
    if smallest is None:
            smallest = n
    elif n<smallest:
            smallest = n
            
print("Maximum is",largest)
Print("Minimum is",smallest)