# -*- coding: utf-8 -*-
""" Robotiq Gripper 
    Simple implimentation

 @author Yuki Suga
 @copyright SUGAR SWEET ROBOTICS
"""

import socket
import time


class RobotiqGripper(object):


    def __init__(self, host, port=63352):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((host, port))
        pass

    def __del__(self):
        self._sock.disconnect()

    def gripper_action(self, value):
        #self.__simple_gripper.send( ("SET POS %d\n" % value).encode('utf-8') )
        #self.__simple_gripper.send(b"SET GTO 1\n")
        self._sock.send( ("SET POS %d\n" % value).encode('utf-8') )
        self._sock.send(b"SET GTO 1\n")
        time.sleep(5.0)
        #self.__simple_gripper.send(b"SET GTO 0\n")
        self._sock.send(b"SET GTO 0\n")
        print("gripper_action_send.")
        pass

    def open_gripper(self):
        self.gripper_action(0)#(255)
        print("gripper_opened.")
        pass


    def close_gripper(self):
        self.gripper_action(255)#(0)
        print("gripper_closed.")
        pass

