# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


from operator import length_hint


def find_anagram(words, anagrams):
    # [assignment] Add your code here
  
  str1 = words.lower()
  str2 = anagrams.lower()
  if len(str1) == len(str2) :
        sort_str1 = sorted(str1)
        sort_str2 = sorted(str2)


        if sort_str1 == sort_str2 : 
          print(True)
          return True
          
        
        else:
          print(False)
          return False

  else:
     print(False)
     return False
     
words = input("please enter the first word:")
anagrams = input("please enter the second word:") 

find_anagram(words,anagrams)

