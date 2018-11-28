#include <cmath>
#include <cassert>
#include <vector>
#include <set>
#include <string>
#include <queue>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cassert>
//#include <functional>

using namespace std;
#define MP make_pair
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;


string dat[25];
int r, c;
void solve() {
    vector<int> posts;
    for (int i = 0; i < r; i++) {
        int j = 0;
        int prev = 0;
        int post = 0;
        bool flag = false;
        for (j = 0; j < c; j++) {
            if (dat[i][j] != '?') {
                flag = true;
                for (int k = prev; k < j; k++) {
                    dat[i][k] = dat[i][j];
                }
                prev = j+1;
                post = j;
            }
        }
        if (flag) {
            for (int k = post+1; k < c; k++) {
                dat[i][k] = dat[i][post];
            }
            posts.push_back(i);
        }
    }
    int idx = 0;
    for (int i = 0; i < posts[0]; i++) {
        dat[i] = dat[posts[idx]];
    }
    for (int i = posts[posts.size()-1]+1; i < r; i++) {
        dat[i] = dat[posts[posts.size()-1]];
    }
    for (int i = 0; i < posts.size()-1; i++) {
        for (int j = posts[i]+1; j<posts[i+1]; j++) {
            dat[j] = dat[posts[i]];
        }
    }
    for (int i = 0; i < r; i++) {
        cout << dat[i] << endl;
    }
}

int main () {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cin >> r >> c;
        for (int j = 0; j < r; j++) {
            cin >> dat[j];
 //           cout << dat[j] << endl;
        }
        printf("Case #%d:\n", i);
        solve();
//        cout << endl;
    }
}
