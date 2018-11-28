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


void solve()
{
    int K;
    string s;
    cin >> s >> K;
    int n = (int) s.length();
    
    int res = 0;
    
    for(int i = 0; i < 10 * n; i++)
    {
        int j = -1;
        for(int k = 0; k <= n - K; k++)
        {
            if(s[k] == '-')
            {
                j = k;
                k = n;
            }
        }
        
        if(j != -1)
        {
            for(int k = j; k < j + K; k++)
            {
                if(s[k] == '-') s[k] = '+';
                else s[k] = '-';
            }
            res++;
        }
    }
    
    for(int i = 0; i < n; i++)
    {
        if(s[i] == '-')
        {
            cout << "IMPOSSIBLE";
            return;
        }
    }
    cout << res;
}

int main()
{
    ios_base::sync_with_stdio(false);cin.tie(0), cout.tie(0);
    //freopen(FILE ".in", "r", stdin);freopen(FILE ".out", "w", stdout);
    freopen("A-large.in", "r", stdin);freopen("output.txt", "w", stdout);
    
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
