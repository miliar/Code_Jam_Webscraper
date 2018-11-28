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

void solve(){
    int R,C;
    cin>>R>>C;
    vector<string> S(R);
    cin>>S;
    cout<<endl;
    REP(i,R)FOR(j,1,C){
        if(S[i][j]=='?')S[i][j]=S[i][j-1];
    }
    REP(i,R)FOR(j,1,C){
        if(S[i][C-j-1]=='?')S[i][C-j-1]=S[i][C-j];
    }
    
    FOR(i,1,R){
        if(S[i][0]=='?')S[i]=S[i-1];
    }
    FOR(i,1,R){
        if(S[R-i-1][0]=='?')S[R-i-1]=S[R-i];
    }
    
    REP(i,R)cout<<S[i]<<endl;
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
