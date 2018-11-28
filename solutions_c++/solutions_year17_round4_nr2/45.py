#include<bits/stdc++.h>
using namespace std;

#define int long long

#define rep(i,n) for(int i=0;i<(n);i++)
#define pb push_back
#define all(v) (v).begin(),(v).end()
#define fi first
#define se second
typedef vector<int>vint;
typedef pair<int,int>pint;
typedef vector<pint>vpint;

template<typename A,typename B>inline void chmin(A &a,B b){if(a>b)a=b;}
template<typename A,typename B>inline void chmax(A &a,B b){if(a<b)a=b;}

int N,M,C;

int cnt[1111],cnt2[1111];
int acc[1111];
void solve(){
    cin>>N>>C>>M;

    memset(cnt,0,sizeof(cnt));
    memset(cnt2,0,sizeof(cnt2));
    memset(acc,0,sizeof(acc));
    for(int i=0;i<M;i++){
        int p,h;
        cin>>p>>h;
        p--;h--;
        cnt[p]++;
        cnt2[h]++;
        acc[p]++;
    }

    int num=0;
    rep(i,C)chmax(num,cnt2[i]);
    rep(i,N)acc[i+1]+=acc[i];

    rep(i,N){
        chmax(num,(acc[i]+i)/(i+1));
    }

    int latte=0;
    for(int i=N-1;i>=0;i--){
        latte+=max(0ll,cnt[i]-num);
    }
    cout<<num<<" "<<latte<<endl;
}

signed main(){
    int T;cin>>T;
    for(int i=1;i<=T;i++){
        cout<<"Case #"<<i<<": ";
        solve();
    }
}
