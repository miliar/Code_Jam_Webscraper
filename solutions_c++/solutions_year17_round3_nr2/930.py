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
    int Ac,Aj;
    cin >> Ac >> Aj;
    vector<section> secs;
    vector<int> sum(2);
    rep(i,0,Ac){
        int C,D;
        cin >> C >> D;
        secs.push_back(section({C,D,0,D-C}));
        sum[0]+=D-C;
    }
    rep(i,0,Aj){
        int J,K;
        cin >> J >> K;
        secs.push_back(section({J,K,1,K-J}));
        sum[1]+=K-J;
    }
    vector<int> used(1440,-1);
    rep(i,0,Ac) rep(j,secs[i].l,secs[i].r) used[j]=0;
    rep(i,0,Aj) rep(j,secs[Ac+i].l,secs[Ac+i].r) used[j]=1;
    sort(secs.begin(),secs.end(),[&](const section &a,const section& b){ return a.l<b.l; });
    vector<pair<int,int>> intervals;
    rep(i,0,Ac+Aj-1){
        if(secs[i].o!=secs[i+1].o) continue;
        intervals.push_back(make_pair(secs[i+1].l-secs[i].r,i));
    }
    if(secs[0].o==secs[Ac+Aj-1].o) intervals.push_back(make_pair(1440-secs[Ac+Aj-1].r+secs[0].l,Ac+Aj-1));
    sort(intervals.begin(),intervals.end());
    for(auto &p:intervals){
        int i=p.second,l=secs[i].r,r=secs[(i+1)%(Ac+Aj)].l;
        if(sum[secs[i].o]+p.first>720) continue;
        for(int j=0; j<p.first; ++j){
            used[(l+j)%1440]=secs[i].o;
            ++sum[secs[i].o];
        }
    }

    queue<int> q;
    rep(i,0,1440) if(used[i]!=-1) q.push(i);
    while(!q.empty()){
        int x=q.front();
        q.pop();
        if(sum[used[x]]==720) continue;
        rep(i,-1,2){
            if(i==0) continue;
            int x_=(x+i+1440)%1440;
            if(used[x_]!=-1) continue;
            q.push(x_);
            used[x_]=used[x];
            ++sum[used[x]];
        }
    }
    int ans=0;
    rep(i,0,1440) if(used[i]!=used[(i+1)%1440]) ++ans;
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
