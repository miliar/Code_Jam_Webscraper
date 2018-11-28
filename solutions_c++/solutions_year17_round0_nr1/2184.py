#include <bits/stdc++.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
        cout << "Case #" << cas << ": ";
        string str;
        int n, len;
        cin >> str >> n;
        len = str.length();
        vector<bool> v;
        for (int i = 0; i < len; i++)
            v.push_back(str[i] == '+' ? true : false);

        int ans = 0;
        bool haveans = true;
        for (int i = 0; i < len && haveans; i++)
            if (!v[i] && i + n <= len)
            {
                for (int j = 0; j < n; j++)
                    v[i + j] = !v[i + j];
                ans++;
            }
            else if (!v[i])
                haveans = false;
        if (!haveans)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << ans << endl;
    }
    return 0;
}
