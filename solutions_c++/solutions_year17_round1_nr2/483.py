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

int n, p, r[51], c[51];

struct Q {
    int v;
    int l, r;
}q[51][51];

bool cmp(const Q & q1, const Q & q2) {
    return q1.v < q2.v;
}

void init() {
    CC(r, 0); CC(q, 0); CC(c, 0);
}

bool valid() {
    int a = 0, b = 10000000;
    REP(i, n) {
        if (q[i][c[i]].l > a) a=q[i][c[i]].l;
        if (q[i][c[i]].r < b) b=q[i][c[i]].r;
    }
    return a <= b;
}

int solve() {
    int ans = 0;

    REP(i, n) {
        sort(q[i], q[i]+p, cmp);
    }

    REP(i, n) REP(j, p) {
        q[i][j].l = int(ceil(q[i][j].v / 1.1 / r[i]));
        q[i][j].r = int(q[i][j].v / 0.9 / r[i]);
        //cout<<i<<" "<<j<<" "<<q[i][j].l<<" "<<q[i][j].r<<" "<<q[i][j].v<<endl;
    }
    
    while (true) {
        if (valid()) {
            ans++;
            REP(i, n) {
                c[i]++;
                if (c[i] >= p) return ans;
            }
        } else {
            int min_l = 0;
            REP(i, n) if (q[i][c[i]].l < q[min_l][c[min_l]].l) {
                min_l = i;
            }
            c[min_l]++;
            if (c[min_l] >= p) return ans;
        }
    }
    return ans;
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
        scanf("%d%d", &n, &p);
        REP(j, n) {
            scanf("%d", &r[j]);
        }
        REP(j, n) REP(k, p) {
            scanf("%d", &q[j][k].v);
        }
        printf("Case #%d: %d\n", i, solve());
    }
	return 0;
}
