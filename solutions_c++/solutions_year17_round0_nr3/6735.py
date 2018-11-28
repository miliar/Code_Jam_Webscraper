//
//  main.cpp
//  BathroomStalls
//
//  Created by Hjalmar Basile on 08/04/2017.
//  Copyright © 2017 Hjalmar Basile. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


// insertion sort of the last element
void reorder(vector<int> &a) {
    long long hole = a.size() - 1;
    int last = a[hole];
    
    while(hole > 0) {
        if(a[hole - 1] > last) {
            a[hole] = a[hole - 1];
            hole--;
        } else {
            break;
        }
    }
    
    a[hole] = last;
}

int main() {
    
    int t;
    cin >> t;
    
    for(int t_i = 1; t_i <= t; t_i++) {
        cout << "Case #" << t_i << ": ";
        
        int n, k;
        cin >> n >> k;
        
        vector<int> spaces;
        spaces.push_back(n);
        
        int max_s;
        for(int j = 1; j < k ; j++) {
            max_s = spaces[spaces.size() - 1];
            spaces[spaces.size() - 1] = max_s / 2;
            reorder(spaces);
            
            spaces.push_back((max_s - 1) / 2);
            reorder(spaces);
        }
        
        cout << (spaces[spaces.size() - 1] / 2) << " " << (spaces[spaces.size() - 1] - 1) / 2 << endl;
    }
    
    return 0;
}
