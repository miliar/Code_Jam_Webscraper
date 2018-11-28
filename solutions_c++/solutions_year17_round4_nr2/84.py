#include <bits/stdc++.h>
using namespace std;
//make_tuple emplace_back next_permutation push_back make_pair second first setprecision

#if MYDEBUG
#include "lib/cp_debug.h"
#else
#define DBG(...) ;
#endif

using LL = long long;
constexpr LL LINF=334ll<<53;
constexpr int INF=15<<26;
constexpr LL  MOD=1E9+7;

struct Problem{
    int n,c,m;
    vector<vector<LL>> t;
    vector<LL> cnt,seat;
    Problem(LL n,int c, int m):n(n),c(n),m(m),t(n,vector<LL>(c)),cnt(c),seat(n){};

    void solve(){
        for(int i=0; i<m; ++i){
            int a,b;
            cin >> a >> b;
            --a;--b;
            t[a][b]++;
            cnt[b]++;
        }
        LL prom=0,maxi=0;
        LL sum=0;
        for(int i=0; i<n; ++i){
            seat[i]=accumulate(t[i].begin(),t[i].end(),0ll);
            sum+=seat[i];
            maxi=max((sum+i)/(i+1),maxi);
        }
        int ans=max(*max_element(cnt.begin(),cnt.end()),maxi);
        for(int i=0; i<n; ++i){
            prom+=max<LL>(0,seat[i]-ans);
        }
        cout << ans <<' '<<prom <<"\n";
    }
};

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int testcases;
    cin >> testcases;
    for(int i=1; i<=testcases; ++i){
        cout << "Case #" << i << ": ";
        int n,c,m;
        cin >> n >> c >> m;
        Problem p(n,c,m);
        p.solve();
    }


    return 0;
}

