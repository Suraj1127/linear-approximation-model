#!/usr/bin/env python3
"""
Author: Suraj Regmi
Date: 3rd July, 2018
Description: Linear model approximating non-linear functions
"""

import numpy as np
import matplotlib.pyplot as plt


class LinearApproximationModel:
    def __init__(self, original_function, derivative_function, range, intervals):
        """
        LinearApproximationModel to model any non-linear equation by conditional
        linear equations.
        :param original_function: the original function to plot
        :param derivative_function: derivative of the original function
        :param range: range on which the plot is to be made
        :param intervals: no of intervals in which the range is to be divided
        """
        self.original_function = original_function
        self.derivative_function = derivative_function
        self.range = range
        self.intervals = intervals

    def set_ranges(self):
        """
        Sets the ranges(or domain) of all the intervals

        Instance variables:
        spot_points: the points in the range
        slopes: slopes at the spot_points
        value_ranges: list of ranges of all the intervals

        """

        self.spot_points = np.linspace(self.range[0], self.range[1], self.intervals)
        del_x = (self.range[1]-self.range[0])/((self.intervals-1)*2)
        self.slopes = eval(self.derivative_function.format(list(self.spot_points)))
        self.value_ranges = list(zip(self.spot_points-del_x, self.spot_points+del_x))

    def approximate_graph(self):
        """
        Draw the approximate graph using linear approximation with local derivatives(slopes)

        Color notation:
        Approximate graph: green
        Real graph: blue
        """
        for i, j in enumerate(self.value_ranges):
            x_t = np.linspace(j[0],j[1],2)
            y_t = self.slopes[i]*(x_t-self.spot_points[i])+eval(self.original_function.format(self.spot_points[i]))

            # Approximate graph
            # Have only one legend for approximate graph
            if i == 0:
                plt.plot(x_t, y_t, color='green', label='Approximate function')
            else:
                plt.plot(x_t, y_t, color='green')

        # actual graph
        plt.plot(
            np.linspace(self.range[0], self.range[1], 100),
            eval(self.original_function.format(list(np.linspace(self.range[0], self.range[1], 100)))),
            color='blue',
            label='Real function'
        )

        # For labelling and legends
        plt.xlabel('x')
        plt.ylabel('y')

        plt.legend()
        plt.show()


def main():

    # Take function and its derivative in numpy format
    function = input("Enter the function in 'x':\n")
    derivative_function = input("Enter its derivative in 'x':\n")

    function = function.replace('x', 'np.array({})')
    derivative_function = derivative_function.replace('x', 'np.array({})')

    # Take range in which the plot is to be drawn
    rangee = [int(i) for i in input("Enter the range in which the plot is to be drawn.\n"
                   "The lower value and upper value is to be separated by spaces.\n").strip().split()]

    # Take number of middle points with which the curve is to be approximated.
    no_of_points = int(input("Enter the number of middle points with which the curve is to be approximated.\n").strip())

    # Build instance of LinearApproximateModel class and then approximate the graph
    approximation_model = LinearApproximationModel(function, derivative_function, rangee, no_of_points)
    approximation_model.set_ranges()
    approximation_model.approximate_graph()

    print("The real function and approximate function are plotted as shown in screen.")


if __name__ == "__main__":
    main()