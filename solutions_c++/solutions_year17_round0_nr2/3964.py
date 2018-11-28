#include<bits/stdc++.h>
#include<algorithm>
using namespace std;
typedef long long int ll;
int main()
{
    freopen("1.in","r",stdin);
    freopen("1a.out","w",stdout);
    ll t,j=1;
    cin>>t;
    while(j<=t)
    {
        ll n,i,p,m,x,y,z,a,q,r;
        string s;
        cin>>s;
        for(i=s.size()-1;i>=1;i--)
        {
            if(s[i-1]>s[i])
            {
                for(p=i;p<s.size();p++)
                s[p]='9';
                s[i-1]-=1;
            }
        }
        if(s[0]=='0'){
        cout<<"Case #"<<j<<": ";
        for(i=1;i<s.size();i++)
        cout<<s[i];
        cout<<endl;
        }
        else
            cout<<"Case #"<<j<<": "<<s<<endl;
        j++;
    }
}
