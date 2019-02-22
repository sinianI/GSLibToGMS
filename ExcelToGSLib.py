import numpy as np
import pandas as pd
import xlrd

df = pd.read_csv('Region.csv', header=None)

matrix = np.asmatrix(df)

#print(matrix)

M, N = np.shape(matrix)


a = np.flip(matrix, 0)

b = np.reshape(a, (M*N, 1))

print(b)

hdr_str = """{M:d} {N:d} 1
1
facies""".format(M=M,N=N)
outfile = 'Region.txt'
np.savetxt(outfile,b,header=hdr_str,comments='')