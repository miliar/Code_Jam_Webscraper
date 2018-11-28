#include <bits/stdc++.h>
using namespace std;
queue<int> q;
char s[1001];
int k, x, ans;
main()
{
    freopen("A-large.in","r",stdin);
    freopen("A_L.txt","w",stdout);
    int t; scanf("%d",&t);
    for(int it = 1;it <= t;it++)
    {
        scanf(" %s %d",s,&k);
        ans = 0;
        while(!q.empty()) q.pop();
        for(int i = 0; i != strlen(s);i++)
        {
            x = (s[i]=='+'?0:1);
            while(!q.empty() && q.front() + k <= i)
                q.pop();
            x += q.size();
            x %= 2;
            if(x == 1)
            {
                if(i <= strlen(s)-k)
                {
                    q.push(i);
                    ans++;
                }
                else ans = -1;
            }
        }
        if(ans == -1) printf("Case #%d: IMPOSSIBLE\n",it);
        else printf("Case #%d: %d\n",it,ans);
    }
}
