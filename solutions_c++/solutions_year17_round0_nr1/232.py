#include <bits/stdc++.h>
using namespace std;


char s[10050];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("2.txt", "w", stdout);
    int t,ti=1;scanf("%d",&t);
    while(t--)
    {
        int k,sum=0;
        scanf("%s%d",s,&k);
        for(int i=0;s[i+k-1];i++)
            if(s[i]=='-')
            {
                for(int j=0;j<k;j++)
                    if(s[i+j]=='-')
                        s[i+j]='+';
                    else
                        s[i+j]='-';
                sum++;
            }
        bool can=1;
        for(int i=0;s[i];i++)
            if(s[i]=='-')
            {
                can=0;
                break;
            }
        printf("Case #%d: ",ti++);
        if(can==0)
            puts("IMPOSSIBLE");
        else
            printf("%d\n",sum);
    }
    return 0;
}
