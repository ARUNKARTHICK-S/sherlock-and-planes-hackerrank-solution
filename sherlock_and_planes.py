import os
def solve(points):
    if((points[0][1] == points[1][1]== points[2][1]== points[3][1]) | (points[0][0] == points[1][0]== points[2][0]== points[3][0]) | (points[0][2] == points[1][2]== points[2][2]== points[3][2])):
        return "YES" 
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        points = []

        for _ in range(4):
            points.append(list(map(int, input().rstrip().split())))

        result = solve(points)

        fptr.write(result + '\n')

    fptr.close()
