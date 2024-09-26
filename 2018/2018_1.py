from caesar_cipher import CaesarCipher

SEQ1 = ["CONSENSUS", "ARMKRACHT", "VREDEVUUR", "AGNOSTICI", "LUIAARDIJ", "ENKELVOUD", "RIJTUIGJE", "IJSDUIKER"]
SEQ2 = ["VERSLOEG", "VEROVERD", "MILLIADE", "AARDNOOT", "DYNASTIE", "BOTTELEN", "GENERAAL"]


def print_verticals(seq: list[str]):
    for i in range(len(seq[0])):
        res = ""
        for word in seq:
            res += word[i]
        print(res)


def print_all_shifted_verticals(seq: list[str]):
    cc = CaesarCipher()
    for i in range(26):
        print(f"Printing verticals with shift {i}")
        shifted_sequence = [cc.substitute(word, i) for word in seq]
        print_verticals(shifted_sequence)


if __name__ == "__main__":
    print_all_shifted_verticals(SEQ2)