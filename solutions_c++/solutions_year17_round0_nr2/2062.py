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
#define max3(a, b, c) max((a), max((b), (c)))
#define max4(a, b, c, d) max(max((a), (b)), max((c), (d)))
#define min3(a, b, c) min((a), min((b), (c)))
#define min4(a, b, c, d) min(min((a), (b)), min((c), (d)))
#define isz(x) (int)(x).size()

typedef long long ll;
typedef long double ld;
typedef unsigned int ui;
typedef pair<int, int> pii;
typedef vector<int> vi;

/* <------------------------------------------------------------------------------------> */

vector<int> num, ans;
int n;

bool check(int d, int i)
{
    for (; i < n; ++i)
    {
        if (d < num[i]) return true;
        if (d > num[i]) return false;
    }
    return true;
}

void subsolve()
{
    num.clear();
    ans.clear();

    string s;
    cin >> s;

    for (char & c : s) num.pb(c - '0');
    n = isz(num);
    ans.resize(n);

    for (int i = 0, dw = 0; i < n; ++i)
        for (int j = 9; j >= dw; --j)
            if (check(j, i))
            {
                ans[i] = j;
                if (j < num[i])
                {
                    for (int k = i + 1; k < n; ++k)
                        ans[k] = 9;
                    i = n;
                }
                dw = j;
                break;
            }

    reverse(all(ans));
    while (!ans.empty() && !ans.back()) ans.pop_back();
    reverse(all(ans));
    for (int & i : ans) cout << i;
    cout << "\n";
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
        freopen("B-large.in", "r", stdin);
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
