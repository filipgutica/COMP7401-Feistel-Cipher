import sys, getopt, hashlib
from math import exp, expm1

ROUNDS = 8
BLOCKSIZE = 8
BLOCKSIZE_BITS = 64
PATH_TO_FILES = "Files/"
SECRET = "3f788083-77d3-4502-9d71-21319f1792b6"

def main(argv):
    decrypt = False
    encrypt = False

    try:
        opts, args = getopt.getopt(argv, "hdem:t:k:o:", [" mode ='', ptext=", "key=", "outfile="])

    except getopt.getoptError:
        sys.exit(1)

    if len(sys.argv[1:]) < 6:
        print ('Usage: ./feistel.py -[d|e] -m <mode> -t <inputfile> -k <key> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Usage: ./feistel.py -[d|e] -m <mode> -t <inputfile> -k <key> -o <outputfile>')
            sys.exit()
        elif opt == "-d":
            decrypt = True
        elif opt == "-e":
            encrypt = True
        elif opt in ("-m", "--mode"):
            mode = str(arg).lower()
        elif opt in ("-t", "--ptext"):
            filename = str(arg)
        elif opt in ("-k", "--key"):
            key = str(arg)
        elif opt in ("-o", "--outfile"):
            outfilename = str(arg)

    if (encrypt and decrypt):
        print("Cannot encrypt AND decrypt")
        sys.exit(1)

    if (mode != "ecb" and mode != "cbc"):
        print ("Unknown cryptographic mode")
        sys.exit(1)


    with open(PATH_TO_FILES + filename, "r") as f:
        input = f.read()

    # call the crypto function
    if (encrypt):
        output = encryptMessage(key, input, mode)
    elif (decrypt):
        output = decryptCipher(key, input, mode)

    with open(PATH_TO_FILES + outfilename, 'w+') as fw:
        fw.write(output)

    # Print the ciphertext

    #print(ciphertext)


def encryptMessage(key, message, mode):
    ciphertext = ""
    n = BLOCKSIZE  # 8 bytes (64 bits) per block

    # Split mesage into 64bit blocks
    message = [message[i: i + n] for i in range(0, len(message), n)]

    lengthOfLastBlock = len(message[len(message)-1])

    if ( lengthOfLastBlock < BLOCKSIZE):
        for i in range(lengthOfLastBlock, BLOCKSIZE):
            message[len(message)-1] += " "

    #print(message)

    # generate a 256 bit key based of user inputted key
    key = key_256(key)
    key_initial = key
    for block in message:
        #print ("Block: " + block)
        L = [""] * (ROUNDS + 1)
        R = [""] * (ROUNDS + 1)
        L[0] = block[0:BLOCKSIZE/2]
        R[0] = block[BLOCKSIZE/2:BLOCKSIZE]

        #print ("L Initial: " + L[0])
        #print ("R Initial: " + R[0])

        for i in range(1, ROUNDS+1):

            L[i] = R[i - 1]
            if (mode == "cbc"):
                if (i == 1):
                    key = key_initial
                else:
                    key = subkeygen(L[i], key_initial, i)
            R[i] = xor(L[i - 1], scramble(R[i - 1], i, key))

        ciphertext += (L[ROUNDS] + R[ROUNDS])

    return ciphertext

def decryptCipher(key, ciphertext, mode):
    message = ""
    n = BLOCKSIZE  # 8 bytes (64 bits) per block

    # Split message into 64bit blocks
    ciphertext = [ciphertext[i: i + n] for i in range(0, len(ciphertext), n)]

    lengthOfLastBlock = len(ciphertext[len(ciphertext)-1])

    if ( lengthOfLastBlock < BLOCKSIZE):
        for i in range(lengthOfLastBlock, BLOCKSIZE):
            ciphertext[len(ciphertext)-1] += " "


    # generate a 256 bit key based off the user inputted key
    key = key_256(key)
    key_initial = key
    for block in ciphertext:
        #print ("Block: " + block)
        L = [""] * (ROUNDS + 1)
        R = [""] * (ROUNDS + 1)
        L[ROUNDS] = block[0:BLOCKSIZE/2]
        R[ROUNDS] = block[BLOCKSIZE/2:BLOCKSIZE]

        # print ("L Initial: " + L[0])
        # print ("R Initial: " + R[0])

        for i in range(8, 0, -1):

            if (mode == "cbc"):
                key = subkeygen(L[i], key_initial, i)

                if (i == 1):
                    key = key_initial

            R[i-1] = L[i]
            L[i-1] = xor(R[i], scramble(L[i], i, key))


        message += (L[0] + R[0])

    return message


def key_256(key):
    return hashlib.sha256(key + SECRET).hexdigest()

def subkeygen(s1, s2, i):
    #print ("GENERATING KEY #" + str(i))
    #print ("S1: " + s1)
    #print ("S2: " + s2)
    result = hashlib.sha256(s1 + s2).hexdigest()
    #print ("RESULT: " + result)
    return result

def scramble(x, i, k):
    k = stobin(k)
    x = stobin(str(x))

    k = bintoint(k)
    x = bintoint(x)

    res = pow((x * k), i)
    res = itobin(res)

    return bintostr(res)


# xor two strings
def xor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


# string to binary
def stobin(s):
    return ''.join('{:08b}'.format(ord(c)) for c in s)


# binary to int
def bintoint(s):
    return int(s, 2)


# int to binary
def itobin(i):
    return bin(i)


# binary to string
def bintostr(b):
    n = int(b, 2)
    return ''.join(chr(int(b[i: i + 8], 2)) for i in xrange(0, len(b), 8))


if __name__ == "__main__":
    main(sys.argv[1:])
