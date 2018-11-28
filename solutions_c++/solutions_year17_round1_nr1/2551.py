/*************************************************************************
	> File Name: a.cpp
	> Author: skt
	> Mail: sktsxy@gmail.com
	> Created Time: 2017年04月15日 星期六 08时55分47秒
 ************************************************************************/

#include <cstring>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <complex>
#include <cassert>
// #pragma comment(linker,"/STACK:102400000,102400000")
using namespace std;
#define LL long long
#define pb push_back
#define mp make_pair
#define x first
#define y second
template <typename T> inline void checkMax(T &a, T b) {a = a>b?a:b;}
template <typename T> inline void checkMin(T &a, T b) {a = a<b?a:b;}
typedef pair<int, int> PII;
typedef vector<int> vi;
const double PI = acos(-1.0);
const double eps = 1e-8;

#define MAXN 30

int T, Cas = 1, R, C;
char mat[MAXN][MAXN], ans[MAXN][MAXN];

vector < pair<int, int> > cpos[30];
pair<int, int> rpos[30];
int sum[MAXN][MAXN];

struct Node {
    char c;
    int minl, minr, maxl, maxr;

    Node() {}
    Node(char c, int minl, int minr, int maxl, int maxr) : c(c), minl(minl), minr(minr), maxl(maxl), maxr(maxr) {}
};

vector < Node > cv;

int calc(int x1, int y1, int x2, int y2) {
    return sum[x2][y2] + sum[x1 - 1][y1 - 1] - sum[x2][y1 - 1] - sum[x1 - 1][y2];
}

void init() {
    memset(sum, 0, sizeof(sum));
    for (int i = 1; i <= R; i ++) {
        for (int j = 1; j <= C; j ++) {
            sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + (mat[i][j] != '?');
        }
    }
}

void gao() {
    for (int i = 0; i < cv.size(); i ++) {
            int LX = cv[i].minl, LY = cv[i].minr;
            int RX = cv[i].maxl, RY = cv[i].maxr;
            int count = (RX - LX + 1) * (RY - LY + 1);
            for (int j = 1; j < LX; j ++) {
                if (calc(j, LY, RX, RY) == count) {
                    cv[i].minl = j;
                    break;
                }
            }
            for (int x1 = cv[i].minl; x1 <= cv[i].maxl; x1 ++) {
                for (int x2 = cv[i].minr; x2 <= cv[i].maxr; x2 ++) {
                    mat[x1][x2] = cv[i].c;
                }
            }
        }
        init();

        for (int i = 0; i < cv.size(); i ++) {
            int LX = cv[i].minl, LY = cv[i].minr;
            int RX = cv[i].maxl, RY = cv[i].maxr;
            int count = (RX - LX + 1) * (RY - LY + 1);
            for (int j = R; j > RX; j --) {
                if (calc(LX, LY, j, RY) == count) {
                    cv[i].maxl = j;
                    break;
                }
            }
            for (int x1 = cv[i].minl; x1 <= cv[i].maxl; x1 ++) {
                for (int x2 = cv[i].minr; x2 <= cv[i].maxr; x2 ++) {
                    mat[x1][x2] = cv[i].c;
                }
            }
        }
        init();

        for (int i = 0; i < cv.size(); i ++) {
            int LX = cv[i].minl, LY = cv[i].minr;
            int RX = cv[i].maxl, RY = cv[i].maxr;
            int count = (RX - LX + 1) * (RY - LY + 1);
            for (int j = C; j > RY; j --) {
                if (calc(LX, LY, RX, j) == count) {
                    cv[i].maxr = j;
                    break;
                }
            }
            for (int x1 = cv[i].minl; x1 <= cv[i].maxl; x1 ++) {
                for (int x2 = cv[i].minr; x2 <= cv[i].maxr; x2 ++) {
                    mat[x1][x2] = cv[i].c;
                }
            }
        }
        init();

        for (int i = 0; i < cv.size(); i ++) {
            int LX = cv[i].minl, LY = cv[i].minr;
            int RX = cv[i].maxl, RY = cv[i].maxr;
            int count = (RX - LX + 1) * (RY - LY + 1);
            for (int j = 1; j < LY; j ++) {
                if (calc(LX, j, RX, RY) == count) {
                    cv[i].minr = j;
                    break;
                }
            }
            for (int x1 = cv[i].minl; x1 <= cv[i].maxl; x1 ++) {
                for (int x2 = cv[i].minr; x2 <= cv[i].maxr; x2 ++) {
                    mat[x1][x2] = cv[i].c;
                }
            }
        }
        init();
}

void work() {
    memset(mat, 0, sizeof(mat));
    cv.clear();
    memset(sum, 0, sizeof (sum));
    for (int i = 0; i < 30; i ++) cpos[i].clear();
    for (int i = 0; i < 30; i ++) rpos[i] = make_pair(0, 0);
    printf("Case #%d:\n", Cas ++);
    scanf("%d %d", &R, &C);
    for (int i = 1; i <= R; i ++) {
        scanf("%s", mat[i] + 1);
        for (int j = 1; j <= C; j ++) {
            if (mat[i][j] != '?') {
                cpos[mat[i][j] - 'A'].push_back(make_pair(i, j));
            }
        }
    }
    for (int i = 0; i < 26; i ++) {
        int minl = R + 1, maxl = 0, minr = C + 1, maxr = 0;
        for (int j = 0; j < cpos[i].size(); j ++) {
            minl = min(cpos[i][j].first, minl);
            maxl = max(cpos[i][j].first, minl);
            minr = min(cpos[i][j].second, minr);
            maxr = max(cpos[i][j].second, maxr);
        }
        if (maxl) {
            cv.push_back(Node('A' + i, minl, minr, maxl, maxr));
        }
        for (int j = minl; j <= maxl; j ++) {
            for (int k = minr; k <= maxr; k ++) {
                mat[j][k] = 'A' + i;
            }
        }
    }
    init();

    if (sum[R][C] == 0) {
        for (int i = 1; i <= R; i ++) {
            for (int j = 1; j <= C; j ++) {
                mat[i][j] = 'A';
            }
        }
    } else {
        while (sum[R][C] != R * C) {
            
            gao();
        }   
    }
    for (int i = 1; i <= R; i ++) {
        printf("%s\n", mat[i] + 1);
    }
}
int main() {
    scanf("%d", &T);
    while (T --) {
        work();
    }
    return 0;
}
