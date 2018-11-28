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
    string s;
    int k;
    cin >> s >> k;
    int n = s.size();
    int ans = 0;
    for (int i = 0; i <= n - k; i++)
    {
        if (s[i] == '+')
            continue;
        for (int j = i; j < i + k; j++)
            s[j] = (s[j] == '+' ? '-' : '+');
        ans++;
    }
    for (int i = 0; i < n; i++)
        if (s[i] != '+')
        {
            cout << "IMPOSSIBLE";
            return;
        }
    cout << ans;
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("small_output.txt", "w", stdout);
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
