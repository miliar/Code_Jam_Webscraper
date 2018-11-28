#include<bits/stdc++.h>
using namespace std;


const int maxn = 1e5;

char s[maxn];
int A[maxn];
int k;

int solve()
{
    int res = 0;
    int len = strlen(s);
    for(int i = 0;i < len;++i)
        if(s[i] == '-')
        {
            res++;
            int lft = len-i;
            if(lft < k) return -1;

            for(int j = 0;j < k;++j)
                if(s[i+j] == '+')
                    s[i+j] = '-';
                else
                    s[i+j] = '+';

        }
    return res;
}


int main()
{
    freopen("./A-large.in","r",stdin);
    freopen("./out.txt","w",stdout);
    int kase;
    scanf("%d",&kase);
    for(int z = 1;z <= kase;++z)
    {
        scanf("%s",s);
        scanf("%d",&k);
        int res = solve();
        if(res == -1)
            printf("Case #%d: IMPOSSIBLE\n",z);
        else
            printf("Case #%d: %d\n",z,res);
    }

    return 0;
}
