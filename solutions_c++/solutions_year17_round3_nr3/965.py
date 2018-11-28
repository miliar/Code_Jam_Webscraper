//
//  main.cpp
//  C
//
//  Created by Hjalmar Basile on 30/04/2017.
//  Copyright © 2017 Hjalmar Basile. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
    
    ifstream fin("/Users/hjalmar/Desktop/C/C/C-small-1-attempt0.in.txt");
    ofstream fout("/Users/hjalmar/Desktop/C/C/C-small-1-attempt0.out.txt");
    
    int t;
    fin >> t;
    
    for(int t_i = 1; t_i <= t; t_i++) {
        fout << "Case #" << t_i << ": ";
        
        int n, k;
        fin >> n >> k;
        
        double u;
        fin >> u;
        
        vector<double> p(n);
        for(int i = 0; i < n; i++) {
            fin >> p[i];
        }
        sort(p.begin(), p.end());
        p.push_back(1.0);
        
        for(int i = 1; i <= n; i++) {
            double diff = p[i] - p[i - 1];
            double cost = diff * ((double) i);
            if(u >= cost) {
                for(int j = 0; j < i; j++) {
                    p[j] = p[i];
                }
                u -= cost;
            } else {
                double add = u / i;
                for(int j = 0; j < i; j++) {
                    p[j] += add;
                }
                break;
            }
        }
        
        fout << fixed << setprecision(9);
        double prob = 1.0;
        for(int i = 0; i < n; i++) {
            prob *= p[i];
        }
        fout << prob << endl;
        
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
