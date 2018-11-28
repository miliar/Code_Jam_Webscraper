


#include<bits/stdc++.h>
#define ll long long
#define pb push_back
#define mp make_pair
#define MX 10000000
#define pll pair<ll,ll>
#define fr(i,a,b) for(ll i=a;i<=b;i++)
#define re_fr(i,a,b) for(ll i=a;i>=b;i--)
#define mod 1000000007
#define fast() ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
using namespace std;
ll gcd(ll a,ll b) {return b==0?a:gcd(b,a%b);}
void fil()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
}



bool vis[30];
int main()
{
    fast();
    fil();

    ll n; cin>>n;
    fr(i,1,n)
    {
        string s; cin>>s;
        ll k; cin>>k;
        ll ans=0;
        ll p=s.size()-1;
        fr(ia,0,p)
        {
            ll sz=p-ia+1;
            if(sz<k) break;
            else
            {
                if(s[ia]=='-')
                {
                    fr(ja,ia,ia+k-1)
                    {
                        if(s[ja]=='-') s[ja]='+';
                        else if(s[ja]=='+') s[ja]='-';
                    }


                    ans++;
                }
            }
        }
        ll ck=0;
        fr(ia,0,p)
        {
            if(s[ia]=='-') ck++;
        }
        cout<<"Case #"<<i<<": ";
        if(!ck) cout<<ans<<endl;
        else cout<<"IMPOSSIBLE"<<endl;
    }












}


