# Number and emoji converter using dictionaries and functions
def emoji_convertor(char):
    output = ""
    emoji = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        ":)": "😀",
        ":(": "😥",
        ":/": "😐"
    }
    for ch in char:
        output += " " + emoji.get(ch, ch)
    return output


message = (input("Enter message including text emojis and numbers:\n"))
message2 = message.split(" ")
print(emoji_convertor(message2))
