#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int cnt = 0; cnt < t; cnt++){
        int k;
        string s;
        cin >> s >> k;
        int ct = 0;
        for (int i = 0; i + k <= s.size(); i++){
            if (s[i] != '+'){
                ct++;
                for (int j = 0; j < k; j++){
                    if (s[i + j] == '-') s[i + j] = '+';
                    else s[i + j] = '-';
                }
            }
        }
        bool b = true;
        for (int i = s.size() - k + 1; i < s.size(); i++){
            if (s[i] == '-'){
                b = false;
            }
        }
        cout << "Case #" << cnt + 1 << ": ";
        if (!b) cout << "Impossible\n";
        else cout << ct << "\n";
    }
    return 0;
}
