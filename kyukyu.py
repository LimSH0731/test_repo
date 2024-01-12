def do_kyukyu(n:int):
    for i in range(1,9+1):
        print(f'{n} X {i} = {n*i}')


if __name__=='__main__':
    n = int(input('please enter number(1~9): '))
    do_kyukyu(n)

