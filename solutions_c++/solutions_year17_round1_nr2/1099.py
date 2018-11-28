#include <iostream>
#include <iomanip>
#include <string>
#include <map>
#include <math.h>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <set>
#include <queue>
#include <sstream>
#include <deque>
#include <memory.h>
#include <cassert>
#include <ctime>
#include <time.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define pb push_back
#define mp make_pair
#define FILE "file"
#define lc v << 1
#define rc (v << 1) + 1
#define inf 1e+9
#define linf ll(1e+18)
#define classname SubtreeSumHash

ll b[2][10];

bool yes(ll f, ll x)
{
    for(ll r = f * 100 / (x * 110); r <= f * 100 / (90 * x) + 1; r++)
    {
        if(90 * r  * x <= 100 * f && 100 * f <= 110 * r * x)
        {
            return true;
        }
    }
    return false;
}

bool yes2(ll f, ll x, ll s, ll y)
{
    for(ll i = f * 100 / (x * 110); i <= f * 100 / (90 * x) + 1; i++)
    {
        //cout << i << " " << f << " " << s << " " << 90 * f << " " << x * i * 100 << " " << 110 * f << " " <<  90 * s << " " <<  y * i * 100 << " " << 110 * s << "\n";
        if(i && 90 * x * i <= f * 100 && f * 100 <= 110 * x * i && 90 * y * i  <= s * 100 && s * 100 <= 110 * y * i )
        {
            return true;
        }
    }
    return false;
}

void solve()
{
    int n, p;
    cin >> n >> p;
    
    vector<int> a;
    a.resize(p);
    
    int res = 1;
    for(int i = 1; i <= p; i++)
    {
        res *= i;
        a[i - 1] = i - 1;
    }
    
    if(n == 1)
    {
        ll x;
        cin >> x;
        int ans = 0;
        for(int i = 0; i < p; i++)
        {
            ll y;
            cin >> y;
            ans += yes(y, x);
        }
        cout << ans;
        return;
    }
    
    
    ll x, y;
    cin >> x >> y;
    
    for(int i = 0; i < n; i++)
    {
        for(int k = 0; k < p; k++)
        {
            cin >> b[i][k];
        }
    }
    
    int ans = 0;
    for(int i = 0; i < res; i++)
    {
        int temp = 0;
        for(int k = 0; k < p; k++)
        {
            ll f = b[0][k], s = b[1][a[k]];
            temp += yes2(f, x, s, y);
            //cout << f << " " << s << "\n";
        }
        //cout << "\n";
        ans = max(ans, temp);
        next_permutation(a.begin(), a.end());
    }
    cout << ans;
}

void gcj()
{
    int t;
    cin >> t;
    for(int i = 0; i < t; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << "\n";
    }
}

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(0), cout.tie(0);
    freopen(FILE ".in", "r", stdin);freopen(FILE ".out", "w", stdout);
    gcj();
    return 0;
}
