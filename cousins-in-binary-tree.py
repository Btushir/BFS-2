"""
BFS: O(n) and SC: O(n)
Todo:: DFS
"""
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, node, x, y):
        q = deque()
        q.append((node, None))

        while q:
            size = len(q)
            # need to be updated for each level, since it is possible the nodes are found but not at same level
            x_found, y_found = False, False
            x_p, y_p = None, None
            for _ in range(size):
                curr, parent = q.popleft()
                if curr.val == x:
                    x_found = True
                    x_p = parent

                if curr.val == y:
                    y_found = True
                    y_p = parent

                if curr.left:
                    q.append((curr.left, curr))
                if curr.right:
                    q.append((curr.right, curr))

            # need to be processed after each level.
            if x_found and y_found:
                return x_found, y_found, x_p, y_p

            # If only one node is found at this level, they cannot be cousins
            if x_found or y_found:
                return False, False, None, None

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_found, y_found, x_p, y_p = self.bfs(root, x, y)
        if (x_found and y_found) and (x_p != y_p):
            return True
        else:
            return False



