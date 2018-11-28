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

//"C-small-1-attempt2.in"
#define INP_FILE "C-large.in"
#define OUT_FILE "output.txt"

void solve1(ll n, ll k, ll &l, ll &r)
{
    while (k > 1) {
        k /= 2;
        n = (n - 1) / 2;
    }
    l = n / 2; r = n - l - 1;
}

void cut(ll n, ll &l, ll &r) {
    l = n / 2; r = n - l - 1;
}
void solve2(ll n, ll k, ll &l, ll &r)
{
    ll c, s,cc,ss;
    c = 1; s = 0;
    while (k>c+s && n>1) {
        if (s) cut(n - 1, l, r); else cut(n, l, r);
        k -= (c+s);
        if (n % 2) {
            cc = 2*c + s;
            ss = s;
        } else {
            cc = c ;
            ss = c + 2*s;
        }
        n /= 2;
        c = cc;
        s = ss;
    }
    if (k) {
        if (n == 1) l = r = 0; else
        if (k > c && n>1) cut(n - 1, l, r); else cut(n, l, r);
    }
}

void solve3(ll n, ll k, ll &l, ll &r) {
    vi a(n + 2, 0);
    a[0] = a[n + 1] = 1;
    fi(it, 0, k) {
        int mx=-1, mn = -1,best=-1;
        fie(i, 1, n) if (a[i] == 0) {
            int tl = i - 1; while (a[tl] == 0) --tl; ++tl;
            int tr = i + 1; while (a[tr] == 0) ++tr; --tr;
            int cmn = min(i - tl, tr - i);
            int cmx = max(i - tl, tr - i);
            if (mn < cmn || (mn == cmn && mx < cmx)) {
                mn = cmn;
                mx = cmx;
                best = i;
            }
        }
        a[best] = 1;
        l = mx; r = mn;

    }
}


void solve4(ll n, ll k, ll &l, ll &r) {
    priority_queue<ll> q;
    q.push(n);
    fi(it, 0, k) {
        n = q.top(); q.pop();
        cut(n, l, r);
        q.push(l);
        q.push(r);
    }
}

int main()
{
    freopen(INP_FILE, "r", stdin);
    freopen(OUT_FILE, "w", stdout);
    
    /*fie(n, 1, 100) {
        fie(k, 1, n) {
            ll l1, l2, r1, r2;
            //solve2(5, 3, l2, r2);
            solve4(n, k, l1, r1);
            solve2(n, k, l2, r2);
            if (l1 != l2 || r1 != r2) {
                printf("asdsad %d %d\n",n,k);
            }
        }
    }
    return 0;*/

    int tstCnt; scanf("%d", &tstCnt);
    for (int tst = 1; tst <= tstCnt; tst++)
    {
        ll n, k, l, r; scanf("%lld %lld", &n, &k);

        /*ll l1, l2, r1, r2;
        solve2(500, 233, l1, r1);
        solve4(n, k, l1, r1);
        solve3(n, k, l2, r2);
        if (l1 != l2 || r1 != r2) {
            printf("asdsad");
        }*/
        solve2(n, k, l, r);
        printf("Case #%d: %lld %lld\n", tst, l, r);
    }

    return 0;
}