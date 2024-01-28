#!/usr/bin/env python3

import rospy

from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

import sys

def perform_trajectory():

    rospy.init_node('kuka_trajectory_publisher') #Node definition

    contoller_name='/joint_states'

    trajectory_publisher = rospy.Publisher(contoller_name,JointTrajectory, queue_size=10) #Publisher Definition

    argv = sys.argv[1:] #It will read the webshell 

    kuka_joints = ['cabeza_motor1', 'motor1_cuerpo1', 'cuerpo1_motor2', 'motor2_cuerpo2', 'cuerpo2_motor3','motor3_cuerpo3','cuerpo3_motor4','motor4_cola'] #Name of joints

    goal_positions = [ float(argv[0]) , float(argv[1]) , float(argv[2]) ,float(argv[3] ), float(argv[4]) , float(argv[5]), float(argv[6]), float(argv[7]) ] #Positions in radians where to move

 

    rospy.loginfo("Goal Position set lets go ! ")

    rospy.sleep(1)

    trajectory_msg = JointTrajectory() #JointTrajectory object declaration

    trajectory_msg.joint_names = kuka_joints

    trajectory_msg.points.append(JointTrajectoryPoint())

    trajectory_msg.points[0].positions = goal_positions

    trajectory_msg.points[0].velocities = [0.0 for i in kuka_joints]

    trajectory_msg.points[0].accelerations = [0.0 for i in kuka_joints]

    trajectory_msg.points[0].time_from_start = rospy.Duration(3)

    rospy.sleep(1)

    trajectory_publisher.publish(trajectory_msg)


if __name__ == '__main__':

    perform_trajectory()