#include <bits/stdc++.h>
using namespace std;


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int cnt = 1; cnt <= t; cnt++)
    {
        char s[1005];
        int k;
        cin >> s >> k;
        int n = strlen(s), ans = 0;
        for(int i = 0; i + k <= n; i++)
            if(s[i] == '-')
            {
                for(int j = 0; j < k; j++)
                    s[i + j] = (s[i + j] == '-') ? '+' : '-';
                ans++;
            }
        int f = 0;
        for(int i = 0; i < n; i++)
            if(s[i] == '-')
                f |= 1;
        if(f)
            printf("Case #%d: IMPOSSIBLE\n", cnt);
        else
            printf("Case #%d: %d\n", cnt, ans);
    }
    return 0;
}