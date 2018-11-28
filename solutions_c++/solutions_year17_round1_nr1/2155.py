#include <cmath>
#include <cstdio>
#include <vector>
#include <set>
#include <list>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin>>T;
    for(int test_case = 0; test_case < T; test_case++) {
        cout<<"Case #"<<test_case+1<<":\n";
        int r,c;
        cin>>r>>c;
        vector<vector<char> > grid;
        for(int i = 0; i < r; i++) {
            vector<char> row;
            row.resize(c);
            for(int j = 0; j < c; j++) {
                cin>>row[j];
            }
            grid.push_back(row);
        }
        // Fill right
        for(int i = 0; i < r; i++) {
            char current_letter = NULL;
            for(int j = 0; j < c; j++) {
                if(grid[i][j] != '?') {
                    current_letter = grid[i][j];
                }
                if(grid[i][j] == '?' && current_letter != NULL) {
                    grid[i][j] = current_letter;
                }
            }
        }
        // Fill left
        for(int i = 0; i < r; i++) {
            char current_letter = NULL;
            for(int j = c-1; j >= 0; j--) {
                if(grid[i][j] != '?') {
                    current_letter = grid[i][j];
                }
                if(grid[i][j] == '?' && current_letter != NULL) {
                    grid[i][j] = current_letter;
                }
            }
        }
        // Fill empty rows
        for(int i = 0; i < r; i++) {
            bool all_empty = true;
            for(int j = 0; j < c; j++) {
                if(grid[i][j] != '?') {
                    all_empty = false;
                }
            }
            if(all_empty) {
                char fill_row = NULL;
                // Look down for non-empty row
                for(int j = i+1; j < r; j++) {
                    if(grid[j][0] != '?') {
                        // We can use this row
                        fill_row = j;
                        break;
                    }
                }
                if(fill_row == NULL) {          
                    // Look up for non-empty row
                    for(int j = i-1; j >= 0; j--) {
                        if(grid[j][0] != '?') {
                            // We can use this row
                            fill_row = j;
                            break;
                        }
                    }
                }
                for(int j = 0; j < c; j++) {
                    grid[i][j] = grid[fill_row][j];
                }
            }
        }
        // Output
        for(int i = 0; i < r; i++) {
            for(int j = 0; j < c; j++) {
                cout<<grid[i][j];
            }
            cout<<"\n";
        }
    }
    return 0;
}