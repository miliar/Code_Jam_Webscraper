#include <bits/stdc++.h>
using namespace std;
typedef long long ll;




int main()
{
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdin);
    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        string s;
        int k;
        cin >> s >> k;
        int ans = 0;
        for (int j = 0; j <= s.size() - k; j++) {
            if (s[j] == '-') {
                for (int ii = 0; ii < k; ii++) {
                    s[ii + j] = s[ii + j] == '-' ? '+' : '-';
                }
                ans++;
            }
        }
        cout << "Case #" << i << ": ";
        if (count(s.begin(), s.end(), '-'))
            cout << "IMPOSSIBLE";
        else
            cout << ans;
        cout << endl;
    }
}