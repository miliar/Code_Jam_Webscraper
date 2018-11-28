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

map<ll, ll> d;
map<ll, ll> f;

void solve()
{
    f.clear();
    d.clear();
    ll n, k;
    cin >> n >> k;
    
    d[n] = 1;
    f[-n] = 1;
    map<ll, ll>::reverse_iterator it;
    
    while(!d.empty())
    {
        it = d.rbegin();
        n = it->first;
        ll l, r;
        r = n / 2;
        l = n / 2 - !(n & 1);
        if(l > 0) {d[l] += d[n]; f[-l] += d[n];}
        if(r > 0) {d[r] += d[n]; f[-r] += d[n];}
        d.erase(n);
    }
    
    for(map<ll, ll>::iterator it = f.begin(); it != f.end(); it++)
    {
        //cout << abs(it->first) << " " << it->second << "\n"; continue;
        if(k - it->second <= 0)
        {
            ll t = abs(it->first);
            cout << t / 2 << " " << t / 2 - !(t & 1);
            return;
        }
        k -= it->second;
    }
}

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(0), cout.tie(0);
    //freopen(FILE ".in", "r", stdin);freopen(FILE ".out", "w", stdout);
    freopen("C-large.in", "r", stdin);freopen("output.txt", "w", stdout);
    
    int t;
    cin >> t;
    for(int c = 1; c <= t; c++)
    {
        cout << "Case #" << c << ": ";
        solve();
        cout << "\n";
    }
    return 0;
}
