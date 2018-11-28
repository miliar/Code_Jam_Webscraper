#include <stdio.h>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <ctime>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <utility>

using namespace std;

#define pb push_back
#define ft first
#define sd second
#define mpr make_pair
#define all(x) begin((x)), end((x))
#define rall(x) (x).rbegin(), (x).rend()
#define forn(i, n) for (int (i) = 0; (i) < (n); ++(i))
#define isz(x) (int)(x).size()

typedef long long ll;
typedef long double ld;
typedef unsigned int ui;
typedef pair<int, int> pii;
typedef vector<int> vi;

/* <------------------------------------------------------------------------------------> */

string s;

void rev(int l, int k)
{
    for (int i = l; i < l + k; ++i)
        s[i] = (s[i] == '+' ? '-' : '+');
}

void subsolve()
{
    int n, k, ans = 0;
    cin >> s >> k;
    n = isz(s);

    for (int i = 0; i < n; ++i)
    {
        if (s[i] == '-')
        {
            if (i + k > n)
            {
                cout << "IMPOSSIBLE\n";
                return;
            }
            rev(i, k);
            ++ans;
        }
    }

    cout << ans << "\n";
}

void solve()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        cout << "Case #" << i << ": ";
        subsolve();
    }
}

/* <------------------------------------------------------------------------------------> */

 #define LOCAL
// #define FILE_NAME

int main()
{
    #if defined LOCAL
        freopen("A-large.in", "r", stdin);
        freopen("output.txt", "w", stdout);
    #elif defined FILE_NAME
        freopen(FILE_NAME".in", "r", stdin);
        freopen(FILE_NAME".out", "w", stdout);
    #endif

    ios_base::sync_with_stdio(0);
    cin.tie(0);

    solve();

    return 0;
}
