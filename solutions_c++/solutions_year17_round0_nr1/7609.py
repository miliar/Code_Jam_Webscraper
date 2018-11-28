#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int x=1;
    while(x<=t)
    {   int ans=0;
        string s;
        int k;
        cin>>s>>k;
        int n=s.length();
        int i=0;
        for(i=0;i<=n-k;i++)
        {
            if(s[i]=='+')
                 continue;
            ans++;
            int j=i;
            int l=k;
            for(j;j<n&&l>0;j++)
            {
                if(s[j]=='+')
                   s[j]='-';
                else
                   s[j]='+';
                l--;
            }
        }
        int flag=0;
        //cout<<s<<endl;
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                cout<<"Case #"<<x<<": "<<"IMPOSSIBLE"<<endl;
                flag=1;
                x++;
                break;
            }
        }
        if(flag==1)
              continue;
        cout<<"Case #"<<x<<": "<<ans<<endl;
        x++;

    }
    return 0;
}
