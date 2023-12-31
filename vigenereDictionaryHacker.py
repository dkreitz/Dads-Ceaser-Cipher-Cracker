# Vigenere Cipher Dictionary Hacker
# http://inventwithpython.com/hacking (BSD Licensed)

import detectEnglish, vigenereCipher #, pyperclip


def main():
  ciphertext = """Tzx isnz eccjxkg nfq lol mys bbqq I lxcz."""
  hackedMessage = hackVigenere(ciphertext)

  if hackedMessage is not None:
    #print('Copying hacked message to clipboard:')
    print(hackedMessage)
    #pyperclip.copy(hackedMessage)
  else:
    print('Failed to hack encryption.')


def hackVigenere(ciphertext):
  with open('dictionary.txt', 'r') as fo:
    words = fo.readlines()
    fo.close()

  for word in words:

    word = word.strip()  # remove the newline at the end
    #print('word: ' + word)

    decryptedText = vigenereCipher.decryptMessage(word, ciphertext)
    #print('decryptedText: ' + decryptedText)

    if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
      # Check with user to see if the decrypted key has been found.
      print()
      print('Possible encryption break:')
      print('Key ' + str(word) + ': ' + decryptedText[:100])
      print()
      print('Enter D for done, or just press Enter to continue breaking:')
      response = input('> ')

      if response.upper().startswith('D'):
        return decryptedText


if __name__ == '__main__':
  main()
