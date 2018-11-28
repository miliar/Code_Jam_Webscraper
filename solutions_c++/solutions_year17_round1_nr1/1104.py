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

char a[30][30];

void solve()
{
    cout << "\n";
    int r, c;
    cin >> r >> c;
    for(int i = 0; i < r; i++)
    {
        string s;
        cin >> s;
        for(int k = 0; k < c; k++)
        {
            a[i][k] = s[k];
        }
    }
    
    for(int i = 0; i < r; i++)
    {
        for(int k = 0; k < c; k++)
        {
            if(a[i][k] == '?' && k)
            {
                a[i][k] = a[i][k - 1];
            }
        }
    }
    
    for(int i = 0; i < r; i++)
    {
        for(int k = c - 1; k >= 0; k--)
        {
            if(a[i][k] == '?' && k < c - 1)
            {
                a[i][k] = a[i][k + 1];
            }
        }
    }
    
    for(int i = 0; i < r; i++)
    {
        for(int k = 0; k < c; k++)
        {
            if(a[i][k] == '?' && i)
            {
                a[i][k] = a[i - 1][k];
            }
        }
    }
    
    for(int i = r - 1; i >= 0; i--)
    {
        for(int k = 0; k < c; k++)
        {
            if(a[i][k] == '?' && i < r - 1)
            {
                a[i][k] = a[i + 1][k];
            }
        }
    }
    
    for(int i = 0; i < r; i++)
    {
        for(int k = 0; k < c; k++)
        {
            cout << a[i][k];
        }
        if(i < r - 1)
        {
            cout << "\n";
        }
    }
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
