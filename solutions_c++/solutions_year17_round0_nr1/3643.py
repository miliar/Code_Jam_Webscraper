#include "bits/stdc++.h"
using namespace std;
typedef long long ll;
string s;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,k=0;
    cin>>t;
    while(k<t)
    {
        int n,m,i,j,ans=0,f=0;
        cin>>s>>m;
        n=s.length()-m+1;
        for(i=0;i<n;i++)
        if(s[i]=='-')
        {
            ans++;
            for(j=1;j<m;j++)
                s[i+j]=s[i+j]=='-'?'+':'-';
        }
        n=s.length();
        for(;i<n;i++)
        if(s[i]=='-'){f=1;break;}
        printf("Case #%d: ",++k);
        if(f)printf("IMPOSSIBLE");
        else printf("%d",ans);
        printf("\n");
    }
    return 0;
}
