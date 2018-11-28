#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    int t,n,k,i,j,ans;
    cin>>t;
    for(ll te=1;te<=t;te++)
    {
        string s;
        cin>>s>>k;
        bool f=1;
        ans=0;
        for(i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                if(i+k-1>=s.length())
                    {f=0;break;}
                else
                {
                    ans++;
                    for(j=i;j<i+k;j++)
                        if(s[j]=='-')
                        s[j]='+';
                        else
                            s[j]='-';
                }
            }
        }
        if(f)
        cout<<"Case #"<<te<<": "<<ans<<endl;
        else
            cout<<"Case #"<<te<<": "<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
