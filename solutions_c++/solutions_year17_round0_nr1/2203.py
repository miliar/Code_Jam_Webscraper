#include<bits/stdc++.h>

using namespace std;

int t,k,cs=1;
char s[20004];

int main()
{
    freopen("A-large(1).in","r",  stdin);
    freopen("A-large-output.txt","w", stdout);

    scanf("%d",&t);

    while(t--)
    {
        scanf("%s %d",s,&k);

        int ans=0;
        int n= strlen(s);
        for(int i=0; i<=n-k; i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(int j=i; j<i+k; j++)
                {
                    if(s[j]=='-') s[j]= '+';
                    else s[j]='-';
                }
            }
        }
        int fl=1;

        for(int i=0; i<n; i++)
        {
            if(s[i]=='-') fl=0;
        }

//        printf(" %s\n",s);
        if(fl)printf("Case #%d: %d\n",cs++,ans);
        else printf("Case #%d: IMPOSSIBLE\n",cs++);
    }
}
