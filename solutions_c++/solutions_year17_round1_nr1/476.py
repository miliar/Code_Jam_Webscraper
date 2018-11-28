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

char g[51][51], f[51][51];
int n, m;

void init() {
    scanf("%d%d", &n, &m);
    CC(g, 0); CC(f, 0);
    REP(i, n) scanf("%s", g[i]);
}

void solve() {
    REP(i, n) REP(j, m) {
        if (g[i][j] == '?' || ('A' <= f[i][j] && f[i][j] <= 'Z')) continue;
        f[i][j] = g[i][j];
        for (int k = j-1; k >= 0 && g[i][k] == '?'; k--) f[i][k] = g[i][j];
        for (int k = j+1; k < m && g[i][k] == '?'; k++) f[i][k] = g[i][j];
        
    }
    REP(i, n) if ('A' <= f[i][0] && f[i][0] <= 'Z') {
        for (int k = i-1; k >= 0 && !('A' <= f[k][0] && f[k][0] <= 'Z'); k--) REP(j, m) f[k][j] = f[i][j];
        for (int k = i+1; k < n && !('A' <= f[k][0] && f[k][0] <= 'Z'); k++) REP(j, m) f[k][j] = f[i][j];
    }
    REP(i, n) printf("%s\n", f[i]);
}

int main()
{
#ifdef DEBUG
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
#endif
    int T;
    scanf("%d", &T);
    FOR(i, T) {
        init();
        printf("Case #%d:\n", i);
        solve();
    }
	return 0;
}
