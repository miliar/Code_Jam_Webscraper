#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <cctype>
#include <numeric>
#include <queue>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <iterator>
#define FOR(i,s,e) for(int i=(s);i<(int)(e);i++)
#define FOE(i,s,e) for(int i=(s);i<=(int)(e);i++)
#define REP(i,n)   FOR(i,0,n)
#define ALL(x) (x).begin(), (x).end()
#define CLR(s) memset(s,0,sizeof(s))
#define PB push_back
#define ITER(v)      __typeof((v).begin())
#define FOREACH(i,v) for(ITER(v) i=(v).begin();i!=(v).end();i++)
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
#define x first
#define y second

const int N = 100;

int n, p;
int a[N];
int lo[N][N], hi[N][N];
bool used[N][N];

LL Ceil(LL up, LL dn) {
    return (up + dn - 1) / dn;
}

LL Floor(LL up, LL dn) {
    return up / dn;
}

int main() {
    int T; scanf("%d", &T); FOE(ca, 1, T) {
        scanf("%d%d", &n, &p);
        FOR(i, 0, n) scanf("%d", a + i);

        FOR(i, 0, n) FOR(j, 0, p) {
            int x; scanf("%d", &x);
            lo[i][j] = Ceil(10 * x, 11 * a[i]);
            hi[i][j] = Floor(10 * x, 9 * a[i]);
        }

        CLR(used);
        int ans = 0;

        FOE(s, 1, 1000000) {
            bool ok = true;
            while (ok) {
                vi v; 
                FOR(i, 0, n) {
                    ok = false;
                    FOR(j, 0, p) if (!used[i][j] && s >= lo[i][j] && s <= hi[i][j]) {
                        v.PB(j);
                        ok = true;
                        break;
                    }
                    if (!ok) break;
                }

                if (ok) {
                    ans += 1;
                    FOR(i, 0, n) {
                        used[i][v[i]] = true;
                    }
                } else {
                    break;
                }
            }
        }

        printf("Case #%d: %d\n", ca, ans);
    }
    return 0;
}
