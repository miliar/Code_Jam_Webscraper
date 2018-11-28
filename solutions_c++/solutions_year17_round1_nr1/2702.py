// A C program to implement Ukkonen's Suffix Tree Construction
// Here we build generalized suffix tree for two strings
// And then we find longest common substring of the two input strings
#include <stdio.h>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <iostream>
#include <string.h>
#include <string>
#include <stdlib.h>
#include <vector>
#include <cmath>
using namespace std;

typedef long long ll;
#define MAXN 30

ll n, m, t;


int main()
{
    cin >> t;
    for (int cse = 1; cse <= t; cse++){
        cin >> n >> m;
        char grid[MAXN][MAXN];
        bool allq[MAXN];
        memset(grid, '.', sizeof(grid));
        memset(allq, true, sizeof(allq));
        cout << "Case #" << cse << ":" << endl;
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                cin >> grid[i][j];
                if (grid[i][j] != '?') allq[i] = false;
            }
            if (!allq[i]){
                int j = 0;
                for (j = 0; j < m; j++){
                    if (grid[i][j] != '?'){
                        break;
                    }
                }
                for (int k = 0; k < j; k++){
                    grid[i][k] = grid[i][j];
                }
                for (int k = j+1; k < m; k++){
                    if (grid[i][k] == '?'){
                        grid[i][k] = grid[i][k-1];
                    }
                }
            }
        }
        ll ind[MAXN];
        int j = 0;
        for (j = 0; j < n; j++){
            if(!allq[j]){
                break;
            }
        }
        for (int i = 0; i < j; i++){
            ind[i] = j;
        }
        for (int i = j; i < n; i++){
            if (allq[i]){
                ind[i] = ind[i-1];
            }
            else {
                ind[i] = i;
            }
        }
        
        for (int i = 0; i < n; i++){
            ll realind = ind[i];
            for (int j = 0; j < m; j++){
                grid[i][j] = grid[realind][j];
                cout << grid[i][j];
            }
            cout << endl;
        }
        
    }
    return 0;
}

