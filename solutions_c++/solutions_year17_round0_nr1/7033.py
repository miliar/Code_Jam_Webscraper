#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("inputu2.in","r",stdin);
    freopen("output2.txt","w",stdout);
    int t,c=1,k;
    cin>>t;
    string s;
    while(t--)
    {
        cin>>s>>k;
        cout<<"Case #"<<c<<": ";
        c++;
        int n=s.length(),ans=0;
        for(int i=0; i<n-k+1; i++)
        {
            if(s[i]=='+')
                continue;
            ans++;
            for(int j=i; j<i+k; j++)
            {
                if(s[j]=='-')
                    s[j]='+';
                else
                    s[j]='-';
            }
        }
        for(int i=0; i<n; i++)
        {
            if(s[i]=='-')
            {
                ans=-1;
                break;
            }
        }
        if(ans==-1)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
            cout<<ans<<endl;

    }
    return 0;
}
