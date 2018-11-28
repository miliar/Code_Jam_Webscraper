#include <bits/stdc++.h>
using namespace std;

#define rep(i,x,y) for(int i=(x);i<(y);++i)
#define debug(x) #x << "=" << (x)

#ifdef DEBUG
#define _GLIBCXX_DEBUG
#define print(x) std::cerr << debug(x) << " (L:" << __LINE__ << ")" << std::endl
#else
#define print(x)
#endif

const int inf=1e9;
const int64_t inf64=1e18;
const double eps=1e-9;

template <typename T> ostream &operator<<(ostream &os, const vector<T> &vec){
    os << "[";
    for (const auto &v : vec) {
    	os << v << ",";
    }
    os << "]";
    return os;
}

using i64=int64_t;

void solve(){
    i64 D,N;
    cin >> D >> N;
    vector<i64> K(N),S(N);
    rep(i,0,N) cin >> K[i] >> S[i];

    auto ok=[&](long double x){
        rep(i,0,N){
            if(x<=S[i]) continue;
            //x*t=K[i]+S[i]*t,(x-S[i])*t=K[i]
            long double t=K[i]/(x-S[i]);
            if(t*x<D) return false;
        }
        return true;
    };

    long double lb=0,ub=inf64;
    rep(i,0,256){
        long double m=(lb+ub)/2;
        if(ok(m)) lb=m;
        else ub=m;
    }
    cout << lb << endl;
}

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);
    cout.setf(ios::fixed);
    cout.precision(10);
    int t;
    cin >> t;
    rep(i,1,t+1){
        cout << "Case #" << i  << ": ";
        solve();
    }
    return 0;
}
