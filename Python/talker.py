#!/usr/bin/env python

# This is basically just example code

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry

test_msg = Odometry()

def talker():
    pub = rospy.Publisher('/odom', Odometry, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # The rate that messages will be sent, given in Hz
    while not rospy.is_shutdown():
        rospy.loginfo(test_msg)
        pub.publish(test_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass