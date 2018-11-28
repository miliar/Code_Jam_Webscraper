#include <type_traits>
#include <stdint.h>
#include <stdexcept>
#include <climits>
#include <ctime>
#include <chrono>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <vector>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

#include <unordered_set>
#include <unordered_map>

using namespace std;

int aa[100][100]; // both
int ar[100][100]; // rooks
int ab[100][100]; // bishops
int crx[100];
int cry[100];
int cb1[200];
int cb2[200];

/*
   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4
 0 x x x x x x x x
 1 x x x x x x x x .
 2 x x x x x x x x   .
 3 x x x x x x x x     .
 4 x x x x x x x x       .
 5 x x x x x x x x .       .
 6 x x x x x x x x . .       .
 7 x x x x x x x x . . . . . . . cb2
 8 . . ,       .
 9 . .       .
10 .       .
11 .     .
12 .   .
13 . .
14 . cb1

*/


int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, q; cin >> n >> q;
        for (int i = 0; i < 2*n; i++) {
            cb1[i] = cb2[i] = 0;
        }
        for (int y = 0; y < n; y++) {
            crx[y] = cry[y] = 0;
            for (int x = 0; x < n; x++) {
                aa[y][x] = 0, ar[y][x] = ab[y][x] = 0;
            }
        }
        int s = 0;
        for (int i = 0; i < q; i++) {
            string cc; cin >> cc; char t = cc[0];
            int y, x; cin >> y >> x; --y; --x; int fy = n-1-y;
            if (t == 'x' || t == 'o') { s++; aa[y][x] |= 1; cry[y]++; crx[x]++; }
            if (t == '+' || t == 'o') { s++; aa[y][x] |= 2; cb1[y+x]++; cb2[fy+x]++; }
        }
        if (true) { // place rooks
            int y = 0, x = 0;
            while (true) {
                while (y < n && cry[y]) y++;
                while (x < n && crx[x]) x++;
                if (y >= n || x >= n) break;
                s++; ar[y][x] |= 1; aa[y][x] |= 1; cry[y]++; crx[x]++;
            }
        }
        if (true) { // place bishops (try placing them on the edges)
            vector<pair<int, int>> vp;
            for (int i = 0; i < n; i++) {
                vp.push_back({0,i});
                vp.push_back({n-1,i});
                vp.push_back({i,0});
                vp.push_back({i,n-1});
            }
            for (auto p : vp) {
                int y = p.first, x = p.second; int fy = n-1-y;
                if (cb1[y+x] | cb2[fy+x]) continue;
                s++; ab[y][x] |= 2; aa[y][x] |= 2; cb1[y+x]++; cb2[fy+x]++;
            }
        }        
        char to_ch[4] {'.','x','+','o'};
        vector<string> vm;
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                if (ar[y][x] | ab[y][x]) {
                    stringstream ss; ss << to_ch[aa[y][x]] << " " << (y+1) << " " << (x+1);
                    vm.push_back(ss.str());
                }
            }
        }
        printf("Case #%d: %d %d\n", t, s, (int)vm.size());
        for (const auto& m : vm) printf("%s\n", m.c_str());
    }
    return 0;
}
