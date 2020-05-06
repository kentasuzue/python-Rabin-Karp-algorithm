# python-Rabin-Karp-algorithm-find-pattern-in-text
This Python implementation of the Rabin-Karp algorithm finds the location of every occurence of a pattern string in a text string with O(N) time complexity, versus the naive approach with O(N^2) time complexity. The pattern string is no longer than the text string.

The program accepts as inputs:
  a first console input, the pattern string to search for in the text string.
  a second console input, the text string.

In the class Polynomial, in the method __init__:
  self.prime should be a prime number that is larger than the length of the text string.
  self.different_hash_functions indicates how many polynomial hash functions are used to distinguish an actual occurrence of the pattern string from just a collision.  
  The polynomial variable of each polynomial hash function is randomly chosen from the range [1, self.prime - 1]
 
