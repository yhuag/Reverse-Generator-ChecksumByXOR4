### Usage
The program takes in a "target word", and generate several "possible words". The relationship is that possible words can be encrypted and generated along with a checksum. This checksum will be identical to the target word given, so as to breach Integrity.

### Checksum Algorithm
The checksum algorithm is rather simple and insecure: The checksum is 4 bytes long, and it is done by adding the bytes of the ciphertext together, by first dividing the ciphertext into blocks of 4 bytes and then XORing each block with the next. (copied from HKUST COMP3632 spring 2017 Assignment 2 instruction)
