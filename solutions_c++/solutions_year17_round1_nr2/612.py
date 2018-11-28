#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cmath>
using namespace std;
int T;
int n,p;
int main()
{
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
        cin >> n >> p;
        vector<int> r;
        vector<pair<int, int>> q[52];
        for (int i = 0; i < n; ++i)
        {
            int t;
            cin >> t;
            r.push_back(t);
        }
        for (int i = 0; i < n; sort(q[i].begin(), q[i].end()), ++i)
            for (int j = 0; j < p; ++j)
            {
                int t, sl, su;
                cin >> t;
                sl = ceil(1.0 * t / (r[i] * 1.1));
                su = floor(1.0 * t / (r[i] * 0.9));
                if (1.0 * t / (1.0 * r[i] * (sl-1)) < 1.1001 )
                    --sl;
                if (1.0 * t / (1.0 * r[i] * (su+1)) > 0.8999 )
                    ++su;
                q[i].push_back(pair<int,int>(sl,su));
            }
        int ans = 0;
        int pos[52] = {0};
        while (1)
        {
            bool end = false;
            int lower = -1, upper = 10000000;
            for (int i = 0; i < n; ++i)
                if (pos[i] >= q[i].size())
                {
                    end = true;
                    break;
                }
                else
                {
                    lower = max(lower, q[i][pos[i]].first);
                    upper = min(upper, q[i][pos[i]].second);
                }
            if (end)
                break;
            if (lower <= upper)
                ++ans;
            else
            {
                int endmin = 10000000, endpos = -1;
                for (int i = 0; i < n; ++i)
                    if (endmin > q[i][pos[i]].second)
                    {
                        endmin = q[i][pos[i]].second;
                        endpos = i;
                    }
                ++pos[endpos];
                continue;
            }
            if (end)
                break;
            for (int i = 0; i < n; ++i)
                ++pos[i];
        }
        cout << "Case #" << t << ": "  << ans << endl;
    }
    return 0;
}
