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

string fail="IMPOSSIBLE";
string latte="RYB";

string solve(){
    int N;
    int R,Y,B,O,G,V;
    cin>>N>>R>>O>>Y>>G>>B>>V;

    vector<pint>vec;
    vec.pb({R,0});vec.pb({Y,1});vec.pb({B,2});
    sort(all(vec));reverse(all(vec));

    if(vec[0].fi>N/2)return fail;

    vint ans(N,-1);
    int cur=0;
    while(vec[0].fi){
        ans[cur]=vec[0].se;
        cur+=2;
        vec[0].fi--;
    }

    while(vec[1].fi){
        if(cur>=N)cur=1;
        ans[cur]=vec[1].se;
        cur+=2;
        vec[1].fi--;
    }

    rep(i,N)if(ans[i]==-1)ans[i]=vec[2].se;
    string res(N,'*');
    rep(i,N)res[i]=latte[ans[i]];
    return res;
}


signed main(){
    int T;scanf("%lld",&T);
    rep(i,T){
        printf("Case #%lld: ",i+1);
        cout<<solve()<<endl;
    }
    return 0;
}
