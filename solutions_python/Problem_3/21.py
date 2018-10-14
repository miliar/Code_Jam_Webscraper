"""started 13h30

"""

from math import *

import psyco
psyco.full()

_debug = 0



class solve_case:
    def __init__(self, case_no, f, R, t, r, g):
        self.f = f
        self.R = R
        self.t = t
        self.r = r
        self.g = g

        #f, R, t, r, g = self.f, self.R, self.t, self.r, self.g


        print "\n\n-------------- New case", case_no
        print "radius is", R - t - f
        



    def solve_it(self):
        f, R, t, r, g = self.f, self.R, self.t, self.r, self.g

        # The fly can't even go thru !!
        if f*2 >= g:
            return 1.


        x_left_corners_l = self.get_left_corners_l()
        x_right_corners_l = [item + g - 2*f for item in x_left_corners_l]

        nb_gaps = len(x_left_corners_l)
        

        area_the_fly_can_go_int = 0
        area_the_fly_can_go_float = 0.
        area_racquet = R**2 * pi / 4
        radius_inside = R-t-f
        
        self.radius_inside = radius_inside

        area_gap = (g-2*f) **2

        for n_y in range(nb_gaps):
            for n_x in range(nb_gaps):
                square_bottom_left_t = x_left_corners_l[n_x], x_left_corners_l[n_y]
                square_bottom_right_t = x_right_corners_l[n_x], x_left_corners_l[n_y]
                square_top_left_t = x_left_corners_l[n_x], x_right_corners_l[n_y]
                square_top_right_t = x_right_corners_l[n_x], x_right_corners_l[n_y]
        
                bottom_left_is_inside = self.is_inside(*square_bottom_left_t)
                bottom_right_is_inside = self.is_inside(*square_bottom_right_t)
                top_left_is_inside = self.is_inside(*square_top_left_t)
                top_right_is_inside = self.is_inside(*square_top_right_t)

                inside_t = (bottom_left_is_inside, bottom_right_is_inside, top_left_is_inside, top_right_is_inside)
                                          
                
                if inside_t == (True, True, True, True):
                    area_the_fly_can_go_int += area_gap

                elif inside_t == (True, False, False, False):
                    if _debug:
                        print "%d, %d : case 1" % (n_x, n_y),
                    # Just the bottom left corner is in the circle
                    x, y = square_bottom_left_t
                    secteur_angle = acos(1.*x/ radius_inside) - asin(1.*y / radius_inside)
                    assert secteur_angle < pi/4, "secteur_angle should be < 90deg"

                    area_courbure = self.get_area_courbure(secteur_angle)
                    

                    x_intersec = self.get_other_coord_on_circle(y)
                    y_intersec = self.get_other_coord_on_circle(x)
                    
                    area_small_triangle = (x_intersec - x) * (y_intersec - y) /2

                    assert area_small_triangle < area_gap, "area_small_triangle should be < area_gap"
                    

                    to_add = area_courbure + area_small_triangle
                    assert to_add > 0, "to_add should be >0"

                    if _debug: print to_add
                    
                    area_the_fly_can_go_float += to_add

                elif inside_t == (True, True, False, False):
                    # Just the bottom left and bottom right corners are in the circle  
                    if _debug:
                        print "%d, %d : case 2" % (n_x, n_y),
                        
                    x_l, y = square_bottom_left_t
                    x_r, dummy = square_bottom_right_t
                    
                    secteur_angle = acos(1.*x_l/ radius_inside) - acos(1.*x_r / radius_inside)
                    assert secteur_angle < pi/4, "secteur_angle should be < 90deg"

                    area_courbure = self.get_area_courbure(secteur_angle)

                    y_intersec_l = self.get_other_coord_on_circle(x_l)
                    y_intersec_r = self.get_other_coord_on_circle(x_r)

                    area_trapeze = (y_intersec_l + y_intersec_r - 2 * y) * (x_r - x_l) /2

                    to_add = area_courbure + area_trapeze
                    assert to_add > 0, "to_add should be >0"
                    if _debug: print to_add
                    
                    area_the_fly_can_go_float += to_add
                    
                    
                elif inside_t == (True, False, True, False):
                    # Just the bottom left and top left corners are in the circle  
                    if _debug:
                        print "%d, %d : case 3" % (n_x, n_y),

                    x, y_b = square_bottom_left_t
                    dummy, y_t = square_top_left_t

                    secteur_angle = asin(1.*y_t/ radius_inside) - asin(1.*y_b / radius_inside)
                    assert secteur_angle < pi/4, "secteur_angle should be < 90deg"

                    area_courbure = self.get_area_courbure(secteur_angle)

                    x_intersec_t = self.get_other_coord_on_circle(y_t)
                    x_intersec_b = self.get_other_coord_on_circle(y_b)

                    area_trapeze = (x_intersec_t + x_intersec_b - 2 * x) * (y_t - y_b) /2

                    to_add = area_courbure + area_trapeze
                    assert to_add > 0, "to_add should be >0"
                    if _debug: print to_add
                    
                    area_the_fly_can_go_float += to_add
                        
                    
                elif inside_t == (True, True, True, False):
                    # Just the top right corner is not in the circle  
                    if _debug:
                        print "%d, %d : case 4" % (n_x, n_y),
                        
                    x_l, y_b = square_bottom_left_t
                    x_r, dummy = square_bottom_right_t
                    dummy, y_t = square_top_left_t

                    secteur_angle = asin(1.*y_t/ radius_inside) - acos(1.*x_r / radius_inside)
                    assert secteur_angle < pi/4, "secteur_angle should be < 90deg"

                    area_courbure = self.get_area_courbure(secteur_angle)


                    x_intersec_t = self.get_other_coord_on_circle(y_t)
                    y_intersec_r = self.get_other_coord_on_circle(x_r)


                    area_triangle_out = (x_r - x_intersec_t) * (y_t - y_intersec_r) / 2

                    to_add = area_courbure + area_gap - area_triangle_out
                    assert to_add > 0, "to_add should be >0"
                    
                    if _debug: print to_add
                    area_the_fly_can_go_float += to_add

                elif inside_t == (False, False, False, False):
                    #not at all in the circle
                    pass

                else:
                    assert False, "Missing case %s" % inside_t
                    
        area_the_fly_can_go = area_the_fly_can_go_float + area_the_fly_can_go_int
        return (area_racquet - area_the_fly_can_go) / area_racquet

    def get_other_coord_on_circle(self, coord):
        return sqrt(self.radius_inside **2 - coord**2)

    def get_area_courbure(self, secteur_angle):
        area_secteur_angle =       self.radius_inside**2 *secteur_angle / (2   )
        area_triangle_isocele = self.radius_inside**2 * sin(secteur_angle/2) * cos(secteur_angle/2)
        
        assert area_secteur_angle > area_triangle_isocele, "area_secteur_angle should be > area_triangle_isocele"

        return area_secteur_angle - area_triangle_isocele


    def is_inside(self, x, y):
        """ True if point is inside circle minus fly """

        if y == 0:
            d = x
        elif x == 0:
            d = y
        else:
            d = sqrt(x*x + y*y)

        return d < self.R - self.t - self.f


    def get_left_corners_l(self):
        f, R, t, r, g = self.f, self.R, self.t, self.r, self.g
        
        nb_corners_inside = 0
        x_corners_l = []
        
        finished = False
        while not finished:
            x_corner_bottom_left = self.get_x_corner_bottom_left(nb_corners_inside)
            
            if self.is_inside(x_corner_bottom_left, y=0):
                nb_corners_inside += 1
                x_corners_l.append(x_corner_bottom_left)

            else:
                finished = True
            
        return x_corners_l

    def get_x_corner_bottom_left(self, n):
        first = self.r + self.f
        period = self.g + 2 * self.r

        return first + n * period
        
    def get_x_corner_bottom_right(self, n):
        return self.get_x_corner_bottom_left() + self.g - 2* self.f

