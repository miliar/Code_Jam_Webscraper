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
    LL n,k;
    Problem(LL n, LL k):n(n),k(k){};

    void solve(){
        map<LL,LL> m;
        m[n]=1;
        for(LL i=0; ;){
            auto it = m.end();
            it--;
            if(i+it->second>=k)break;
            i+=it->second;
            m[it->first/2]+=it->second;
            m[(it->first-1)/2]+=it->second;
            m.erase(it);
        }
        auto it = m.end();
        it--;
        cout << it->first/2 << ' '<<(it->first-1)/2 <<"\n";
    }
};

int main(){
    cin.tie(0);
    ios_base::sync_with_stdio(false);
    int testcases;
    cin >> testcases;
    for(int i=1; i<=testcases; ++i){
        cout << "Case #" << i << ": ";
        LL n,k;
        cin >> n >> k;
        Problem p(n,k);
        p.solve();
    }

    return 0;
}

