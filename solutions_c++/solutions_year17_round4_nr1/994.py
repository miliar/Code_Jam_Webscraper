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

#define INP_FILE "A-large.in"
#define OUT_FILE "output.txt"

#define updiv(q,w) ((q)-(q)/(w))
int solve() {
    int n, p; cin >> n >> p;
    vi a;
    vi c(p, 0); fi(i, 0, n) { int t; cin >> t; t %= p; c[t]++; a.push_back(t); }
    if (p == 2) return c[0] + c[1] / 2 + c[1] % 2;
    if (p == 3) {
        int ans = c[0], t = abs(c[1] - c[2]);
        ans += min(c[1], c[2]) + t/3 +(t%3?1:0);
        return ans;
    }
    int ans = c[0] + c[2]/2 + min(c[1], c[3]), t = abs(c[1] - c[3]);
    if (c[2] % 2) {
        if (t > 1) { ++ans; t -= 2; }
        else { ++t; }
    }
    ans+= t/4 + (t % 4 ? 1 : 0);
    return ans;
}

int main()
{
    freopen(INP_FILE, "r", stdin);
    freopen(OUT_FILE, "w", stdout);
    int tstCnt; cin >> tstCnt;
    for (int tst = 1; tst <= tstCnt; tst++)
    {
        printf("Case #%d: %d\n",tst, solve());
    }

    return 0;
}