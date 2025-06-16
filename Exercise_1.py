# S30 Problem #58 Level Order Traversal in Binary tree
#LeetCode #102 https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Author : Akaash Trivedi
# Time Complexity : O(n) #traverse all node
# Space Complexity : O(n) space by queue
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        #for empty list
        if not root:
            return result

        queue = deque()
        queue.append(root)
        level = 0 # initially level is 0

        #untill queue is not empty
        while queue:
            # at each level we have distinct list
            result.append([])
            # size at the current level
            size = len(queue)

            for i in range(size):
                currNode = queue.popleft()
                # fulfill the current level
                result[level].append(currNode.val)

                # process current childs by adding it to the queue
                # for next level
                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
            
            level += 1 # for next level

        return result