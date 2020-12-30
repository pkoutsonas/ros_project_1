#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16


class Server:
    def __init__(self):
        self.node1 = None
        self.node2 = None

    def node1_callback(self, msg):
        self.node1 = msg.data

        self.printing()

    def node2_callback(self, msg): 
        self.node2 = msg.data

        # self.printing()

    def printing(self):

        list1 = [self.node1, self.node2]

        if self.node1 != self.node2 :
            if is_prime(min(list1)):
                rospy.loginfo(" Printing : %d" %min(list1) )
            else :
                rospy.loginfo(" Printing : %d" %max(list1))
        else :
            rospy.loginfo("They are equals!")

            
        
def is_prime(num):

    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
                break
            else:
                return True
    else:
        return False


if __name__ == '__main__':
    rospy.init_node('listener')

    server = Server()

    rospy.Subscriber("Node_1", Int16 , server.node1_callback)

    rospy.Subscriber("Node_2", Int16, server.node2_callback)

    rospy.spin()