def repeat_string(str, n):
    result = str * n  
    return result

input_str, input_n = input().split()

n = int(input_n)

output_str = repeat_string(input_str, n)
print(output_str)
