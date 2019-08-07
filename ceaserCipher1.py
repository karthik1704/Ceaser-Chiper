# CeaserChiper
# If Any mistake Feel Free to Correct or Issue to me in Github!!


class CeaserChiper:
    # You cab add more Symbols
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ?!.'
    secret_msg = ''
    translated = ''
    private_key = 0

    # Get Details
    def get_mode(self):
        self.secret_msg = input("Enter Secret Message:")
        print('1.Encrypt \n2.Decrypt')
        mode = input('Select 1 or 2:')
        if mode == '1':
            print('Encryption')
            self.encryption()
        elif mode == '2':
            print('Decryption')
            self.decryption()
        else:
            self.get_mode()
    # Encryption

    def encryption(self):
        self.private_key = int(input("Enter Private Key:\t"))
        for symbol in self.secret_msg:
            if symbol in self.SYMBOLS:
                symbolIndex = self.SYMBOLS.find(symbol)
                translatedIndex = symbolIndex + self.private_key
                if translatedIndex >= len(self.SYMBOLS):
                    translatedIndex -= len(self.SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex += len(self.SYMBOLS)

                self.translated += self.SYMBOLS[translatedIndex]
            else:
                self.translated += symbol

        print('Secret Message : ', self.translated)
    # Decryption

    def decryption(self):
        dkeymode = input('Do You Decrpt Key(Y or N):')
        # Private Key Know Section
        if dkeymode.upper() == 'Y':
            self.private_key = int(input("Enter Decrypt Key:\t"))
            for symbol in self.secret_msg:
                if symbol in self.SYMBOLS:
                    symbolIndex = self.SYMBOLS.find(symbol)
                    translatedIndex = symbolIndex - self.private_key
                    if translatedIndex >= len(self.SYMBOLS):
                        translatedIndex -= len(self.SYMBOLS)
                    elif translatedIndex < 0:
                        translatedIndex += len(self.SYMBOLS)

                    self.translated += self.SYMBOLS[translatedIndex]
                else:
                    self.translated += symbol

            print('Secret Message : ', self.translated)
        # Private Key Not Know Section
        elif dkeymode.upper() == 'N':
            # Using For Loop to Indentify Private Key
            for dkey in range(len(self.SYMBOLS)):
                for symbol in self.secret_msg:
                    if symbol in self.SYMBOLS:
                        symbolIndex = self.SYMBOLS.find(symbol)
                        translatedIndex = symbolIndex - dkey
                        if translatedIndex >= len(self.SYMBOLS):
                            translatedIndex -= len(self.SYMBOLS)
                        elif translatedIndex < 0:
                            translatedIndex += len(self.SYMBOLS)

                        self.translated += self.SYMBOLS[translatedIndex]

                    else:
                        self.translated += symbol
                if len(self.translated) <= len(self.secret_msg):
                    print("Private Key:", dkey)
                    print(self.translated)
                    self.translated = ''

    def __init__(self):
        self.get_mode()


CeaserChiper()
