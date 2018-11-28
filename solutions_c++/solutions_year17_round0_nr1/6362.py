#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t,ts;
    cin>>ts;
    for(t=1;t<=ts;t++)
    {
        int n,k;
        string s;
        cin>>s>>k;
        n=s.size();
        int f=1,ans=0;
        for(int i=0;i<n;i++)
            if(s[i]=='-'&&i+k-1<n)
                {for(int j=i;j<i+k;j++)
                    if(s[j]=='-') s[j]='+';
                    else s[j]='-';
                 ans++;
                }

        for(int i=0;i<n;i++) if(s[i]=='-') f=0;
        if(f==0) printf("Case #%d: IMPOSSIBLE\n",t);
        else printf("Case #%d: %d\n",t,ans);
    }
}
