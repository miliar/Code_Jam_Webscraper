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
bool Less(LL s,LL t){
    return s*10<t*9;
}
bool More(LL s,LL t){
    return s*10>t*11;
}
bool inner(LL s,LL t){
    return (t*9<=s*10&&s*10<=t*11);
}
void solve(){
    int N,P;
    cin>>N>>P;
    vector<LL> r(N),R(N);
    vector<vector<LL>> Q(N,vector<LL>(P));
    vector<int> id(N,0);
    cin>>r>>Q;
    LL max_id=0;
    REP(i,N){
        Q[i].pb(1145141919);
        R[i]=r[i];
        if(R[max_id]<R[i])max_id=i;
    }
    REP(i,N)sort(ALL(Q[i]));
    int res=0;
    while(R[max_id]<=1500000){
        for(bool update=true;update;){
            update=true;
            REP(i,N){
                while(Less(Q[i][id[i]],R[i]))id[i]++;
                if(More(Q[i][id[i]],R[i]))update=false;
            }
            if(update){
                REP(i,N)id[i]++;
                res++;
            }
        }
        REP(i,N)R[i]+=r[i];
    }
    cout<<res<<endl;
        
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
