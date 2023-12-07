while True:
    StartNum = int(input("Enter a number [start]: "))
    if StartNum == 0:
        break
    elif StartNum < 0:
        print("Enter non-negative numbers.\n ")
        continue
    EndNum = int(input("Enter a number [end]: "))

    if EndNum < 0:
        print("Enter non-negative numbers.\n ")
    elif EndNum <= StartNum:
        print(f"Enter a number greater than {StartNum}.\n ")
    else:
        print(f"Prime numbers between {StartNum} and {EndNum} are: ", end="")
        for num in range(StartNum, EndNum + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num, end=" ")
        print("\n")
