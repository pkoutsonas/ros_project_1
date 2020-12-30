#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from random import randint


def publisher():
    
    pub = rospy.Publisher('Node_2', Int16, queue_size=10)

    rospy.init_node('talker', anonymous=True)

    rate = rospy.Rate(0.5)

    output = Int16()

    while not rospy.is_shutdown():
        output.data = randint(0,1000)

        rospy.loginfo(output)

        pub.publish(output)

        rate.sleep()
    

if __name__ == "__main__":
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
