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

struct max_flow{
    struct edge{int to,cap,rev;};
    vector<vector<edge>> graph;
    vector<bool> done;
    max_flow(int size):graph(size),done(size){}
    void add_edge(int from,int to,int cap){
        graph[from].push_back(edge{to,cap,(int)graph[to].size()});
        graph[to].push_back(edge{from,0,(int)graph[from].size()-1});
    }
    int dfs(int v,int t,int f){
        if(v==t) return f;
        done[v]=true;
        for(auto &e:graph[v]){
            if(done[e.to] or e.cap<=0) continue;
            int d=dfs(e.to,t,min(f,e.cap));
            if(d>0){
                e.cap-=d;
                graph[e.to][e.rev].cap+=d;
                return d;
            }
        }
        return 0;
    }
    int calc_max_flow(int s,int t){
        int flow=0;
        while(true){
            fill(done.begin(),done.end(),false);
            int f=dfs(s,t,inf);
            if(f==0) return flow;
            flow+=f;
        }
    }
};

//1-P
//P+1 - 2*P

//i*P+j - i*P+P
//i*P+P+1 - i*P+P


void solve(){
    int N,P;
    cin >> N >> P;
    vector<int> R(N);
    vector<vector<int>> Q(N,vector<int>(P));
    rep(i,0,N) cin >> R[i];
    rep(i,0,N){
        rep(j,0,P) cin >> Q[i][j];
        sort(Q[i].begin(),Q[i].end());
    }

    map<vector<int>,int> memo;
    function<int(vector<int>&)> rec=[&](vector<int> &v){
        if(memo.find(v)!=memo.end()) return memo[v];
        int &res=memo[v];
        int lb=1,ub=inf,mi=inf,index=-1;
        rep(i,0,N){
            lb=max(lb,(10*Q[i][v[i]]+11*R[i]-1)/(11*R[i]));
            ub=min(ub,(10*Q[i][v[i]])/(9*R[i]));
            if(index==-1 or mi>(10*Q[i][v[i]])/(9*R[i])){
                index=i;
                mi=(10*Q[i][v[i]])/(9*R[i]);
            }
        }
        if(lb<=ub){
            bool f=false;
            rep(i,0,N){
                ++v[i];
                if(v[i]==P) f=true;
            }
            if(!f) res=max(res,rec(v)+1);
            else res=max(res,1);
            rep(i,0,N) --v[i];
            return res;
        }

        if(v[index]==P-1)  return res;
        ++v[index];
        res=max(res,rec(v));
        --v[index];
        return res;
    };
    vector<int> v(N);
    cout << rec(v) << endl;
    /*
    int id=0;
    vector<vector<int>> ins(N),outs(N),ms(N);
    rep(i,0,N){
        rep(j,0,P) ins[i].push_back(id++);
        rep(j,0,P) outs[i].push_back(id++);
        rep(j,0,2) ms[i].push_back(id++);
    }
    int s=id++,t=id++;
    max_flow mf(id);
    */
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
