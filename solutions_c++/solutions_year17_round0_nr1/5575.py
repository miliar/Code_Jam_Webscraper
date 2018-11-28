#include <bits/stdc++.h>

using namespace std;

int main()
{
    ifstream cin("inn.in");
    ofstream cout("out.txt");
    int T;
    ios_base::sync_with_stdio(0);
    cin >> T;
    for (int t = 1; t <= T; t++){
        string s;
        cin >> s;
        int k;
        cin >> k;
        int ans = 0;
        for (int i = 0; i <= (int)s.size() - k; i++)
        if (s[i] == '-'){
            ans++;
            for (int j = i; j <= i + k - 1; j++)
                if (s[j] == '-')
                    s[j] = '+';
                else
                    s[j] = '-';
        }

        for (int i = 0; i < (int)s.size(); i++)
            if (s[i] == '-')
                ans = -1;
        if (ans == -1)
            cout << "Case #" << t << ": IMPOSSIBLE\n";
        else
            cout << "Case #" << t << ": " << ans << '\n';
    }
    return 0;
}
