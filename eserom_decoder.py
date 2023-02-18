morse_code = {
    "10" : "A",
    "0111" : "B",
    "0101" : "C",
    "011" : "D",
    "1" : "E",
    "1101" : "F",
    "001" : "G",
    "1111" : "H",
    "11" : "I",
    "1000" : "J",
    "010" : "K",
    "1011" : "L",
    "00" : "M",
    "01" : "N",
    "000" : "O",
    "1001" : "P",
    "0010" : "Q",
    "101" : "R",
    "111" : "S",
    "0" : "T",
    "110" : "U",
    "1110" : "V",
    "100" : "W",
    "0110" : "X",
    "0100" : "Y",
    "0011" : "Z",
    "10000" : "1",
    "11000" : "2",
    "11100" : "3",
    "11110" : "4",
    "11111" : "5",
    "01111" : "6",
    "00111" : "7",
    "00011" : "8",
    "00001" : "9",
    "00000" : "0"
}

def decoder(code):
    final_string = []
    words = code.split("  ")
    for word in words:
        letters = word.split(" ")
        for letter in letters:
            final_string.append(str(morse_code[letter]))
        final_string.append(" ")
    return "".join(final_string)

print(decoder("1111 1 1011 1011 000  100 000 101 1011 011"))
