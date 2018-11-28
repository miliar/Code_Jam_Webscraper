#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
	ll t;
    cin>>t;
    for(ll z=1;z<=t;z++)
    {
        int flag = 0,in,f=0;
        string s;
        cin>>s;
        ll n = s.length();
        for(ll i=0;i<n-1;i++)
        {
            if(s[i]>s[i+1]){
                in = i;
                f=1;
                break;
            }
        }
        if(n==1)
            f=0;
        cout<<"Case #"<<z<<": ";
        if(f==0)
            cout<<s<<endl;
        else{    
        char temp = s[in];
        if(temp=='1')
        {
            flag=1;
            for(ll i=in;i>=1;i--)
                s[i]='9';
        }
        if(temp!='1')
        s[in]=((s[in]-'0')-1)+'0';
        for(ll i=in-1;i>=0;i--)
        {
            if(s[i]==temp){
                s[i]=s[i+1];
                s[i+1]='9';}
            else
                break;
        }
        for(ll i = in+1;i<n;i++)
            s[i]='9';
        if(flag)
            for(ll i=1;i<n;i++)
                cout<<s[i];
        else
            cout<<s;
            cout<<endl;
        }
    }
 return 0;
}
