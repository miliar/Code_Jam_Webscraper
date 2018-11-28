#include <bits/stdc++.h>
using namespace std;


int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int p=1; p<=t; p++)
    {
        bool flag = true;
        int k, ans=0;
        string s;
        cin >> s >> k;
        int i=0;
        while (i<s.length())
        {
            while ((i<s.length()) && (s[i] == '+'))
               i++;

            if (s.length()-i<k) break;
            for (int j=i; j<i+k; j++)
            {
                if (s[j] == '+') s[j] = '-'; else s[j] = '+';
            }
            i++;
            ans++;

        }
        for (int j=0; j<s.length(); j++)
            if (s[j] == '-') {cout << "Case #" << p << ": " << "IMPOSSIBLE" << endl; flag = false; break; }
            if (flag ) cout << "Case #" << p << ": " << ans << endl;
    }
}
