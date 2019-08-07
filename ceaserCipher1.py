
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ?!.'


def ceaser_chiper(msg, key):
    translated = ''
    for symbol in msg:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex + key
            if translatedIndex >= len(SYMBOLS):
                translatedIndex -= len(SYMBOLS)
            elif translatedIndex < 0:
                translatedIndex += len(SYMBOLS)

            translated += SYMBOLS[translatedIndex]
        else:
            translated += symbol

    return translated


class CeaseChiper:
    SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 ?!.'
    secret_msg = ''
    translated = ''
    private_key = 3

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

    def encryption(self):
        self.private_key = int(input("Enter Private Key:\t"))
        for symbol in self.secret_msg:
            if symbol in self.SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = symbolIndex + self.private_key
                if translatedIndex >= len(SYMBOLS):
                    translatedIndex -= len(SYMBOLS)
                elif translatedIndex < 0:
                    translatedIndex += len(SYMBOLS)

                self.translated += SYMBOLS[translatedIndex]
            else:
                self.translated += symbol

        print('Secret Message : %s', self.translated)

    def decryption(self):
        dkeymode=input('Do You Decrpt Key(Y or N):')
        if dkeymode.upper()=='Y':
            self.private_key = int(input("Enter Decrypt Key:\t"))
            for symbol in self.secret_msg:
                if symbol in self.SYMBOLS:
                    symbolIndex = SYMBOLS.find(symbol)
                    translatedIndex = symbolIndex - self.private_key
                    if translatedIndex >= len(SYMBOLS):
                        translatedIndex -= len(SYMBOLS)
                    elif translatedIndex < 0:
                        translatedIndex += len(SYMBOLS)

                    self.translated += SYMBOLS[translatedIndex]
                else:
                    self.translated += symbol

            print('Secret Message : ', self.translated)

        elif dkeymode.upper()=='N':
            for dkey in range(len(self.SYMBOLS)):
                for symbol in self.secret_msg:
                    if symbol in self.SYMBOLS:
                        symbolIndex = SYMBOLS.find(symbol)
                        translatedIndex = symbolIndex - dkey
                        if translatedIndex >= len(SYMBOLS):
                            translatedIndex -= len(SYMBOLS)
                        elif translatedIndex < 0:
                            translatedIndex += len(SYMBOLS)

                        self.translated += SYMBOLS[translatedIndex]
                        
                    else:
                        self.translated += symbol
            for i in range(0,len(self.translated),len(self.secret_msg)):
                print(self.translated[i:i+4])

       

    def __init__(self):
        self.get_mode()


CeaseChiper()
