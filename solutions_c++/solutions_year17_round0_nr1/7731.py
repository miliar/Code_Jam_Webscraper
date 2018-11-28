#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("out1.txt","w",stdout);
    int t,n,tc,l;
    char pan[1005];
    scanf("%d",&tc);
    for(t=1;t<=tc;t++)
    {
        scanf("%s %d",pan,&n);
        int l = strlen(pan);
        int cnt  = 0;
        for(int i = 0;i<l;i++)
        {
            if(pan[i]=='+')continue;
            cnt++;
            if(l-i<n)break;
            for(int j = i;j<i+n;j++)
            {
                if(pan[j]=='+')pan[j] = '-';
                else pan[j] = '+';
            }
            //printf("%s\n",pan);
        }
        bool flag = true;
        for(int i = 0;i<l;i++)
        {
            if(pan[i]=='-')
            {
                flag = false;
                break;
            }
        }
        printf("Case #%d: ",t);
        if(!flag)printf("IMPOSSIBLE\n");
        else printf("%d\n",cnt);

    }
    return 0;
}
