#include<bits/stdc++.h>
using namespace std;
int solve()
{
    string s;
    cin>>s;
    int l=s.length();
    int k;int i,j;int ans=0;
    scanf("%d",&k);
    if(k>l)
        return -1;
    else
    {
        for(i=0;i<=l-k;i++)
        {
            if(s[i]=='-')
            {
                for(j=i;j<i+k;j++)
                    if(s[j]=='-')
                    {
                        s[j]='+';
                    }
                    else
                        s[j]='-';
                ans++;
            }
        }
        for(i=l-k;i<l;i++)
        {
            if(s[i]=='-')
            {
                ans=-1;
                break;
            }
        }
        return ans;
    }
}
int main()
{
    freopen("p1.in","r",stdin);
    freopen("p1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        int ans=solve();
        if(ans==-1)
            printf("Case #%d: IMPOSSIBLE\n",i);
        else
            printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
