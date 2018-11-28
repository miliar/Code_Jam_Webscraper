#define _CRT_SECURE_NO_DEPRECATE
#define _CRT_SECURE_NO_WARINGS
#define _USE_MATH_DEFINES

#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;
typedef pair<int64, int64> pll;

const int INF = (int)(1e9 + 1337);
const int64 LINF = (int64)(4e18);
const double EPS = (double)(1e-11);
#define sq(x) ((x)*(x))
#define FAIL() ((*(int*)(0))++)

int64 f[20][10][2];
int d[20];
int sz;

int64 dyn(int pos, int last, int flag)
{
    if(pos == sz)
        return 1;
    if(f[pos][last][flag] != -1)
        return f[pos][last][flag];
    
    int64 res = 0;

    int lim = d[pos];
    if(flag)
        lim = 9;
    for(int i = last; i <= lim; i++)
    {
        int npos = pos + 1;
        int nlast = i;
        int nflag = flag;
        if(i < d[pos])
            nflag = 1;
        res += dyn(npos, nlast, nflag);
    }

    return f[pos][last][flag] = res;
}

int64 calc(int64 dd)
{
    memset(f, -1, sizeof f);
    sz = 0;
    while(dd)
    {
        d[sz] = dd % 10;
        dd /= 10;
        sz++;
    }
    reverse(d, d + sz);
    return dyn(0, 0, 0);
}

void solve()
{
    int64 n;
    cin >> n;
    int64 v = calc(n);
    int64 l = 1, r = n, res = n;
    while(l <= r)
    {
        int64 mid = (l + r) >> 1;
        if(calc(mid) == v)
        {
            res = mid;
            r = mid - 1;
        }
        else
            l = mid + 1;
    }
    cout << res;
}

int main()
{
    ios_base::sync_with_stdio(false); cin.tie(0);
    int ts;
    cin >> ts;
    for(int i = 1; i <= ts; i++)
    {
        cout << "Case #" << i << ": ";
        solve();
        cout << '\n';
    }
    return 0;
}
