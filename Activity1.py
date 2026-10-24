def eq_mid(n):
    arr = [1]*n + [0] + [1]*n
    size = len(arr)
    for i in range(size):
        left_sum = 0
        right_sum = 0
        for j in range(i):
            left_sum += arr[j]
        for k in range(i+1,size):
            right_sum += arr[k]
        if right_sum == left_sum:
            return i
    return -1
p= int(input("Enter a number : "))
print(eq_mid(p))