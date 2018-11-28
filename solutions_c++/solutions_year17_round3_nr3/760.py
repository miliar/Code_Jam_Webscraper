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

struct section{
    int l,r,o,len;
};

void solve(){
    int N,K;
    cin >> N >> K;
    long double U;
    vector<long double> P(N);
    cin >> U;
    rep(i,0,N) cin >> P[i];

    auto ok=[&](long double x){
        long double s=0,res=1;
        rep(i,0,N){
            if(P[i]>=x){
                res*=P[i];
                continue;
            }
            if(s+x-P[i]>=U) return (long double)0;
            s+=x-P[i];
            res*=x;
        }
        return res;
    };

    long double lb=0,ub=1;
    rep(i,0,128){
        long double m=(lb+ub)/2;
        if(ok(m)) lb=m;
        else ub=m;
    }
    cout << ok(lb) << endl;
}

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);
    cout.setf(ios::fixed);
    cout.precision(10);
    int T;
    cin >> T;
    rep(i,1,T+1){
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
