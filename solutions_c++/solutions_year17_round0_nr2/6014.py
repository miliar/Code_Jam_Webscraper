


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
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
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
        ll p=s.size()-1;
        ll loc=0,sexy=-1,fun=0;
        fr(ia,1,p)
        {
            if(s[ia]<s[ia-1])
            {
                if(sexy==-1) sexy=ia-1;
                fun=0;
                 break;
            }
            else if(s[ia]==s[ia-1])
            {
                if(sexy==-1) sexy=ia-1; fun++;
            }
            else sexy=-1;
        }
        //cout<<sexy<<endl;
        if(sexy>=0 && fun) sexy=-1;
        if(sexy>=0)
        {
        ll ck=0;
        fr(ia,0,p)
        {
            if(sexy==ia)
            {
                if(s[ia]=='1') s[ia]='0';
                else s[ia]=(char) s[ia]-1;
                ck++;
            }
            else if(ck)
            {
                s[ia]='9';
            }
        }
        }
        cout<<"Case #"<<i<<": ";
        fr(ia,0,p)
        {
            if(s[ia]=='0' && !ia) {}
            else cout<<s[ia];
        }
        cout<<endl;
    }












}

