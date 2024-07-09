#TimeComplexity - O(mn)
#Space Complexity = O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        a = []
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        top = 0
        right = n - 1
        bottom = m - 1
        while top <= bottom and left <= right:
            #left to right
            for i in range(left, right + 1):
                a.append(matrix[top][i])
            top += 1
            #top to bottom
            for i in range(top, bottom + 1):
                a.append(matrix[i][right])
            right -= 1
            #right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    a.append(matrix[bottom][i])
                bottom -= 1
            #bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    a.append(matrix[i][left])
                left += 1
        
        return a