// ███▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓▓▓╬╬╬╬╬╬▓█
// ███▓███████▓▓╬╬╬╬╬╬╬╬╬╬╬╬▓███▓▓▓▓█▓╬╬╬▓█
// ███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█
// ████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
// ███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
// ████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
// ███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█
// ████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
// ███▓▓▓▓▓▓▓╬╬▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
// ████▓▓▓╬╬╬╬▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
// ███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
// █████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
// █████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
// █████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
// ████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
// ████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
// █████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██
// █████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
// ██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███
// ███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
// ███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████
// ████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
// █████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████
// ██████████▓▓▓█▓▓▓╬▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
// ███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████
// ██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
// ███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████
//#include "grader.h"
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <numeric>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <list>
#include <cmath>
#include <bitset>
#include <cassert>
#include <queue>
#include <deque>
#include <cassert>
#define For(i, a, b) for (int i = a; i < b; ++i)
#define Out(i, a, b) for (int i = a - 1; i >= b; --i)
#define pb push_back
#define x first
#define y second
#define files(FileName) read(FileName); write(FileName)
#define read(FileName) freopen((FileName + ".in").c_str(), "r", stdin)
#define write(FileName) freopen((FileName + ".out").c_str(), "w", stdout)
using namespace std;
template<typename T1, typename T2>inline void chkmin(T1 &x, T2 y) { if (x > y) x = y; }
template<typename T1, typename T2>inline void chkmax(T1 &x, T2 y) { if (x < y) x = y; }

using namespace std;

typedef long double base;
typedef pair <long double, long double> point;

const string FILENAME = "input";
const int MAXN = 1e6 + 1, p = 1e9 + 7, d = 720;
const base Pi = acos(-1);

int n, m, t;
int cnt[2];
set <pair <int, pair <int, int>>> que[2];
int clr[d * 2 + 1][4];

void test(int num) {
    cin >> n >> m;
    cnt[0] = cnt[1] = d;
    for (int i = 0; i <= d * 2; ++i) {
        clr[i][0] = 0;
    }
    for (int i = 0; i < n; ++i) {
        int L, R;
        cin >> L >> R;
        for (int j = L; j < R; ++j) {
            clr[j][0] = 1;
        }
    }
    for (int i = 0; i < m; ++i) {
        int L, R;
        cin >> L >> R;
        for (int j = L; j < R; ++j) {
            clr[j][0] = 2;
        }
    }
    for (int i = 0; i <= d * 2; ++i) {
        clr[i][3] = clr[i][2] = clr[i][1] = clr[i][0];
    }
    if (clr[0][0] == 0) {
        clr[0][0] = 1;
        clr[0][1] = 1;
        clr[0][2] = 2;
        clr[0][3] = 2;
    } 
    int l = d * 2 - 1;
    if (clr[l][0] == 0) {
        clr[l][0] = 1;
        clr[l][1] = 2;
        clr[l][2] = 2;
        clr[l][3] = 1;
    } 
    int ans = d * 2 + 1;
    for (int t = 0; t < 4; ++t) {
        que[0].clear();
        que[1].clear();
        cnt[0] = cnt[1] = d;
        for (int L = 0; L < d * 2; ++L) {
            if (clr[L][t] == 0) continue;
            --cnt[clr[L][t] - 1];
            if (L == 0 || clr[L - 1][t] != clr[L][t]) {
                int R = L, res = 0, M1, M2;
                while ((R < d * 2) && (clr[R][t] == 0 || (res == 0 && clr[R][t] == clr[L][t]))) {
                    if (clr[R][t] == 0) {
                        if (res == 0) {
                            M1 = R;
                        }
                        M2 = R + 1;
                        ++res;
                    }
                    ++R;
                }
                if (res && clr[R][t] == clr[L][t]) {
                    //cout << res << ' ' << M1 << ' ' << M2 << endl;
                    que[clr[L][t] - 1].insert({res, {M1, M2}});
                }
            }
        }
        if (cnt[0] < 0 || cnt[1] < 0) continue;
        for (int c = 0; c < 2; ++c) {
            while (que[c].size()) {
                auto v = *que[c].begin();
                que[c].erase(v);
                if (cnt[c] >= v.x) {
                    //cout << "OK" << endl;
                    cnt[c] -= v.x;  
                    assert((v.y.y - v.y.x) == v.x);
                    for (int j = v.y.x; j < v.y.y; ++j) {
                        clr[j][t] = c + 1;
                    }
                } 
            }
        }
        int lst = 0, res = 0;
        for (int i = 0; i < d * 2; ++i) {
            if (clr[i][t] == 0) {
                if (cnt[lst] == 0) {
                    clr[i][t] = (!lst) + 1;
                } else {
                    clr[i][t] = lst + 1;
                }
                --cnt[clr[i][t] - 1];
            } 
            lst = clr[i][t] - 1;
            if (i && clr[i - 1][t] != clr[i][t]) {
                ++res;
            }
            //cout << clr[i][t];
        }
        //cout << endl;
       // cout << res << endl;
      //  cout << endl << endl;
        chkmin(ans, res + (clr[0][t] != clr[l][t]));
        assert(cnt[0] == 0 && cnt[1] == 0);
    }
    cout << "Case #" << num + 1 << ":" << ' ' << ans << endl;
}

int main() {
    srand(time(0));
    files(FILENAME);
    ios::sync_with_stdio(0);
    cin >> t;
    for (int i = 0; i < t; ++i) {
        test(i);
    }   
}

