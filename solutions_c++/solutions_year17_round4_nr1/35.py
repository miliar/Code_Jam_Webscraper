#include <iostream>
#include <vector>
#include <map>

using namespace std;

int sol(map<vector<int>, int>& memo, vector<int> cnt, int sum, int n)
{
    if (n == 0)
    {
        return 0;
    }
    if (memo.find(cnt) == memo.end())
    {
        int base = (sum == 0);
        memo[cnt] = base;
        for (size_t i = 0; i < cnt.size(); ++i)
        {
            if (cnt[i] > 0)
            {
                cnt[i] --;
                int ans = base + sol(memo, cnt, (sum + i) % cnt.size(), n - 1);
                cnt[i] ++;
                if (ans > memo[cnt])
                {
                    memo[cnt] = ans;
                }
            }
        }
    }

    return memo[cnt];
}

int main()
{
    int T;

    cin >> T;
    for (int ct = 0; ct < T; ++ct)
    {
        int n, p;
        cin >> n >> p;
        vector<int> cnt(p);
        for (int i = 0; i < n; ++i)
        {
            int g;
            cin >> g;
            cnt[g % p] ++;
        }
        map<vector<int>, int> m;
        int ans = sol(m, cnt, 0, n);
        cout << "Case #" << (ct + 1) << ": " << ans << endl;
    }
    return 0;
}
