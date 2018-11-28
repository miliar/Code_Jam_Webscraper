#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <cmath>
#include <set>
#include <unordered_map>
#include <map>
#include <functional>
#include <iomanip>
#include <vector>
#include <utility>

using namespace std;

typedef long long ll;

const bool debug = false;

vector<vector<char>> b;
int r, c;


void solve (){


cin >> r >> c;
b = vector<vector<char>>(r, vector<char> (c));
int i, j;
for(i = 0; i < r; i++) {
    for(j = 0; j < c; j++) {
        cin >> b[i][j];
    }
}
int p, q;
for(i = 0; i < r; i++) {
    for(j = 0;j < c; j++) {
        if(b[i][j] != '?') {
            p = j - 1;
            while(p >= 0 && b[i][p] == '?') {
                b[i][p] = b[i][j];
                p--;
            }
            p = j + 1;
            while(p < c && b[i][p] == '?') {
                b[i][p] = b[i][j];
                p++;
            }

        }
    }
}
for(i = 0; i < r; i++) {
    if(b[i][0] == '?') {
        int p;
        for(p = i + 1; p < r; p++) {
            if(b[p][0] != '?') {
                break;
            }
        }
        if(p == r) {
            for(p = i - 1; p >= 0; p--) {
                if(b[p][0] != '?') {
                    break;
                }
            }
        }
        for(int j = 0; j < c; j++) {
            b[i][j] = b[p][j];
        }
    }
}
for(i = 0; i < r; i++) {
    for(j = 0; j < c; j++) {
        cout << b[i][j];
    }
    cout << '\n';
}

}

int main() {
   ios_base::sync_with_stdio(false);
   if(!debug) {
        freopen("large.in", "r", stdin);
        freopen("large.out", "w", stdout);
    }
    int t;
    cin >> t;
    int i;
    for(i = 1; i <= t; i++) {
        cout << "Case #" << i << ": " << '\n';
        solve();

        cerr << "Case " << i << '\n';
    }
    return 0;
}
