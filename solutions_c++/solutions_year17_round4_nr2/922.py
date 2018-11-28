#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>
#include <utility>
using namespace std;

#define fi(i,a,b) for(int i=(a);i<(b); ++i)
#define fd(i,a,b) for(int i=(a);i>(b); --i)
#define fie(i,a,b) for(int i=(a);i<=(b); ++i)
#define fde(i,a,b) for(int i=(a);i>=(b); --i)
#define mp(a,b) make_pair(a,b)
#define pb(x) push_back(x)
#define all(x) x.begin(), x.end()
#define rall(s) (s).rbegin(),(s).rend()
#define C(u) memset((u),0,sizeof((u)))
#define x first
#define y second
#define inf 1000000000
typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi > vvi;
typedef pair<int, int> pii;

#define INP_FILE "B-small-attempt2.in"
#define OUT_FILE "output.txt"

int main()
{
    freopen(INP_FILE, "r", stdin);
    freopen(OUT_FILE, "w", stdout);
    int tstCnt; cin >> tstCnt;
    for (int tst = 1; tst <= tstCnt; tst++)
    {
        int n, c, m; cin >> n >> c >> m;
        vvi a(c, vi(n,0)); fi(i, 0, m) { 
            int q, w; cin >> q >> w; --q; --w; 
            a[w][q]++; 
        }
        //fi(i, 0, c) sort(all(a[i]));
        int ans = 0;
        int r0 = 0,r1=0;
        fi(i, 0, n - 1) {
            int t;
            int &x1 = a[1][i];
            r0 = max(r0, i + 1);
            while (x1 && r0 < n) {
                t = min(x1, a[0][r0]);  ans += t; x1 -= t; a[0][r0] -= t; if (a[0][r0] == 0) ++r0;
            }
        }
        fi(i, 0, n - 1) {
            int t;
            int &x0 = a[0][i];
            r1 = max(r1, i + 1);
            while (x0 && r1 < n) {
                t = min(x0, a[1][r1]);  ans += t; x0 -= t; a[1][r1] -= t; if (a[1][r1] == 0) ++r1;
            }
        }
        ans += a[0][0] + a[1][0]; int f0 = a[1][0], f1 = a[0][0], prom = 0;
        fi(i, 1, n) {
            int t = 0;
            int n0 = a[0][i];
            int n1 = a[1][i];
            t = min(f0, n0); n0 -= t; f0 -= t;
            t = min(f1, n1); n1 -= t; f1 -= t;
            t = min(n0, n1); prom += t; ans += t; n0 -= t; n1 -= t;
            ans += n0; f1 += n0;
            ans += n1; f0 += n1;
        }
        /*if (max(a[0][0]+ a[0][1], a[1][0] + a[1][1])!=ans) {
            cerr << "x";
        }*/
        printf("Case #%d: %d %d\n", tst, ans, prom);
    }

    return 0;
}