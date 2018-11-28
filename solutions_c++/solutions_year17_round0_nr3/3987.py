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

void done(int cn, LL ans1, LL ans2)
{
    cout<<"Case #"<<cn<<": "<<ans2<<" "<<ans1<<endl;
}

typedef pair<int, int> PII;
typedef pair<int, PII> PIII;
LL n, k;

struct compare{
    bool operator()(const PIII& a, const PIII& b)
    {
        return (    (a.first<b.first) ||
                    (a.first==b.first && a.second.first>b.second.first) ||
                    (a.first==b.first && a.second.first==b.second.first && a.second.second>b.second.second)
                );
    }
};


void solve(int cn)
{
    cin>>n>>k;

    priority_queue<PIII, vector<PIII>, compare > q;
    q.push({n, {1, n}});

    PIII top;
    LL s, l, r, ls, rs, ll, lr, rl, rr;

    LL ans1, ans2;
    while(k--){
        top=q.top();
        q.pop();
        s=top.first;
        l=top.second.first;
        r=top.second.second;
        //trace3(s, l, r);

        ls=(s-1)/2;
        ll=l;
        lr=l+ls-1;

        rs=(s-1)-ls;
        rr=r;
        rl=lr+2;

        q.push({ls, {ll,lr} });
        q.push({rs, {rl,rr} });

        ans1= ls;
        ans2= rs;
    }

    done(cn, ans1, ans2);
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


