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

LL t,k,dp[2005][2005];
string s;

inline void flip(LL p)
{
    if(s[p]=='+') s[p]='-';
    else s[p]='+';
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>t;
    rep(lp,1,t){
        cin>>s>>k;
        LL n=s.size();
        s=" "+s;
        cout<<"Case #"<<lp<<": ";
        LL ans=0;
        repb(i,n,k) if(s[i]=='-'){
            ans++;
            rep(j,i-k+1,i) flip(j);
            //cout<<i<<" "<<s<<endl;
        }
        bool chk=true;
        rep(i,1,n) if(s[i]=='-') chk=0;
        if(chk) cout<<ans<<"\n";
        else cout<<"IMPOSSIBLE\n";
    }
}
