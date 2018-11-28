#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

string s;

int main ()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, n, i, j, k;
    cin >> t;
    int cs=0;
    while (t--)
    {
        cs++;
        cin >> s;
        cin >> k;
        int ans=0, flag=0;
        for (i=0; i<s.size(); i++)
        {
            if (s[i]=='-')
            {
                if (i+k>s.size())
                {
                    flag=1;
                    printf("Case #%d: IMPOSSIBLE\n", cs);
                    break;
                }
                ans++;
                for (j=i; j<i+k; j++)
                {
                    if (s[j]=='+') s[j]='-';
                    else s[j]='+';
                }
            }
        }
        if (flag) continue;
        printf("Case #%d: %d\n", cs, ans);
    }
    return 0;
}
