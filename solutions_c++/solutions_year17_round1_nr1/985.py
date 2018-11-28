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
    int r,c;
    cin >> r >> c;
    vector<string> g(r);
    rep(i,0,r) cin >> g[i];
    rep(i,0,r){
        rep(j,1,c){
            if(g[i][j-1]=='?' or g[i][j]!='?') continue;
            g[i][j]=g[i][j-1];
        }
        for(int j=c-2; j>=0; --j){
            if(g[i][j+1]=='?' or g[i][j]!='?') continue;
            g[i][j]=g[i][j+1];
        }
    }
    rep(j,0,c){
        rep(i,1,r){
            if(g[i-1][j]=='?' or g[i][j]!='?') continue;
            g[i][j]=g[i-1][j];
        }
        for(int i=r-2; i>=0; --i){
            if(g[i+1][j]=='?' or g[i][j]!='?') continue;
            g[i][j]=g[i+1][j];
        }
    }
    rep(i,0,r) cout << g[i] << endl;
}

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);
    cout.setf(ios::fixed);
    cout.precision(10);
    int t;
    cin >> t;
    rep(i,0,t){
        cout << "Case #" << i+1 << ":" << endl;
        solve();
    }
    return 0;
}
