#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("/Users/KhalidRamadan/Desktop/input.txt", "r", stdin);
    freopen("/Users/KhalidRamadan/Desktop/output.txt", "w", stdout);
    int t;
    cin >> t;
    for(int T = 1; T <= t; T++)
    {
        string s;
        cin >> s;
        int k;
        cin >> k;
        int ans = 0;
        bool ok = 1;
        for(int i = 0; i < (int)s.size() && ok; i++)
        {
            if(s[i] == '+') continue;
            ans ++;
            if(i + k > (int)s.size()) ok = 0;
            for(int j = i; j < i + k && ok; j++)
            {
                if(s[j] == '+') s[j] = '-';
                else s[j] = '+';
            }
        }
        cout << "Case #" << T << ": ";
        if(ok)
            cout << ans << endl;
        else cout << "IMPOSSIBLE" << endl;
    }
}
