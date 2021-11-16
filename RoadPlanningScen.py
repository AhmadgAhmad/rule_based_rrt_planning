"""
@ Ahmad Ahmad, V1, 11-16-2021

Find (unfeasible) path in driving scenario  

"""

from mp_algorithms.RRT.rrt import *



def main():
    
    str_bounds = [1, 10, 0, 20] 
    start = [5,0]
    goal = [5,20]
    obstacleList = [(7.5, 5, 1.5)]  # [x, y, radius]
    
    scen = RRT(start=start,obstacle_list=obstacleList,
                goal=goal,play_area=str_bounds,rand_area=[-1,20])
    path = scen.planning(animation=True)

    if path is None:
        print("Cannot find path")
    else:
        print("found path!!")

        # Draw final path
        if True:
            scen.draw_graph()
            plt.plot([x for (x, y) in path], [y for (x, y) in path], '-r')
            plt.grid(True)
            plt.pause(0.01)  # Need for Mac
            plt.show()
           
if __name__ == '__main__':
    main()
