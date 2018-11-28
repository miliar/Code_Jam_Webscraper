#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <sstream>

#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=n-1;i>=0;i--)
#define FOR(i,n) for(int i=1;i<=(n);i++)
#define FORD(i,n) for(int i=(n);i>=1;i--)

#define SZ(x) ((int)x.size())
#define CC(a,x) memset(a,x,sizeof(a))
#define TWO(x) ((LL)1<<(x))

#define DEBUG

using namespace std;

typedef long long LL;

int n, p;

int a[101];
int y[4];

void init() {
    scanf("%d%d", &n, &p);
    CC(y, 0);
    REP(i, n) {
        scanf("%d", &a[i]);
        y[a[i]%p]++;
    }
}
int solve() {
    int ans = y[0];
    if (p == 2) return y[0] + (y[1] % 2) + (y[1] / 2);
    if (p == 3) {
        int b = min(y[1], y[2]);
        ans += b;
        y[1] -= b;
        y[2] -= b;
        ans += y[1] / 3 + y[2] / 3 + (y[1] % 3 != 0 || y[2] % 3 != 0);
    }
    if (p == 4) {
        int b = min(y[1], y[3]);
        y[1] -= b;
        y[3] -= b;
        int c = min(y[2], y[3]/2);
        y[2] -= c;
        y[3] -= 2*c;
        int d = min(y[2], y[1]/2);
        y[2] -= d;
        y[1] -= 2*d;
        ans += b + c + d + (y[1] % 4 != 0 || y[2] % 2 != 0 || y[3] % 4 != 0) + y[1] / 4 + y[2] / 2 + y[3] / 4;
    }
    return ans;
}

int main()
{
#ifdef DEBUG
    freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
#endif
    int T;
    scanf("%d", &T);
    FOR(i, T) {
        init();
        printf("Case #%d: %d\n", i, solve());
    }
	return 0;
}
