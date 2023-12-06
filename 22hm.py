# две суммы
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

# Обратное целое число
def reverse_integer(x):
    INT_MAX, INT_MIN = 2**31 - 1, -2**31
    result = 0
    sign = 1 if x >= 0 else -1
    x = abs(x)

    while x != 0:
        digit = x % 10
        x //= 10

        if result > (INT_MAX - digit) // 10:
            return 0  # Переполнение
        result = result * 10 + digit

    return sign * result

# Палиндромное число
def is_palindrome(x):
    if x < 0:
        return False

    original, reversed_num = x, 0
    while x != 0:
        digit = x % 10
        x //= 10
        reversed_num = reversed_num * 10 + digit

    return original == reversed_num

# Римские цифры в число
def roman_to_int(s):
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for char in s:
        value = roman_values[char]
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value

    return result

# Самый длинный общий префикс
def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]
    for string in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
            i += 1
        prefix = prefix[:i]

    return prefix
