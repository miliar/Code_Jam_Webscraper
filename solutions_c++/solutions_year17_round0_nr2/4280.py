#include<bits/stdc++.h>
using namespace std;
typedef long long LL;

#define CIN_ONLY if(1)
struct cww{cww(){
    CIN_ONLY{
        ios::sync_with_stdio(false);cin.tie(0);
    }
}}star;
#define fin "\n"
#define FOR(i,bg,ed) for(int i=(bg);i<(ed);i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(v) (v).begin(),(v).end()
#define fi first
#define se second
#define pb push_back
#define DEBUG if(0)
#define REC(ret, ...) std::function<ret (__VA_ARGS__)>
template <typename T>inline bool chmin(T &l,T r)
{bool a=l>r;if(a)l=r;return a;}
template <typename T>inline bool chmax(T &l,T r)
{bool a=l<r;if(a)l=r;return a;}
template <typename T>
istream& operator>>(istream &is,vector<T> &v){
    for(auto &it:v)is>>it;
    return is;
}
typedef pair<LL,LL> P;
LL f(vector<LL> &v,P pv,map<P,LL> &memo){
    if(memo.count(pv))return memo[pv];
    LL pos=pv.fi;
    LL val=pv.se;
    LL ret=-1;
    if(pos==v.size())return memo[pv]=0;
    LL ten=1;
    FOR(i,pos+1,v.size())ten*=10;
    FOR(nxt,val,v[pos]){
        //LL g=f(v,P(pos+1,nxt),memo);
        //if(g==-1)continue;
        chmax(ret,ten-1+ten*nxt);
    }
    if(v[pos]>=val){
        LL g=f(v,P(pos+1,v[pos]),memo);
        if(g>=0)chmax(ret,ten*v[pos]+g);
    }
    //cout<<pos<<" "<<val<<" "<<ret<<endl;
    return memo[pv]=ret;
}
void solve(){
    LL N;
    cin>>N;
    LL ret=1;
    vector<LL> v;
    while(N){
        v.pb(N%10);N/=10;
    }
    reverse(ALL(v));
    map<P,LL> memo;
    cout<<max(f(v,P(0,0),memo),ret)<<endl;
}
int main(){
    int T;
    cin>>T;
    FOR(i,1,T+1){
        cout<<"Case #"<<i<<": ";
        solve();
    }
    return 0;
}
