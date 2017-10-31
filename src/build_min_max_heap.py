"""
# Purpose: To build max and min heap for calculating the median
Author: Rohan Gudgila
"""

import heapq


class BuildMinMaxHeap:
    def __init__(self):
        pass

    @staticmethod
    def build_heap(sm, lg, num):
        if len(sm) == 0:
            heapq.heappush(sm, -num)
            return sm, lg
        if num <= - sm[0]:
            # push to small heap
            heapq.heappush( sm, -num)
        else:
            # push to large heap
            heapq.heappush(lg, num)
            # adjust small and large heap to balance
        if len(sm) - len(lg) == 2:
            heapq.heappush(lg, -heapq.heappop( sm))
        elif len(sm) - len(lg) == -2:
            heapq.heappush(sm, -heapq.heappop(lg))
        return sm, lg