def do_multiply(in_str, nb_shift):
    """ return a integer value from a floating in a string, multiplied by a constant"""
    try:
        dec, frac = in_str.split(".")
        len_frac = len(frac)

        return int("%s%s" % (dec, frac)) * 10**(nb_shift - len_frac)
        
        if len_frac > max_figure_after_dot:
            max_figure_after_dot = len_frac
            
    except ValueError: # No frac part
        return int(in_str) * 10**nb_shift
 
def main(argv):

    f_out = open(argv[1].split(".")[0] + ".out", "w")

    fd = open(argv[1])
    nb_cases = int(fd.readline())


    for case_no in range(1, nb_cases+1):

        f_s, R_s, t_s, r_s, g_s = [item.strip() for item in fd.readline().split()]

        # Calculate number of figures after dot
        max_figure_after_dot = 0
        for item in f_s, R_s, t_s, r_s, g_s:
            try:
                dec, frac = item.split(".")
                len_frac = len(frac)
                if len_frac == 0: len_frac += 1
                
                if len_frac > max_figure_after_dot:
                    max_figure_after_dot = len_frac
            except ValueError: # No frac part
                pass

        f, R, t, r, g = [do_multiply(item, max_figure_after_dot) for item in  [f_s, R_s, t_s, r_s, g_s]]

        # Have read all stuff for this case:
        f_out.write( "Case #%d: %.6f\n" % (case_no,
                                           solve_case(case_no, f, R, t, r, g).solve_it()
                                           )
                     )
        f_out.flush()


    

import sys
if __name__ == "__main__":
    main(sys.argv)
