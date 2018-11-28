#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <ctime>
#include <vector>
#include <queue>
#include <bitset>
#include <cmath>
#include <time.h>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <stdlib.h>
#include <deque>
#include <iomanip>
#include <complex>

using namespace std;

typedef long long ll;
typedef long double ld;

#define TIME (clock() * 1.0 / CLOCKS_PER_SEC)
#define rand_int ((rand() << 15) | rand())

const ld pi = 3.1415926535897932384626433832795;
const ld eps = 1e-8;
const ll prime = 239;
const ll MOD = 1e9 + 7;
const ll INF = 1e18;
const int BIG = 1e9 + 239;
const int MAX_N = 1e5 + 1;
const int MAX_T = (1 << 18);
const int MAX_LOG = 19;
const int dx[4] = {0, -1, 0, 1};
const int dy[4] = {-1, 0, 1, 0};

void solve()
{
    ll n;
    cin >> n;
    if (n < 10)
    {
        cout << n;
        return;
    }
    ll len = 0;
    ll k = n;
    vector<ll> d;
    while (k)
    {
        d.push_back(k % 10);
        k /= 10LL;
    }
    len = d.size();
    ll ans = 0;
    for (int i = 0; i < len - 1; i++)
        ans = 10LL * ans + 9;
    reverse(d.begin(), d.end());
    bool ch = true;
    for (int i = 0; i < len - 1; i++)
        ch &= (d[i] <= d[i + 1]);
    if (ch)
    {
        cout << n;
        return;
    }
    for (int i = 0; i < len; i++)
    {
        if (i == 0 && d[i] == 1)
            continue;
        if (d[i] == 0)
            continue;
        vector<ll> a = d;
        a[i]--;
        for (int j = i + 1; j < len; j++)
            a[j] = 9;
        bool ch = true;
        for (int j = 0; j < len - 1; j++)
            ch &= (a[j] <= a[j + 1]);
        if (ch)
        {
            ll now = 0;
            for (int j = 0; j < len; j++)
                now = 10 * now + a[j];
            ans = max(ans, now);
        }
    }
    cout << ans;
}

int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("small_input.txt", "r", stdin);
    //freopen("small_output.txt", "w", stdout);
    cin.sync_with_stdio(0);
    int number_of_tests;
    cin >> number_of_tests;
    for (int z = 0; z < number_of_tests; z++)
    {
        cout << "Case #" << z + 1 << ": ";
        solve();
        cout << "\n";
    }
    return 0;
}
