# Introduction

The purpose of this assignment is the explore the Feistel cipher and also to help us understand how DES and Triple DES function. It teaches us about multi round ciphers but also the importance of the algorithm and method used to encrypt data for easy encryption and decryption with the right key but making it near impossible to reverse.

# Constraints

We will be limiting our development to the following:

* Python as the development language

* 8 Rounds of the feistel cipher

* Using the same key for all the rounds

* Being able to encrypt and decrypt a few paragraphs of plain text

# Action Plan

Development Plans are as follows:

1. Create a simple "scramble" function which will hide the data while following the rules of the feistel cipher and be easy enough to encrypt and decrypt

2. Execute the encrypt by hand on paper to verify the validity of the approach and that indeed is reversible and functional

3. Write Pseudo of how we initially intend to execute the idea

    1. Please note that our actual code does differ from this but this was the initial approach to the application

## Pseudo Code

This is our initial plan of approach to writing the application. As we continued our development it resulted in slight changes from this to better follow along with the code.

Additionally we are assuming that efficiency and speed are not top priority so we will be using array which will cause additional data. The garbage collector should handle the removal of the data but this is a statement that there are better ways to execute this code.

Assumptions

* 8 rounds

* 64 bit blocks (8 bytes)

* Use same key for each round

Formulas: 

1. f(x, k) = [(2i * k)^x] % ( 2^32 -1)

2. Li = Ri - 1

3. Ri = L[i-1] XOR f(R[i-1], ki) 

### Encryption

    Function Encrypt(Plaintext, key)

        Initialize empty string Ciphertext

        For every 64 bit block of the plaintext

          Initialize array L[8]

          Initialize array R[8]

          Set L[0] to first 32 bits of plaintext block

          Set R[0] to second 32 bits of plaintext block

          For i = 1 to max rounds

          L[i] = R[ i- 1]

          R[i] = L[i - 1] XOR Scramble(R[i - 1], i, key)

        // Add together the final results of each L and R (Lfin and Rfin)

        //Append to the Ciphertext

        Ciphertext += (L[8] + R[8])

        Return Ciphertext

    Function Scramble(x, i, k)

        Return ((xi * k)^i) % (2^32-1)	

### Decryption

    Function Decrypt(Ciphertext, Key)

      Initialize empty string

      For every 64 bit block of the ciphertext

        Array L[8]

        Array R[8]

        L[0] first 32 bit

        R[0] second 32 bit

        For 8 iteration

          R[i+1] = L[i]

          L[i+1] = R[i] Scramble(L[i ], i, key)

        Ciphertext = L[8] + R[8]

      Return ciphertext

    Function Scramble(x, i, k)

      Return ((xi * k)^i) % (2^32-1)

# Instructions

We have two modules: feistel.py and feistel-decrypt.py

Feistel.py is run using python version 2. 

To encrypt a file please run: 

    **Feistel.py -e -m <ecb|cbc> -t <plaintext file> -k <key> -o <ciphertext file>**

Feistel-decrypt.py is run using python version2.

To decrypt a file please run:

    **Feistel.py -d -m <ecb|cbc> -t <ciphertext file> -k <key> -o <resulting plaintext file>**

Please make sure you have the input files for both feistel.py and feistel-decrypt.py in the same directory as the script.** **
