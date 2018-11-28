#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <queue>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <math.h>
#include <stack>
#include <deque>
#include <numeric>
#include <cstring>
#include <cstdio>
#include <list>
#include <cstdlib>
#include <bitset>
#include <ctime>

#define all(v) (v).begin(),(v).end()
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
const ld epsylon = 1e-9;

void solve() {
    int n;
    int r, y, b;
    scanf("%d %d 0 %d 0 %d 0", &n, &r, &y, &b);
    int A= max(r,max(y,b));
    char AC = (r>=y&&r>=b) ? 'R' : ((y>=r&&y>=b) ? 'Y' : 'B');
    char CC = (b<=y&&b<=r) ? 'B' : ((y<=r&&y<=b) ? 'Y' : 'R');
    char BC = (AC!='R'&&CC!='R') ? 'R' : ((AC!='Y'&&CC!='Y')?'Y':'B');
    int B= min(max(r,y),min(max(y,b),max(b,r)));
    int C=min(r,min(y,b));
    if (A-B > C) {
        printf("IMPOSSIBLE");
        return;
    }
    char res[1001];
    int i = 0;
    for (;;) {
        res[i++] = AC;A--;
        if (B > 0 && (A+1)==C && C > 0) {
            res[i++] = BC;B--;
            res[i++] = CC;C--;
        } else if (B > 0) {
            res[i++] = BC;B--;
        } else if (C > 0) {
            res[i++] = CC;C--;
        }
        if (i == n) {
            res[i] = '\0';
            break;
        }
        if (i > n || A < 0 || B < 0 || C < 0) {
            printf("WRONG!!!!!!!!!!!!");
            res[0]=0;
            break;
        }
    }
    printf("%s", res);
}

int main() {
    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/b.in", "r", stdin);
    freopen("/XCodeProjects/codejam2017/q-round/codejam-q/DerivedData/codejam-q/Build/Products/Debug/b.out", "w", stdout);

    int tests;
    scanf("%d\n", &tests);

    for (int test = 1; test <= tests; ++test) {

        printf("Case #%d: ", test);
        solve();
        printf("\n");
    }

    return 0;
}