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

void solve(){
    int N,K;
    cin>>N>>K;
    priority_queue<pint>que;
    que.push(pint(N,1));
    while(K){
        pint p=que.top();
        que.pop();
        while(que.size()&&que.top().fi==p.fi){
            p.se+=que.top().se;
            que.pop();
        }
        int a=p.fi/2;
        int b=p.fi-1-a;
        if(a<b)swap(a,b);

        if(K<=p.se){
            cout<<a<<" "<<b<<endl;
            return;
        }
        que.push(pint(a,p.se));
        que.push(pint(b,p.se));
        K-=p.se;
    }
}

signed main(){
    int T;
    cin>>T;
    rep(i,T){
        cout<<"Case #"<<i+1<<": ";
        solve();
    }
    return 0;
}
