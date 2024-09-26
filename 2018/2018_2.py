words = ["BEN", "GELIJK", "HAL", "KOEK", "MEED", "PERS", "WEND"]

together = "".join(words)
print("".join(sorted(list(together))))

from caesar_cipher import CaesarCipher

cc = CaesarCipher()

for i in range(26):
    print(f"{i}: {cc.substitute('BENGELIJKHALKOEKMEEDPERSWEND', i)}")
    print(f"{i}: {cc.substitute('BENGELIJKHALKOEKMEEDPERSWEND'[::-1], i)}")