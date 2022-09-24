class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=s.split(" ")
        # print(l)
        o=[]
        for i in l:
            o.append(i[::-1])
        # print(o)
        s=""
        for i in range(len(o)):
            s+=o[i]
            if i<len(o)-1:
                s+=" "
        # print(s)
        return s
