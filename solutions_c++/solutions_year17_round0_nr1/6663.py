#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t,i,j,k,l,ans;
    string s;
    cin>>t;
    for(int tc=1;tc<=t;tc++)
    {
        cin>>s>>k;
        l=s.length();
        ans=0;
        for(i=0;i<l-k+1;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(j=i;j<i+k;j++)
                {
                   s[j]=(s[j]=='-')?'+':'-';
                }
            }
        }
        for(i=l-k+1;i<l;i++)
        {
            if(s[i]=='-')
            {
                ans=-1;
                break;
            }
        }
        cout<<"Case #"<<tc<<": ";
        if(ans==-1)
            cout<<"IMPOSSIBLE\n";
        else
            cout<<ans<<"\n";
    }
    return 0;
}


