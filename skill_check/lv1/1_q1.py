def solution(array, commands):
    answer = []
    for l in commands:
        temp = array[l[0] - 1:l[1]]
        temp.sort()
        copy_temp = temp[:]
        answer.append(copy_temp[l[2] - 1])
    
    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
ans = solution(array, commands)
print(ans)