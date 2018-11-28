#include<bits/stdc++.h>
using namespace std;
#define LL long long
#define LD long double
const LL mod=1000000007;
const LD pi = 3.14159265358979323846264338327950288419716939937510;
const LD eps = 1e-10;
const int oo = INT_MAX;
const LL ooo = LONG_LONG_MAX;
LL pwr(LL a,LL b,LL m) {LL res=1%m;a%=m;for(;b;b>>=1){if(b&(1LL))res=res*a%m;a=a*a%m;}return res;} // zero and positive power
#define trace1(x)           cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<endl
#define trace2(x,y)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<endl
#define trace3(x,y,z)       cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "<<x<<" | "#y" = "<<y<<" | "#z" = "<<z<<endl
#define trace4(a,b,c,d)     cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<endl
#define trace5(a,b,c,d,e)   cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<endl
#define trace6(a,b,c,d,e,f) cerr<<__FUNCTION__<<":"<<__LINE__<<": "#a" = "<<a<<" | "#b" = "<<b<<" | "#c" = "<<c<<" | "#d" = "<<d<<" | "#e" = "<<e<<" | "#f" = "<<f<<endl
#define tracea(x,b)         cerr<<__FUNCTION__<<":"<<__LINE__<<": "#x" = "; for(int i=0;i<b;i++){ cerr<<x[i]<<","; }cerr<<endl;

void done(int cn, int ans)
{
    cout<<"Case #"<<cn<<": "<<ans<<endl;
}
void donestr(int cn)
{
    cout<<"Case #"<<cn<<": "<<"IMPOSSIBLE"<<endl;
}

string s;
int k;
int len;

bool flip(int st)
{
    for(int i=st; i<st+k; i++){
        if(s[i]=='-'){
            s[i]='+';
        }
        else{
            s[i]='-';
        }
    }
}

int cntminus(int st)
{
    int ret=0;
    for(int i=st;i<len;i++)
        if(s[i]=='-')
            ret++;
    return ret;
}

void solve(int cn)
{
    cin>>s>>k;
    len=s.length();
    int ans=0;
    //trace1(s);
    for(int i=0;i+k<len;i++){
        if(s[i]=='-'){
            flip(i);
            ans++;
        }
        //trace2(i, s);
    }
    int cnt= cntminus(len-k);
    //trace1(cnt);
    if(cnt==0){
        done(cn, ans);
    }
    else if(cnt<k){
        donestr(cn);
    }
    else if(cnt==k){
        done(cn, ans+1);
    }
}

int main()
{
    ios_base::sync_with_stdio(0);
    //freopen("ip.txt","r",stdin);
    //freopen("op.txt","w",stdout);

    int t; cin>>t;
    for(int i=1;i<=t;i++){
        solve(i);
    }

    return 0;
}


