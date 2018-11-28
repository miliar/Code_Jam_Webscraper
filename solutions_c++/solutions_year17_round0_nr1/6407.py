#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    ll t,j=1;;
    cin>>t;
    while(j<=t)
    {
        ll n,flg=0,i,p,q,r,m,cnt=0;
        string s;
        cin>>s;
        cin>>m;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                if(i+m>s.size())
                {flg=1;break;}
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
        if(flg==1)
            cout<<"Case #"<<j<<": "<<"IMPOSSIBLE"<<endl;
        else
        cout<<"Case #"<<j<<": "<<cnt<<endl;
        j++;

    }
}
