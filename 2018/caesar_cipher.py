import string


class SubstitutionCipher:
    pass


class CaesarCipher(SubstitutionCipher):
    
    def substitute(self, word: str, shift: int) -> str:
        word = list(word)
        alphabet = list(string.ascii_uppercase)
        alphabet_shifted = alphabet[shift:] + alphabet[:shift]
        lookup = {i: j for i,j in zip(alphabet, alphabet_shifted)}
        for i in range(len(word)):
            word[i] = lookup[word[i]]
        return "".join(word)


if __name__ == "__main__":
    cc = CaesarCipher()
    print(cc.substitute("ZZZZ", 1))