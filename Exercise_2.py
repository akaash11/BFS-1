# S30 Problem #59 Course Schedule
#LeetCode #207 https://leetcode.com/problems/course-schedule/description/

# Author : Akaash Trivedi
# Time Complexity : O()
# Space Complexity : O()
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hashm = {}
        indegree = [0] * numCourses
        # build a graph
        for c in prerequisites:
            # independent to dependent mapping
            # c[0] is dependent and c[1] is independent
            hashm[c[1]] = hashm.get(c[1], []) + [c[0]]
            indegree[c[0]] += 1
        
        count = 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
                count +=1
        if not queue:
            return False
        
        while queue:
            currCourse = queue.popleft()
            for dependentC in hashm.get(currCourse, []):
                indegree[dependentC] -= 1
                if indegree[dependentC] == 0:
                    queue.append(dependentC)
                    count +=1
                    if numCourses == count:
                        return True
        return numCourses == count