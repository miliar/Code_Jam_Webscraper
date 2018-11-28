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
    string n;
    cin >> n;
    i64 ans=(n.size()==1?0:stol(string(n.size()-1,'9')));
    rep(i,0,n.size()){
        if(i!=0 and n[i-1]>n[i]) break;
        ans=max(ans,stol(n.substr(0,i+1)));
        if(i!=0 and n[i-1]>n[i]-1) continue;
        ans=max(ans,stol(n.substr(0,i)+string(1,n[i]-1)+string(n.size()-i-1,'9')));
    }
    cout << ans << endl;
}

int main(){
    std::cin.tie(0);
    std::ios::sync_with_stdio(false);
    cout.setf(ios::fixed);
    cout.precision(10);
    int t;
    cin >> t;
    rep(i,1,t+1){
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
