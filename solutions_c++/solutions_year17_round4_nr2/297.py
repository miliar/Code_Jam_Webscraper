#include <iostream>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <queue>
#include <cassert>
#include <map>
#include <set>
#include <ctime>
#include <iomanip>
#include <bitset>

using namespace std;

#define x first
#define y second
#define mp make_pair
#define pb push_back
#define sz(X) ((int)((X).size()))

const int N = 1005;
const int inf = 100000000;

int cnt_c[N], s[N];

void work()
{
    int n, c, m, ans1 = 0;
    cin >> n >> c >> m;
    for (int i = 1; i <= c; ++i)
        cnt_c[i] = 0;
    for (int i = 1; i <= n; ++i)
        s[i] = 0;
    while (m--)
    {
        int p, b;
        cin >> p >> b;
        ans1 = max(ans1, ++cnt_c[b]);
        ++s[p];
    }
    for (int i = 1; i <= n; ++i)
    {
        s[i] += s[i - 1];
        ans1 = max(ans1, (s[i] + i - 1) / i);
    }
    int ans2 = 0, last = 0;
    for (int i = n; i >= 1; --i)
    {
        int x = s[i] - s[i - 1];
        if (x > ans1) {
            x -= ans1;
            s[i - 1] += x;

            if (last < x)
                ans2 += x - last;
            last = x;
            last = x;
        }
    }
    cout << ans1 << ' ' << ans2 << endl;
}

int main()
{
    #ifdef LOCAL_TEST
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i)
    {
        cout << "Case #" << i << ": ";
        work();
    }

    return 0;
}
