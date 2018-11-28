#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large_out.out","w",stdout);

    int t;
    cin>>t;

    int cs=0;
    string in;
    int k;
    while(cs<t)    {
        cin>>in>>k;
        int ans=0;
        for(int i=0;i<=in.length()-k;i++)    {
            if(in[i]=='-')    {
                for(int j=i;j<i+k;j++)    {
                    if(in[j]=='-')    in[j]='+';
                    else    in[j]='-';
                }
                ans++;
            }

        }
        bool ok=1;
        for(int i=0;i<in.length();i++)    {
            if(in[i]=='-')    {ok=0;break;}
        }
        if(!ok)    cout<<"Case #"<<++cs<<": "<<"IMPOSSIBLE"<<endl;
        else    cout<<"Case #"<<++cs<<": "<<ans<<endl;
    }

    return 0;
}
