def solution(n,a,b):
    answer = 0
    index_a, index_b = a, b
    while index_a != index_b:
        if index_a % 2 == 0:
            index_a //= 2
        else:
            index_a //= 2
            index_a += 1

        if index_b % 2 == 0:
            index_b //= 2
        else:
            index_b //= 2
            index_b += 1
        
        answer += 1
    return answer
        
        
    

print(solution(8, 4, 7))

