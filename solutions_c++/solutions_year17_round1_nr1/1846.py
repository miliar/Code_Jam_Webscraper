//
//  main.cpp
//  Project 1
//
//  Created by Jonny Kong on 8/14/16.
//  Copyright © 2016 Jonny Kong. All rights reserved.
//

#include <iostream>
#include <ostream>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <cmath>
#include <queue>
//#include <algorithm>

using namespace std;

#define cin infile
#define cout outfile

int isEmptyColumn(const vector<vector<char>> grid, int col) {
    bool isEmpty = 1;
    for(int i = 0; i < grid.size(); ++i) {
        if(grid[i][col] != '?') {
            isEmpty = 0;
            break;
        }
    }
    return isEmpty;
}

int main() {
    ifstream infile("/Users/Jonnykong/Downloads/A-large.in.txt", ios::in);
    ofstream outfile("/Users/Jonnykong/Downloads/results.txt", ios::out);
    
    int t; cin >> t;
    for(int z = 0; z < t; ++z) {
        int r, c; cin >> r >> c;
        vector<vector<char>> grid(r, vector<char>(c));
        for(int i = 0; i < r; ++i) {
            for(int j = 0; j < c; ++j) {
                cin >> grid[i][j];
            }
        }
        
        // Find the first unempty column
        for(int j = 0; j < c; ++j) {
            char current;
            bool occupied = 0;
            for(int i = 0; i < r; ++i) {
                if(grid[i][j] != '?') {
                    occupied = 1;
                    current = grid[i][j];
                }
                else if(occupied) {
                    grid[i][j] = current;
                }
            }
        }
        for(int j = c - 1; j >= 0; --j) {
            char current;
            bool occupied = 0;
            for(int i = r - 1; i >= 0; --i) {
                if(grid[i][j] != '?') {
                    occupied = 1;
                    current = grid[i][j];
                }
                else if(occupied) {
                    grid[i][j] = current;
                }
            }
        }
        // Move each row left or right
        for(int i = 1; i < c; ++i) {
            if(isEmptyColumn(grid, i)) {
                for(int j = 0; j < r; ++j) {
                    grid[j][i] = grid[j][i - 1];
                }
            }
        }
        for(int i = c - 2; i >= 0; --i) {
            if(isEmptyColumn(grid, i)) {
                for(int j = 0; j < r; ++j) {
                    grid[j][i] = grid[j][i + 1];
                }
            }
        }
        cout << "Case #" << z + 1 << ":" << endl;
        for(int i = 0; i < r; ++i) {
            for(int j = 0; j < c; ++j) {
                cout << grid[i][j];
            }
            cout << endl;
        }
    }
    return 0;
}










