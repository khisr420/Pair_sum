def adder(arr, k):
    temp= 0
    for x in range(0,len(arr)-1):
        temp = arr[x] + arr[x+1]
        if temp ==k:
            print((arr[x], arr[x+1]))
