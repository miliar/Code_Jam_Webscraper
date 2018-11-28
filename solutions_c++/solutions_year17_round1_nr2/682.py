#include <bits/stdc++.h>
using namespace std;
const int MAXN = 55;
int n, m;
int a[MAXN], food[MAXN][MAXN], tmp[MAXN];

inline bool check(int cnt, int now, int j)
{
    return cnt * a[j] * 9 <= now * 10 && cnt * a[j] * 11 >= now * 10;
}

inline bool check(int cnt)
{
    vector<pair<int, int> > v;
    for (int i = 2; i <= n; i++)
    {
        bool haveans = false;
        for (int j = 1; j <= m && !haveans; j++)
            if (check(cnt, food[i][j], i))
            {
                v.push_back(pair<int, int>(i, j));
                haveans = true;
            }
        if (!haveans)
            return false;
    }
    for (unsigned i = 0; i < v.size(); i++)
        food[v[i].first][v[i].second] = 0;
    return true;
}

int main()
{
    ios::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T ; cas++)
    {
        cout << "Case #" << cas << ": ";
        memset(tmp, 0, sizeof(tmp));
        cin >> n >> m;
        for (int i = 1; i <= n; i++)
            cin >> a[i];
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
                cin >> food[i][j];
            sort(food[i] + 1, food[i] + 1 + m);
        }
        int ans = 0;
        for (int i = 1; i <= m; i++)
        {
            int l = (10 * food[1][i] + 11 * a[1] - 1) / (11 * a[1]),
                r = (10 * food[1][i]) / (9 * a[1]);
            if (!l && !r)
                continue;
            for (int j = l; j <= r; j++) {
                if (check(j, food[1][i], 1) && check(j))
                {
                    ans++;
                    food[1][i] = 0;
                    break;
                }

            }
        }
        cout << ans << endl;
    }
    return 0;
}
