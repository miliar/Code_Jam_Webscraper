//
//  main.cpp
//  A
//
//  Created by Hjalmar Basile on 30/04/2017.
//  Copyright © 2017 Hjalmar Basile. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

class Pancake {
    public:
        double radius;
        double height;
    
    Pancake(double r, double h) {
        radius = r;
        height = h;
    }
    
    static bool mycompare(Pancake a, Pancake b) {
        return(a.radius * a.height > b.radius * b.height);
    }
};

int main() {
    
    ifstream fin("/Users/hjalmar/Desktop/A/A/A-large.in.txt");
    ofstream fout("/Users/hjalmar/Desktop/A/A/A-large.out.txt");
    
    int t;
    fin >> t;
    
    for(int t_i = 1; t_i <= t; t_i++) {
        fout << "Case #" << t_i << ": ";

        int n, k;
        fin >> n >> k;
        
        vector<Pancake> pancakes;
        for(int i = 0; i < n; i++) {
            double r_i, h_i;
            fin >> r_i >> h_i;
            
            Pancake p_i(r_i, h_i);
            pancakes.push_back(p_i);
        }
        sort(pancakes.begin(), pancakes.end(), Pancake::mycompare);
        
        fout << fixed << setprecision(9);
        
        double max_area = -1.0;
        for(int i = 0; i < n; i++) {
            double area = pancakes[i].radius * pancakes[i].radius;
            area += 2 * pancakes[i].radius * pancakes[i].height;
            int found = 1;
            if(k > 1) {
                for(int j = 0; j < n; j++) {
                    if(j != i) {
                        if(pancakes[j].radius <= pancakes[i].radius) {
                            area += 2 * pancakes[j].radius * pancakes[j].height;
                            found++;
                            if(found == k)
                                break;
                        }
                    }
                }
            }
            if(found == k && area > max_area)
                max_area = area;
        }
        fout << M_PI * max_area << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
