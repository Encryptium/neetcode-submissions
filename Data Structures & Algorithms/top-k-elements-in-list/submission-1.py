class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCounts = dict()

        for num in nums:
            if num not in numCounts:
                numCounts[num] = 1
            else:
                numCounts[num] += 1

        longestToShortest = set()

        for i in range(k):
            largest = -1
            largestN = None
            for num in numCounts:
                if numCounts[num] > largest:
                    largest = numCounts[num]
                    largestN = num

            longestToShortest.add(largestN)
            numCounts.pop(largestN)

        return list(longestToShortest)