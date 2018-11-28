#include<bits/stdc++.h>

using namespace std;

#define LL long long
#define pb push_back
#define pLL pair<LL,LL>
#define ff first
#define ss second
#define rep(i,a,b) for(LL i=a;i<=b;++i)
#define repb(i,a,b) for(LL i=a;i>=b;--i)
#define ld double
#define mp make_pair
#define vLL vector<LL>
#define vpLL vector<pLL>
#define vld vector<ld>
#define pld pair<ld,ld>
#define vpld vector<pld>
#define SLL set<LL>
#define SpLL set<pLL>
#define FIO ios::sync_with_stdio(false);cin.tie(0);cout.tie(0)

LL t;
string s;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>t;
    rep(lp,1,t){
        cin>>s;
        LL n=s.size();
        s=" "+s;
        cout<<"Case #"<<lp<<": ";
        LL ans=0;
        rep(i,2,n) if(s[i]<s[i-1]){
            s[i-1]--;
            rep(j,i,n) s[j]='9';
            i-=2;
        }
        if(s[1]=='0') s=s.substr(2);
        else s=s.substr(1);
        cout<<s<<"\n";
    }
}
