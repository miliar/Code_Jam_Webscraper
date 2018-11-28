#include <iostream>
#include <cstring>
#include <list>
using namespace std;
#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
int main()
{
    ll t;
    cin>>t;
    for(ll I=1;I<=t;I++)
    {
        ll flag=0;
        cout<<"Case #"<<I<<": ";
        string s;cin>>s;
        for(ll r=0;r<2*s.size()-1;r++){
            flag=0;
        for(ll i=0;i<s.size()-1;i++)
        {
            ll t = s[i]-'0';
            ll q = s[i+1]-'0';
            if(t<=q)
            continue;
            else
            {
                if(t!=0)
                {
                    if(flag==0)
                    {
                        t=t-1;
                        flag=1;
                    }
                    q=9;
                    s[i]='0'+t;
                    s[i+1]='0'+q;
                }
                else
                {
                    s[i+1]='0'+9;
                    s[i]='0'+9;
                    ll j=i-1;
                    while(j>=0)
                    {
                        if(s[j]-'0'>0)
                        {
                            ll q1=s[j]-'0';
                            if(flag==0)
                            s[j]='0'+q1-1;
                            break;
                        }
                        else
                        {
                            s[j]='9';
                            continue;
                        }
                    }
                }
            }
        }
        }
        ll u=0;
        while(s[u]=='0')
        {
            u++;
        }
        s=s.substr(u,s.size()-u);
        cout<<s<<endl;
    }
}
    