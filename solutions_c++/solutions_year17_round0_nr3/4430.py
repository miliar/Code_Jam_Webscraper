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
void solve(){
    LL N,K;
    cin>>N>>K;
    map<LL,LL> num;
    num[-N]=1;
    while(1){
        map<LL,LL> nxt;
        for(auto &it:num){
            LL len=it.fi;
            LL cnt=it.se;
            len++;
            LL l=len/2;
            LL r=len-l;
            if(l<0)nxt[l]+=cnt;
            if(r<0)nxt[r]+=cnt;
            LL latte=min(K,cnt);
            K-=latte;
            cnt-=latte;
            if(K==0){
                cout<<max(-l,-r)<<" "<<min(-l,-r)<<endl;
                return;
            }
        }
        swap(num,nxt);
    }
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
