#include<bits/stdc++.h>
#define X first
#define Y second
#define MEM(x,y) memset(x,y,sizeof x)
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,cas,n,i,j,ans,ok;
    string s;
    cin>>t;
    for(cas=1;cas<=t;cas++)
    {
        ans=0;
        cin>>s>>n;
        for(i=0;i+n<=s.size();i++)
        {
            if(s[i]=='-')
            {
                for(j=0;j<n;j++)
                {
                    if(s[i+j]=='+')s[i+j]='-';
                    else s[i+j]='+';
                }
                ans++;
            }
        }
        ok=1;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='-')ok=0;
        }
        if(ok)printf("Case #%d: %d\n",cas,ans);
        else printf("Case #%d: IMPOSSIBLE\n",cas);
    }
}
