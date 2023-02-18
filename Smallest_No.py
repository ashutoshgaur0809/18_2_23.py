T = int(input("Enter no. of test cases = "))
for i in range(T):
    N = int(input())
    K = int(input())
    if (N > K):
        while (N > 1):
            N = N - K
        print(N)
    elif (N == K):
        print("0")
    else:
        print(N)
