arr = [[1,0,1],
       [0,1,1],
       [0,1,0]
       ]

newarr = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]

moves = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),         (0, 1),
    (1, -1), (1, 0), (1, 1)
]

for i in range(len(arr)):
    for j in range(len(arr[1])):
        count = 0
        for movex, movey in moves:
            x, y = movex + i, movey + j
            if 0 <= x < len(arr) and 0 <= y < len(arr[0]):
                if arr[x][y] == 1:
                    count += 1
        newarr[i][j] = count

for a in range(len(newarr)):
    print(newarr[a])