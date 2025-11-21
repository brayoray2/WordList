import numpy as np
data = np.loadtxt('loop4.csv', delimiter=',', dtype=str, encoding = 'utf8')
def num_letters(num_rows,num_col):
    return(num_rows+num_col)*2 - 4
assert num_letters(3,4) == 10 
words = []
rows,columns = data.shape
c = 0
while c < columns:
    words.append(str(data[0,c]))
    c += 1
r = 1
while r < rows:
    words.append(str(data[r,c-1]))
    r += 1
c = columns - 2
while c >= 0:
    words.append(str(data[r-1,c]))
    c -= 1
r = rows - 2
while r > 0:
    words.append(str(data[r,0]))
    r -= 1
print(words)
