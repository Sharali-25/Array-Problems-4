def winsum(o):
    arr = [0]*o + [1]*o
    size = len(arr)
    for i in range(size - o+1):
        current_sum = 0
        for j in range(i,i+1):
           current_sum += arr[j] 
        if current_sum == o:
            return i
        return -1
print(winsum)
l = int(input("Enter a number : "))
print(winsum(l))