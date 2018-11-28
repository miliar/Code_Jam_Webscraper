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
    int N;
    vector<int> num(7);
    cin >> N >> num[1] >> num[3] >> num[2] >> num[6] >> num[4] >> num[5];
    map<tuple<int,int,vector<int>>,bool> memo;
    map<tuple<int,int,vector<int>>,int> next;
    function<bool(int,int,vector<int>)> rec=[&](int h,int t,vector<int> v){
        auto state=make_tuple(h,t,v);
        if(memo.find(state)!=memo.end()) return memo[state];
        auto &res=memo[state];
        int sum=accumulate(v.begin(),v.end(),0);
        if(sum==0){
            if(N==1) return res=true;
            return res=(h&t)==0;
        }
        int R_=v[1],Y_=v[2],O_=v[3],B_=v[4],V_=v[5],G_=v[6];
        if(R_>Y_+B_+1 or Y_>R_+B_+1 or B_>R_+Y_+1 or O_>B_+1 or G_>R_+1 or V_>Y_+1 or R_+O_+V_>Y_+B_+G_+1 or Y_+O_+G_>R_+B_+V_+1 or B_+G_+V_>R_+Y_+O_+1) return memo[state]=false;
        rep(i,1,7){
            if(v[i]==0 or t&i) continue;
            auto v_=v;
            --v_[i];
            if(rec(h,i,v_)){
                memo[state]=true;
                next[state]=i;
                return true;
            }
        }
        return res=false;
    };

    string c="ARYOBVG";
    rep(i,1,7){
        if(num[i]>0){
            auto v=num;
            --v[i];
            if(rec(i,i,v)){
                string ans;
                int t=i;
                while(ans.size()<N){
                    ans+=c[t];
                    t=next[make_tuple(i,t,v)];
                    --v[t];
                }
                cout << ans << endl;
                return;
            }
        }
    }
    cout << "IMPOSSIBLE" << endl;
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
