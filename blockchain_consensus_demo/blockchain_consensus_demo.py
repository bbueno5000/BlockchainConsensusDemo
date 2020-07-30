"""
Simple Proof-of-Work example.
"""
import hashlib 
import struct
import sys
import time

class BlockchainConsensus:
    """
    DOCSTRING
    """
    def __call__(self):
        # timestamp, message and payload are the “stuff” sent to the network
        timestamp = str(time.time())
        message = 'this is a random message'
        payload = timestamp + message
        # nonce, guess, throttle and target are used to perform the work
        nonce = 0
        guess = 999999999999
        throttle = 100000000
        target = 2**64 / throttle
        payloadHash = hashlib.sha512(payload.encode('utf-8')).digest()
        start = time.time()
        # the following lines are our proof-of-work algorithm
        while guess > target:
            nonce + 1
            guess, = struct.unpack('>Q', hashlib.sha512(hashlib.sha512(
                struct.pack('>Q', nonce) + payloadHash).digest()).digest()[0:8])
        end = time.time()
        print('%s:%s:%s:%s:%s:%s:%s' % (
            timestamp, message, nonce, guess, payload, target, end-start))

if __name__ == '__main__':
    blockchain_consensus = BlockchainConsensus()
    blockchain_consensus()
 