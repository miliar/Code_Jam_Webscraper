#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

ifstream input("/Users/dwang/Downloads/B-small-attempt0.in");

int N, R, O, Y, G, B, V;
int a[6][6];
int d[6];
char cmap[6];

void init() {
    memset(a, 0, sizeof(a));
    memset(d, 0, sizeof(d));
    cmap[0] = 'R';
    cmap[1] = 'B';
    cmap[2] = 'Y';
    cmap[3] = 'G';
    cmap[4] = 'O';
    cmap[5] = 'V';
    input >> N >> R >> O >> Y >> G >> B >> V;
}

void dfs(int k) {
    for (int i = 0; i < N; ++i) {
        printf("%c", cmap[k]);
        int c = 0;
        for (int j = 0; j < 6; ++j) {
            if (a[k][j] > 0) {
                if (a[k][c] == 0 || d[j] > d[c]) {
                    c = j;
                }
            }
        }
        d[k] -= 1;
        d[c] -= 1;
        a[k][c] -= 1;
        a[c][k] -= 1;
        k = c;
    }
}

void solve() {
    for (int i = 0; i <= R * 2; ++i) {
        int j = B * 2 - i;
        int t = Y * 2 - j;
        if (j >= 0 && t >= 0 && t + i == R * 2 && (i + j) % 2 == 0 && (j + t) % 2 == 0 && (i + t) % 2 == 0) {
            a[0][1] = i;
            a[1][0] = i;
            a[1][2] = j;
            a[2][1] = j;
            a[0][2] = t;
            a[2][0] = t;
            d[0] = i + t;
            d[1] = i + j;
            d[2] = t + j;
            if (d[0] > d[1] && d[0] > d[2]) {
                dfs(0);
            } else if (d[1] > d[2]) {
                dfs(1);
            } else {
                dfs(2);
            }
            return;
        }
    }
    printf("IMPOSSIBLE");
}

int main() {
    freopen("/Users/dwang/Documents/test/test/out.txt", "w", stdout);
    int T;
    
    input >> T;
    for (int i = 0; i < T; ++i) {
        init();
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }
    input.close();
    return 0;
}
