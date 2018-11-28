#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    //cout << t << endl;
    for(int q = 0; q < t; ++q)
    {
        string s;
        int k, otv = 0;
        bool f = true;
        cin >> s >> k;
        //cout << s << ' ' << k << '\n';
        for(int i = 0; i <= s.size() - k; ++i)
        {
            if(s[i] == '-')
            {
                otv++;
                for(int j = i; j < i + k; ++j)
                    if(s[j] == '-') s[j] = '+';
                    else s[j] = '-';
            }
        }
        cout << "Case #" << q+1 << ": ";
        for(int i = 0; i < s.size(); ++i)
            if(s[i] == '-')
            {
                cout << "IMPOSSIBLE\n";
                f = false;
                break;
            }
        if(f) cout << otv << '\n';
    }
}
