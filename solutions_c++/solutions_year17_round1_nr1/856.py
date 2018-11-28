//
//  main.cpp
//  Dolphin
//
//  Created by Mahmud on 15/11/17.
//  Copyright © 2017 Mahmud. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <numeric>
#include <algorithm>
#include <functional>
#include <vector>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <utility>
#include <cassert>
#include <iomanip>
#include <ctime>
#include <sstream>
#include <istream>

using namespace std;

const int me = 125;

int T, R, C;
string grid[me];

int main(int argc, const char * argv[]) {
    //ios_base::sync_with_stdio(0);
    //cin.tie(0);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    cin >> T;
    for(int c = 0; c < T; c ++){
        cin >> R >> C;
        for(int i = 1; i <= R; i ++){
            cin >> grid[i];
            grid[i] = "$" + grid[i];
        }
        for(int i = 1; i <= R; i ++){
            for(int j = 1; j <= C; j ++){
                if(grid[i][j] != '?'){
                    for(int k = j - 1; k > 0; k --){
                        if(grid[i][k] != '?')
                            break;
                        grid[i][k] = grid[i][j];
                    }
                    for(int k = j + 1; k <= C; k ++){
                        if(grid[i][k] != '?')
                            break;
                        grid[i][k] = grid[i][j];
                    }
                }
            }
        }
        for(int i = 1; i <= R; i ++){
            for(int j = 1; j <= C; j ++){
                if(grid[i][j] != '?'){
                    for(int k = i - 1; k > 0; k --){
                        if(grid[k][j] != '?')
                            break;
                        grid[k][j] = grid[i][j];
                    }
                    for(int k = i + 1; k <= R; k ++){
                        if(grid[k][j] != '?')
                            break;
                        grid[k][j] = grid[i][j];
                    }
                }
            }
        }
        cout << "Case #" << c + 1 << ":" << endl;
        for(int i = 1; i <= R; i ++){
            for(int j = 1; j <= C; j ++)
                cout << grid[i][j];
            cout << endl;
        }
    }
    
    return 0;
}
