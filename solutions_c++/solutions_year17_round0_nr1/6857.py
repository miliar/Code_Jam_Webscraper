//SHUBHAM RANA says hello
#include <bits/stdc++.h>
#define sp " "
#define br "\n"
using namespace std;
typedef long long int ll;
typedef set<ll>::iterator si;
typedef map<ll,ll>::iterator mi;
const ll MOD=1000000007;
const ll INF=LLONG_MAX;
const double MU=0.000001;
const double PI=3.14159265359;
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	freopen("input_large.txt","r",stdin);
	freopen("output_large.txt","w",stdout);
    ll tt;
    cin>>tt;
    for(ll t=1;t<=tt;t++)
    {
        ll res=0;
        string s;
        cin>>s;
        ll k;
        cin>>k;
        ll n=s.length();
        for(ll i=0;i<=n-k;i++)
        {
            if(s[i]=='+')
                continue;
            else
            {
                //cout<<i<< " ";
                res++;
                ll j=i;
                for(ll j=0;j<k;j++)
                {
                    if(s[i+j]=='+')
                        s[i+j]='-';
                    else
                        s[i+j]='+';
                }
            }
        }
        char d=s[s.length()-k];
        //cout<<d;
        bool b=true;
        for(ll i=n-k;i<n;i++)
        {
            //cout<<s[i];
            if(s[i]!=d)
                b=false;
        }
        if(b&&d=='-')
            res++;
        b?cout<< "Case #"<<t<< ": "<<res<<br:cout<< "Case #"<<t<<": "<< "IMPOSSIBLE"<<br;
    }
	return 0;
}
