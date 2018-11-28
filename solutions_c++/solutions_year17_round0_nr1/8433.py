/// This code is a pure govnocode
#include <bits/stdc++.h>
#define DEBUG(x) cout << #x << " = " << x << endl;
using namespace std;

int main()
{
    freopen("input_r.in", "r", stdin);
    freopen("output.out", "w", stdout);

    int T;
    cin >> T;

    for (int _t = 1; _t <= T; _t++)
    {
        string s;
        int K;
        int ans;

        cin >> s >> K;

        ans = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == '-')
            {
                if (i + K - 1 >= s.size())
                {
                    ans = -1;
                }
                else
                {
                    ans++;
                    for (int j = 0; j < K; j++)
                        s[i + j] = '+' + '-' - s[i + j];
                }
            }
        }

        if (ans != -1)
            cout << "Case #" << _t << ": " << ans << endl;
        else
            cout << "Case #" << _t << ": " << "IMPOSSIBLE" << endl;
    }

    return 0;
}
