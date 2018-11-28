#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int t,i,l,j,n;
    unsigned long long ans;
    string s;
    cin >> t;
    for (j = 1; j <= t; j++)
    {
        cin >> s;
        s = "0" + s;
        l = s.size();
        ans = 0;
        for (i = l-1; i > 0; i--)
          if (s[i] < s[i-1])
          {
              s[i] = '9';
              n = s[i-1] - '0' - 1;
              s[i-1] = n + '0';
          }
        for (i = 1; i < l; i++)
        {
              if (s[i] > s[i+1])
                  s[i+1] = s[i];
              ans = ans*10 + s[i]-'0';
        }
        cout << "Case #" << j << ": " << ans << "\n";
    }
    return 0;
}
