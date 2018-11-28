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

int n, p;
int a[110];
int ct[5];
int f[101][101][101][3];

int dyn(int r1, int r2, int r3, int ost)
{
    if(r1 == 0 && r2 == 0 && r3 == 0)
        return 0;
    if(r1 < 0 || r2 < 0 || r3 < 0)
        return 0;
    if(f[r1][r2][r3][ost] != -1)
        return f[r1][r2][r3][ost];

    int res = max(max(dyn(r1 - 1, r2, r3, (ost + 1) % p), dyn(r1, r2 - 1, r3, (ost + 2) % p)), 
            dyn(r1, r2, r3 - 1, (ost + 3) % p));
    res += !ost;

    return f[r1][r2][r3][ost] = res;
}

void solve()
{
    memset(ct, 0, sizeof ct);
    cin >> n >> p;
    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
        int r = p - (a[i] % p);
        if(r == p)
            r = 0;
        ct[r]++;
    }
    int ans = ct[0];
    memset(f, -1, sizeof f);
    //cout << ct[1] << ct[2] << ct[3] << endl;
    cout << ans + dyn(ct[1], ct[2], ct[3], 0);
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


