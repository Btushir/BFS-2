"""
BFS: O(n) and SC: O(n)

"""
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bfs(self, root, ans):
        q = deque()
        q.append(root)
        while q:
            size = len(q)
            lst = []
            for _ in range(size):
                curr = q.popleft()
                lst.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            ans.append(lst[-1])

    def dfs(self, node, level, ans):
        if not node:
            return
        # the lenght of ans will increased when it goes to the left side of tree
        if len(ans) == level:
            ans.append(node.val)

        self.dfs(node.right, level + 1, ans)
        self.dfs(node.left, level + 1, ans)
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        self.bfs(root, ans)
        return ans
