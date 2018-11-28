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

const int N = 100;

int a[N];
vector<pair<int, int> > b[N];

pair<int, int> cal(int x, int y)
{
    long long r = x / (0.9 * y);
    while (9 * r * y > 10 * x) --r;
    while (9 * (r + 1) * y <= 10 * x) ++r;

    long long l = x / (1.1 * y);
    while (11 * l * y < 10 * x) ++l;
    while (11 * (l - 1) * y >= 10 * x) --l;

    if (l > r) return mp(-1, -1);
    return mp(l, r);
}

void work()
{
    int n, p, _max = 0;
    cin >> n >> p;
    for (int i = 1; i <= n; ++i)
        cin >> a[i];
    for (int i = 1; i <= n; ++i)
    {
        b[i].clear();
        vector<int> t;
        for (int j = 1; j <= p; ++j)
        {
            int x;
            cin >> x;
            t.pb(x);
        }
        sort(t.begin(), t.end());
        for (int j = 1; j <= p; ++j)
        {
            int x;
            x = t[j - 1];
            pair<int, int> y = cal(x, a[i]);
            if (y.x != -1)
            {
                b[i].pb(y);
                _max = max(_max, y.y);
            }
        }
        reverse(b[i].begin(), b[i].end());
    }
    int ans = 0;
    for (int i = 1; i <= _max; ++i)
    {
        bool ok = true;
        for (int j = 1; j <= n; ++j)
        {
            while (b[j].size() && b[j].back().y < i) b[j].pop_back();
            if (b[j].size() == 0)
            {
                cout << ans << endl;
                return;
            }
            if (b[j].back().x > i)
            {
                ok = false;
                break;
            }
        }
        if (ok)
        {
            ++ans;
            for (int j = 1; j <= n; ++j)
                b[j].pop_back();
            --i;
        }
    }
    cout << ans << endl;
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
