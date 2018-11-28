#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T;

    cin >> T;
    for (int ct = 0; ct < T; ++ct)
    {
        int n, c, m;
        cin >> n >> c >> m;
        vector<pair<int, int>> data;
        for (int i = 0; i < m; ++i)
        {
            int p, b;
            cin >> p >> b;
            p--;
            b--;
            data.push_back(make_pair(p, b));
        }
        int ans = 0;
        for (int i = 0; i < n; ++i)
        {
            int total = 0;
            vector<int> cnt(c);
            for (const auto& j : data)
            {
                if (j.first <= i)
                {
                    total++;
                    cnt[j.second]++;
                    ans = max(ans, cnt[j.second]);
                }
            }
            ans = max(ans, (total + i) / (i + 1));
        }
        int earth_mover = 0;
        for (int i = n - 1; i >= 0; --i)
        {
            int cnt = 0;
            for (const auto& j : data)
            {
                if (j.first == i)
                {
                    cnt++;
                }
            }
            if (cnt > ans)
            {
                earth_mover += cnt - ans;
            }
        }
        cout << "Case #" << (ct + 1) << ": " << ans << " " << earth_mover << endl;
    }
    return 0;
}
