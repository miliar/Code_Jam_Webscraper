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

vector<int> v;

void solve()
{
    ll n;
    cin >> n;
    v.clear();
    while(n > 0)
    {
        v.pb(n % 10);
        n /= 10;
    }
    
    reverse(v.begin(), v.end());
    
    int m = (int) v.size();
    
    bool yes = true;
    while(yes)
    {
        yes = false;
        for(int i = 0; i < m - 1; i++)
        {
            if(v[i] > v[i + 1])
            {
                yes = true;
                v[i]--;
                i++;
                while(i < m)
                {
                    v[i++] = 9;
                }
                
            }
        }
    }
    
    yes = true;
    for(int i = 0; i < m; i++)
    {
        if(v[i] != 0)
        {
            yes = false;
        }
        if(!yes)
        {
            cout << v[i];
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(0), cout.tie(0);
    //freopen(FILE ".in", "r", stdin);freopen(FILE ".out", "w", stdout);
    freopen("B-large.in", "r", stdin);freopen("output.txt", "w", stdout);
    
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
