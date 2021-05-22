# Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Score: 10


def readScores(listOfStudents):
    line = list(input().split())
    avScore = sum(map(float, line[1:])) / 3
    name = line[0]
    listOfStudents[name] = avScore


n = int(input())
listOfStudents = dict()
for i in range(n):
    readScores(listOfStudents)
print('%.2f' % listOfStudents[input()])

# Alternative Solution

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
    
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     query_scores = student_marks[query_name]
#     print("{0:.2f}".format(sum(query_scores)/len(query_scores)))