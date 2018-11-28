//Bismillahir Rahmanir Rahim
#include <bits/stdc++.h>
using namespace std;

char aa[100009];
int ar[100009];

int main()
{
    freopen("out.txt","rt",stdin);
    freopen("out1.txt","wt",stdout);
    long long i,j,k,l,n,cas,test,flag,temp,now,ans=0,m;

    cin>>test;
    for(cas=1;cas<=test;cas++)
    {
        scanf("%s%lld",aa,&m);
        n=strlen(aa);

        for(i=1;i<=n;i++) ar[i]=(aa[i-1]=='+');

        ans=0;
        for(i=1;i<=n-m+1;i++)
        {
            if(ar[i]==0)
            {
                for(j=1;j<=m;j++) ar[i+j-1]=!ar[i+j-1];
                ans++;
            }
        }

        flag=1;
        for(i=1;i<=n;i++) if(ar[i]==0) flag=0;

        if(flag) printf("Case #%lld: %lld\n",cas,ans);
        else printf("Case #%lld: IMPOSSIBLE\n",cas);

    }



}
