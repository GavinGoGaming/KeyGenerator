np = input("Is there any namespace? Keep empty if none:")
print("You have put " + np)
key = input("Key:")
print("You have put " + key)
native = input("Native:")
print("You have put " + native)
newStr = input("NewText:")
print("You have put " + newStr)
print("+TextReplacements=(Category=Game, bIsMinimalPatch=True, Namespace=" + np +", Key=" + key + ", NativeString=" + native + ", LocalizedStrings=((\"ar\", " + newStr + "),(\"en\", " + newStr + "),(\"de\", " + newStr + "),(\"es\", " + newStr + "),(\"es-419\", " + newStr + "),(\"fr\", " + newStr + "),(\"it\", " + newStr + "),(\"ja\", " + newStr + "),(\"ko\", " + newStr + "),(\"pl\", " + newStr + "),(\"pt-BR\", " + newStr + "),(\"ru\", " + newStr + "),(\"tr\", " + newStr + "),(\"zh-CN\""", " + newStr + "),(\"zh-Hant\", " + newStr + ")))")