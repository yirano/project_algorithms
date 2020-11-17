'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n, arr=[]):
    dict = [1, 1, 2, 4]
    i = 4
    if n < 4:
        return dict[n]
    else:
        while i <= n:
            dict.append(sum(dict[i-3:i]))
            i += 1

    return dict[len(dict)-1]


def eating_cookies_1(n, arr=[]):
    arr = [1, 2, 3]
    if n == 0:
        return 1
    if n < 0:
        return 0
    ct = 0
    for i in range(len(arr)):
        ct += eating_cookies(n - arr[i])
    return ct


# Courtesy of Adam Young
def eating_cookies(n, cache):
    if n == 0:
        cache[n] = 1
    if n == 1 or n == 2:
        cache[n] = n
    if cache[n] == 0:
        cache[n] = eating_cookies(
            n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    return cache[n]

# print(eating_cookies(500))

# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(
#         f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
