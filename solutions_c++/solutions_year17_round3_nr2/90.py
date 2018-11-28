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

int n[2];
vector<pii> a[2];
int u[24 * 60];
int f[24 * 60][24 * 60][2][2];

int dyn(int pos, int ct0, int fst, int pre)
{
    if(pos >= 24 * 60)
    {
        if(ct0 == 720)
            return (fst != pre);
        else
            return INF;
    }
    if(f[pos][ct0][fst][pre] != -1)
        return f[pos][ct0][fst][pre];

    int res = INF;
    for(int i = 0; i < 2; i++)
    {
        if(u[pos] == i)
            continue;
        int dt = (i != pre);
        if(pos == 0)
            dt = 0;
        int nct0 = ct0 + (i == 0);
        int npre = i;
        int npos = pos + 1;
        int nfst = fst;
        if(pos == 0)
            nfst = i;
        res = min(res, dyn(npos, nct0, nfst, npre) + dt);
    }

    return f[pos][ct0][fst][pre] = res;
}

void solve()
{
    memset(u, -1, sizeof u);
    memset(f, -1, sizeof f);
    cin >> n[0] >> n[1];

    for(int tt = 0; tt < 2; tt++)
    {
        a[tt].resize(n[tt]);
        for(int i = 0; i < n[tt]; i++)
        {
            cin >> a[tt][i].first >> a[tt][i].second;
            for(int j = a[tt][i].first; j < a[tt][i].second; j++)
                u[j] = tt;
        }
    }
    cout << dyn(0, 0, 0, 0);
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
}


