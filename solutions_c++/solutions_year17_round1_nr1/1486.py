
#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <set>
#include <unordered_set>
#include <queue>
#include <cstdio>
#include <queue>
#include <stack>
#include <unordered_map>
#include <sstream>

#include <stdio.h>      /* printf, scanf, NULL */
#include <stdlib.h>

using namespace std;

void cake(vector<string>& vec, int r, int c) {
    unordered_map<char, vector<int>> mp;
    // implement map of four edge for each initial
    // vector<int> = {up, down, left, right};
    for (int i = 0; i < r; ++i) for (int j = 0; j < c; ++j) {
        if (vec[i][j] != '?') {
            if (!mp.count(vec[i][j])) {
                mp[vec[i][j]] = {i, i, j, j};
            }
            else {
                mp[vec[i][j]][0] = min(mp[vec[i][j]][0], i);
                mp[vec[i][j]][1] = max(mp[vec[i][j]][1], i);
                mp[vec[i][j]][2] = min(mp[vec[i][j]][2], j);
                mp[vec[i][j]][3] = max(mp[vec[i][j]][3], j);
            }
        }
    }

    for (auto m : mp) {
        for (int i = m.second[0]; i <= m.second[1]; ++i)
        for (int j = m.second[2]; j <= m.second[3]; ++j) {
            vec[i][j] = m.first;
        }
    }

    for (int i = 0; i < r; ++i) for (int j = 0; j < c; ++j) {
        if (vec[i][j] == '?') {
            if (j == 0) {
                int k = 1;
                while (k < c && vec[i][k] == '?') ++k;
                if (k == c) continue;
                for (int m = j; m < k; ++m) vec[i][m] = vec[i][k];
            }
            if (j > 0 && vec[i][j-1] != '?') vec[i][j] = vec[i][j-1];
        }
    }

    for (int j = 0; j < c; ++j) for (int i = 0; i < r; ++i){
        if (vec[i][j] == '?') {
            if (i == 0) {
                int k = 1;
                while (k < r && vec[k][j] == '?') ++k;
                if (k == r) continue;
                for (int m = i; m < k; ++m) vec[m][j] = vec[k][j];
            }
            if (i > 0 && vec[i-1][j] != '?') vec[i][j] = vec[i-1][j];
        }
    }
}


int main(){
    // vector<string> vec = {"G??", "?C?", "??J"};
    // cake(vec, 3, 3);

    int n; cin >> n;
    
    for (int i = 1; i <= n; ++i) {
        int r, c; cin >> r >> c;
        vector<string> vec;
        string temp;
        for (int j = 0; j < r; ++j) {
            cin >> temp;
            vec.push_back(temp);
        }
        
        cout << "Case #" << i << ": " << endl;
        cake(vec, r, c);
        for (string s : vec) cout << s << endl;
    }
    
    return 0;
}