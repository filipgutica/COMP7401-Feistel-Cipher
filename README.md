# Introduction

The purpose of this assignment is the explore the Feistel cipher and also to help us understand how DES and Triple DES function. It teaches us about multi round ciphers but also the importance of the algorithm and method used to encrypt data for easy encryption and decryption with the right key but making it near impossible to reverse.

# Constraints

We will be limiting our development to the following:

* Python as the development language

* N Rounds of the feistel cipher

* Subkey generation

* ECB and CBC modes

* 64 bit blocks (8 bytes)

# Action Plan

Development Plans are as follows:

1. Create a simple "scramble" function which will hide the data while following the rules of the feistel cipher and be easy enough to encrypt and decrypt

2. Execute the encrypt by hand on paper to verify the validity of the approach and that indeed is reversible and functional

3. Write Pseudo of how we initially intend to execute the idea

    1. Please note that our actual code does differ from this but this was the initial approach to the application

Formulas: 

1. f(x, k) = [(2i * k)^x] % ( 2^32 -1)

2. Li = Ri - 1

3. Ri = L[i-1] XOR f(R[i-1], ki) 


# Instructions

We have two modules: feistel.py and feistel-decrypt.py

Feistel.py is run using python version 2. 

To encrypt a file please run: 

    **Feistel.py -e -m <ecb|cbc> -t <plaintext file> -k <key> -o <ciphertext file>**

Feistel-decrypt.py is run using python version2.

To decrypt a file please run:

    **Feistel.py -d -m <ecb|cbc> -t <ciphertext file> -k <key> -o <resulting plaintext file>**

Please make sure you have the input files for both feistel.py and feistel-decrypt.py in the same directory as the script.** **
