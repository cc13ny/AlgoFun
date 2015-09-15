from math import sqrt

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False

        while not num % 2:
            num /= 2
        while not num % 3:
            num /= 3
        while not num % 5:
            num /= 5
        if num == 1:
            return True

        return False