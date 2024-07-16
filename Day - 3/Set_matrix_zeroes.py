class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arrI, arrJ = set(),set()
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    arrI.add(i)
                    arrJ.add(j)
        for i in range(rows):
            for j in range(cols):
                if(i in arrI or j in arrJ):
                    matrix[i][j] = 0
        
