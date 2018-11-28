#include<bits/stdc++.h>
#include<algorithm>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("2.in","r",stdin);
    freopen("2a.out","w",stdout);
    ll t,j=1;;
    cin>>t;
    while(j<=t)
    {
        ll n,flag=0,i,p,q,r,m,cnt=0;
        string s;
        cin>>s;
        cin>>m;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                if(i+m>s.size())
                {flag=1;break;}
                for(p=i;p<i+m;p++)
                {
                    if(s[p]=='-')
                        s[p]='+';
                    else
                        s[p]='-';
                }
                cnt++;
            }
        }
        if(flag==1)
            cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
        else
        cout<<"Case #"<<j<<": "<<cnt<<endl;
        j++;

    }
}
