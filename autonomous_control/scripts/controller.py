#!/usr/bin/env python

import cv2
#import csv
import numpy as np
#import os
#import pyqrcode
#import random
#import string
from sensor_msgs.msg import Image
import rospy
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge, CvBridgeError

# Code used for autonomous control of rover

class controller():
    def __init__(self):
        self._image_sub = rospy.Subscriber('/R1/pi_camera/image_raw', Image, callback=self._image_callback, queue_size=1)
        self._twist_pub = rospy.Publisher('/R1/cmd_vel', Twist, queue_size=1)
        self._bridge = CvBridge()
        rospy.init_node('controller', anonymous=True)

    def _image_callback(self, image):
        try:
            cv_image = self._bridge.imgmsg_to_cv2(image, "bgr8")
        except CvBridgeError as e:
            print(e)
            return
        
        # TODO: process image to follow path

        move_cmd = Twist()
        move_cmd.linear.x = 0.2
        move_cmd.angular.z = 0.1

        self._twist_pub.publish(move_cmd)

if __name__ == "__main__":
    autonomous_driver = controller()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down controller")

    cv2.destroyAllWindows()