#!/usr/bin/env python3
import time
import cereal.messaging as messaging


class ASLController:
    def __init__(self):
        self.speed = 0
        self.pm = messaging.PubMaster(['advisorySpeedLimit'])

    def _publish_asl_message(self):
        msg = messaging.new_message('advisorySpeedLimit')
        msg.advisorySpeedLimit.speed = self.speed
        msg.valid = True
        msg.advisorySpeedLimit.valid = True
        self.pm.send('advisorySpeedLimit', msg)
        print("[info] Sent advisorySpeedLimit =", self.speed)

    def _adjust_asl(self, amt: int):
        self.speed += amt

    def _quit_test(self):
        print("[info] User requested test quit. Come to a stop safely!")
        exit()

def main():
    testASL = ASLController()

    testASL._publish_asl_message()

    INPUT_MAP = {
        '+' : lambda: testASL._adjust_asl(1),
        '++': lambda: testASL._adjust_asl(5),
        '-' : lambda: testASL._adjust_asl(-1),
        '--': lambda: testASL._adjust_asl(-5),
        'q' : lambda: testASL._quit_test(),
    }

    while True:
        inpt: str = input("[info] Enter a command: ")
        if inpt not in INPUT_MAP:
            print("[ERR!] command not found.")
            continue
        INPUT_MAP[inpt]()
        testASL._publish_asl_message()

if __name__ == "__main__":
    main()
