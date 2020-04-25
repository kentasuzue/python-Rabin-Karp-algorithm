# python3
from typing import List
from random import randint

class PolynomialHash:
    def __init__(self, text:str, pattern_length:int):
        #self.prime = 1_000_003
        self.prime = 500_009

        #self.polynomial_variable = randint(1, self.prime - 1)
        #self.polynomial_variable = 1
        self.different_hash_functions = 4
        self.polynomial_variable = [randint(1, self.prime - 1) for _ in range(self.different_hash_functions)]

        self.text = text
        self.pattern_length = pattern_length
        self.index_of_start_of_last_string_in_text = len(self.text) - pattern_length  # text is 0 indexed
        #self.precomputed_hashes = [-1 for _ in range(self.index_of_start_of_last_string_in_text + 1)]

        #self.precomputed_hashes = [self.prime - 1 for _ in range(self.index_of_start_of_last_string_in_text + 1)]
        #self.precomputed_hashes = [[None for _ in range(self.index_of_start_of_last_string_in_text + 1)] for _ in range(self.different_hash_functions)]
        self.precomputed_hashes = [[None for _ in range(self.different_hash_functions)] for _ in range(self.index_of_start_of_last_string_in_text + 1)]
        #self.precomputed_hashes = [self.prime - 1 for _ in range(self.index_of_start_of_last_string_in_text + 1)]

    def get_polyhash(self, string_to_hash: str, distinct_hash_function: int)->int:
        hash_of_string = 0
        for string_index in range(len(string_to_hash) - 1, -1, -1):
            hash_of_string = (hash_of_string * self.polynomial_variable[distinct_hash_function] \
                               + ord(string_to_hash[string_index])) % self.prime
        return hash_of_string

    def get_highest_degree_variable(self, degree: int, distinct_hash_function)->int:
        highest_degree_variable = 1
        for _ in range(degree):
            highest_degree_variable = (highest_degree_variable * self.polynomial_variable[distinct_hash_function]) % self.prime
        return highest_degree_variable % self.prime
        #return self.polynomial_variable**degree

    def precompute_hashes(self) -> List[List[int]]:
        string_at_text_tail = self.text[-self.pattern_length:]

        for distinct_hash_function in range(self.different_hash_functions):
            self.precomputed_hashes[self.index_of_start_of_last_string_in_text][distinct_hash_function] = self.get_polyhash(string_at_text_tail, distinct_hash_function)

            #highest_degree_variable = self.get_highest_degree_variable(self.pattern_length) % self.prime
            highest_degree_variable = self.get_highest_degree_variable(self.pattern_length, distinct_hash_function)

            for start_of_string_in_text in range(self.index_of_start_of_last_string_in_text - 1, -1, -1):
                self.precomputed_hashes[start_of_string_in_text][distinct_hash_function] = \
                    (
                    self.polynomial_variable[distinct_hash_function] * self.precomputed_hashes[start_of_string_in_text + 1][distinct_hash_function] \
                    + ord(self.text[start_of_string_in_text]) \
                    - highest_degree_variable * ord(self.text[start_of_string_in_text + self.pattern_length]) \
                    + self.prime
                    ) % self.prime
        return self.precomputed_hashes

def read_input():
    #return (input().rstrip(), input().rstrip())
    return (input().strip(), input().strip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):

    if text == '' or pattern == '':
        return []

    polyhash = PolynomialHash(text, len(pattern))

    pattern_hash = [polyhash.get_polyhash(pattern, distinct_hash_function) for distinct_hash_function in range(polyhash.different_hash_functions)]
    #print(f"pattern_hash {pattern_hash}")
    text_hashes = polyhash.precompute_hashes()

    #print(text_hashes)

    pattern_positions_in_text = []

    for start_string_index_of_text_hashes, distinct_hash_functions_text_hashes in enumerate(text_hashes):
        #print(f"index_of_text_hashes {index_of_text_hashes} text_hash {text_hash}")
        if all(pattern_hash[distinct_hash_function] == distinct_hash_functions_text_hashes[distinct_hash_function] for distinct_hash_function in range(polyhash.different_hash_functions)):
            pattern_positions_in_text.append(start_string_index_of_text_hashes)

    #print(pattern_positions_in_text)

    return pattern_positions_in_text

    """
    dumb_hashes = []
    for index in range(len(text) - len(pattern) + 1):
        dumb_hashes.append(polyhash.get_polyhash(text[index:index + len(pattern)]))
    print(f"dumb_hashes {dumb_hashes}")

    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if text[i:i + len(pattern)] == pattern
    ]
    """
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
    #print_occurrences(get_occurrences(' ', ''))

