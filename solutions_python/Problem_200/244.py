def main():
    with open('/Users/tengg/Downloads/B-large.in') as f:
        t = int(f.readline())
        for i in range(1, t+1):
            upper_bound = int(f.readline()) # string
            print(f"Case #{i}: " + last_tidy_num(upper_bound))

def last_tidy_num(n):
    arr = str(n)
    i = 0
    while i < len(arr)-1 and arr[i] <= arr[i+1]:
        i += 1
    if i == len(arr) - 1:
        return arr
    else:
        j = i
        while j > 0 and arr[j] == arr[j-1]:
            j -= 1
        return str(n - int(arr[j+1:]) - 1)

if __name__ == '__main__':
    main()
    #print(last_tidy_num(str(1110)))