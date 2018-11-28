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

unordered_map<i64,map<i64,i64>> cnt;

void rec(i64 len){
    if(cnt.find(len)!=cnt.end()) return;
    ++cnt[len][len];
    i64 l=0,r=len-1,m=(l+r)/2;
    if(l!=m){
        i64 len_=m-l;
        rec(len_);
        for(auto &p:cnt[len_]) cnt[len][p.first]+=p.second;
    }
    if(r!=m){
        i64 len_=r-m;
        rec(len_);
        for(auto &p:cnt[len_]) cnt[len][p.first]+=p.second;
    }
}

void solve(){
    i64 n,k;
    cin  >> n >> k;
    rec(n);
    i64 s=0;
    for(auto it=cnt[n].rbegin(); it!=cnt[n].rend(); ++it){
        if(s+it->second>=k){
            i64 l=0,r=it->first-1,m=(l+r)/2;
            cout << max(m-l,r-m) << " " << min(m-l,r-m) << endl;
            break;
        }
        s+=it->second;
    }
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
