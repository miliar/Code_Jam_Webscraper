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
    int n,m;
    vector<vector<LL>> a;
    vector<LL> need;
    vector<int> pos;
    Problem(LL n, LL m):n(n),m(m),a(n,vector<LL>(m)),need(n),pos(n,-1){};

    void solve(){
        for(int i=0; i<n; ++i){
            cin >> need[i];
        }
        for(int i=0; i<n; ++i){
            for(int j=0; j<m; ++j){
                cin >> a[i][j];
                a[i][j]*=10;
            }
        }
        for(int i=0; i<n; ++i){
            sort(a[i].begin(),a[i].end());
        }
        LL ans=0;
        for(int i=1; i<1200000; ++i){
            bool can=true;
            vector<int> tmp;
            for(int j=0; j<n; ++j){
                auto lb= max<int>(lower_bound(a[j].begin(),a[j].end(),need[j]*i*9)-a[j].begin(),pos[j]+1);
                if(lb==m){can=false;i=1200000;break;}
                if(a[j][lb]<=need[j]*i*11){
                    tmp.push_back(lb);
                }else{
                    can=false;
                    break;
                }
            }
            if(can){
                DBG(i,ans)
                ans++;
                --i;
                DBG(i,ans)
                for(int j=0; j<n; ++j){
                    pos[j]=tmp[j];
                }
            }
        }
        cout << ans <<"\n";
    }
};

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int testcases;
    cin >> testcases;
    for(int i=1; i<=testcases; ++i){
        cout << "Case #" << i << ": ";
        LL n,m;
        cin >> n>>m;
        Problem p(n,m);
        p.solve();
    }

    return 0;
}

