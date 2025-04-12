import random


def main():
    total = 0
    numbers = []
    
    while (total < 100):
        rdnum = random.randint(0, 10)
        if  total + rdnum > 100:
            numbers.append(rdnum)
            break
        else:
            numbers.append(rdnum)
            total += rdnum
        

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
