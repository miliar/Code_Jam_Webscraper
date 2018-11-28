#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, k, n, ans;
    bool flag;
    scanf("%d", &t);
    string s;
    for(int qu = 1; qu <= t; qu++)
    {
        flag = 1;
        cin>>s;
        n = (int)s.length();
        ans = 0;
        scanf("%d", &k);

        for(int i = 0; i <= n - k; i++)
        {
            if(s[i] == '-')
            {
                ans++;
                for(int j = i; j <= i + k - 1; j++)
                {
                    if(s[j] == '-')
                        s[j] = '+';
                    else
                        s[j] = '-';
                }
            }
        }

        for(int i = n - k + 1; i < n; i++)
        {
            if(s[i] == '-')
            {
                flag = 0;
                break;
            }
        }

        if(!flag)
            printf("Case #%d: IMPOSSIBLE\n", qu);
        else
            printf("Case #%d: %d\n", qu, ans);
    }
    return 0;
}
