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
    int N,K;
    cin >> N >> K;
    vector<long double> R(N),H(N);
    rep(i,0,N) cin >> R[i] >> H[i];
    
    vector<int> index;
    rep(i,0,N) index.push_back(i);
    sort(index.begin(),index.end(),[&](int i,int j){ return R[i]*H[i]>R[j]*H[j]; });
    long double pi=acosl(-1),ans=0;
    rep(i,0,N){
        long double sum=pi*R[i]*R[i]+2*pi*R[i]*H[i];
        int cnt=1;
        for(int j:index){
            if(cnt==K) break;
            if(j==i or R[j]>R[i]) continue;
            sum+=2*pi*R[j]*H[j];
            ++cnt;
        }
        if(cnt<K) continue;
        ans=max(ans,sum);
    }
    cout << ans << endl;
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
