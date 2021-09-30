
#Laith code
# class Solution:

#     @staticmethod
#     def longest_palindromic(s: str) -> str:
#         pass

#Noora code
class String(object):
   def longestPalindrome(self, str):
      dp = [[False for i in range(len(str))] for i in range(len(str))]
      for i in range(len(str)):
         dp[i][i] = True
      max_length = 1
      start = 0
      for L in range(2,len(str)+1):
         for i in range(len(str)-L+1):
            end = i+L
            if L==2:
               if str[i] == str[end-1]:
                  dp[i][end-1]=True
                  max_length = L
                  start = i
            else:
               if str[i] == str[end-1] and dp[i+1][end-2]:
                  dp[i][end-1]=True
                  max_length = L
                  start = i
      return str[start:start+max_length]
stro1 = String()
print("Enter a string:")
str = input()
print("Longest palindromic solution:",stro1.longestPalindrome(str))
