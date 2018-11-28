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

string s;
LL n;

void done(int cn, string ans)
{
    cout<<"Case #"<<cn<<": "<<ans<<endl;
}

void solve(int cn)
{
    cin>>s;

    int ind=0;
    for(;ind<s.length()-1;ind++){
        if(s[ind]>s[ind+1]) break;
    }

    if(s.length()==1 || ind==s.length()-1) {
        done(cn, s);
        return;
    }

    int start=ind;
    while(start>=0 && s[start]==s[ind]){
        start--;
    }
    // trace1(start);

    start++;
    s[start]--;
    start++;
    while(start<s.length()) s[start++]='9';

    char ans[s.length()+10];

    int sind=0, aind=0;

    while(sind<s.length()){
        if(s[sind]=='0'){
            sind++;
            continue;
        }
        ans[aind]=s[sind];
        aind++;
        sind++;
    }
    ans[aind]='\0';
    done(cn, ans);

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


