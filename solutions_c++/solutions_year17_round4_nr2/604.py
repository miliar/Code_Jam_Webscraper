// g++ -std=c++11 -O2 ./a.cc -lpthread -lgmp -lgmpxx
#include <bits/stdc++.h>
namespace GCJ{//{{{
    std::mutex input_mutex;
    int current_case_num = 0;

    struct Runner{
        int id; // 0-origin
        std::istream &is;
        std::ostringstream os;
        Runner(std::istream &is, const std::ostream &fmt) : id(-1), is(is){
            input_mutex.lock();
            id = current_case_num++;
            os.copyfmt(fmt);
        }

        void end_input(){
            input_mutex.unlock();
        }
        std::string get_result() const { return os.str(); }

        template<class T>
            Runner &operator<<(const T &val){
                os << val;
                return *this;
            }
        Runner &operator<<(std::ostream &(*pf)(std::ostream &)){
            os << pf;
            return *this;
        }
    };
}//}}}

#include <gmpxx.h>
using ZZ = mpz_class;
using QQ = mpq_class;

#define all(x) begin(x),end(x)
#define rall(x) (x).rbegin(),(x).rend()
#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define rrep(i,n) for(int i=(int)(n)-1;i>=0;--i)
#define repsz(i,v) rep(i,(v).size())
#define aur auto&
#define bit(n) (1LL<<(n))
#define eb emplace_back
#define mt make_tuple
#define fst first
#define snd second
using namespace std;
typedef long long ll;
//#define int long long
template<class C>int size(const C &c){ return c.size(); }
template<class T,class ...U>bool chmin(T&a, const U&...bs){const T b(bs...);if(a<=b)return false;a=b;return true;}
template<class T,class ...U>bool chmax(T&a, const U&...bs){const T b(bs...);if(a>=b)return false;a=b;return true;}


typedef ll Flow;
typedef ll Cost;
static const Cost INF = numeric_limits<Cost>::max() / 10;
struct MinCostFlow{//{{{
    struct E{
        int src, dst;
        Flow cap, flow;
        Cost cost;
        int rev;
        E(int s, int d, Flow cap, Cost cos, int r)
            : src(s), dst(d), cap(cap), flow(0), cost(cos), rev(r) {}
    };
    typedef vector<E> V;
    typedef vector<V> G;
    int n;
    G g;
    vector<Flow> b;
    MinCostFlow(int _n) : n(_n), g(n), b(n) {}

    void add_edge(int src, int dst, Flow l, Flow u, Cost cos){//{{{
        int i = size(g[src]), j = src == dst ? i+1 : size(g[dst]);
        assert(l <= u);
        g[src].eb(src, dst, u, cos, j);
        g[dst].eb(dst, src,-l,-cos, i);
    }//}}}
    void add_undirected_edge(int src, int dst, Flow cap, Cost cost){//{{{
        add_edge(src, dst, 0, cap, cost);
        add_edge(dst, src, 0, cap, cost);
    }//}}}
    void add_src(int v, Flow f){ b[v] += f; }
    void add_dst(int v, Flow f){ b[v] -= f; }

    vector<Cost> h, d;
    vector<pair<int, int> > par;

    inline Flow residue(E& e){ return e.cap - e.flow; }
    inline Cost rcost(E& e){ return e.cost + h[e.src] - h[e.dst]; }
    inline Cost add_flow(E& e, Flow f){//{{{
        e.flow += f;
        g[e.dst][e.rev].flow -= f;
        b[e.src] -= f; b[e.dst] += f;
        return e.cost * f;
    }//}}}
    // b は破壊する.
    pair<bool, Cost> run(){//{{{
        pair<bool, Cost> res(true, 0);
        h.assign(n, 0);
        rep(i, n) rep(j, g[i].size()){
            E& e = g[i][j];
            if(e.cost < 0 || residue(e) < 0) res.second += add_flow(e, residue(e));
        }
        for(bool cont = true; cont; ){
            cont = false;
            d.assign(n, INF); par.assign(n, make_pair(-1, -1));
            priority_queue<pair<Cost, int>, vector<pair<Cost, int>>, greater<pair<Cost, int>>> pq;
            rep(i, n) if(b[i] > 0) pq.emplace(d[i]=0, i);
            while(!pq.empty()){
                int i = pq.top().second;
                Cost c = pq.top().first;
                pq.pop();
                if(d[i] < c) continue;
                rep(j, g[i].size()) if(residue(g[i][j]) > 0){
                    E &e = g[i][j];
                    Cost nc = c + rcost(e);
                    if(nc >= d[e.dst]) continue;
                    par[e.dst] = make_pair(e.src, j);
                    pq.emplace(d[e.dst] = nc, e.dst);
                }
            }
            rep(t, n) if(b[t]<0 && d[t]<INF){
                Flow f = -b[t];
                int s;
                for(s = t; par[s].second != -1; s = par[s].first){
                    E &e = g[par[s].first][par[s].second];
                    f = min(f, residue(e));
                }
                f = min(f, b[s]);
                if(f <= 0) continue;
                cont = true;
                for(s = t; par[s].second != -1; s = par[s].first){
                    E &e = g[par[s].first][par[s].second];
                    res.second += add_flow(e, f);
                    if(residue(e) <= 0) par[s].second = -1;
                }
            }
            rep(i, n) if(d[i] < INF) h[i] += d[i];
        }
        rep(i, n) if(b[i] != 0) res.first = false;
        return res;
    }//}}}
};//}}}

bool solve(GCJ::Runner &gcj){
    int N, C, M; cin >> N >> C >> M;

    vector<int> x, y;
    rep(_, M){
        int p, b; cin >> p >> b; --p; --b;
        (b ? y : x).emplace_back(p);
    }

    gcj.end_input();

    ll inf = 10000000;
    MinCostFlow mcf(2*M);
    int a = size(x), b = size(y);
    vector<int> lx(a), ly(b), rx(a), ry(b);
    rep(i, a) lx[i] = i;
    rep(i, b) ly[i] = a + i;
    rep(i, a) rx[i] = a + b + i;
    rep(i, b) ry[i] = i + a + b + a;

    rep(i, a) rep(ii, a) mcf.add_edge(lx[i], rx[ii], 0, 1, inf);
    rep(j, b) rep(jj, b) mcf.add_edge(ly[j], ry[jj], 0, 1, inf);

    rep(i, a) rep(j, b) mcf.add_edge(ly[j], rx[i], 0, 1, 0);
    rep(i, a) rep(j, b) {
        if(x[i] != y[j]) {
            mcf.add_edge(lx[i], ry[j], 0, 1, inf);
        }else if(x[i] != 0) {
            mcf.add_edge(lx[i], ry[j], 0, 1, inf + 1);
        }
    }
    rep(i, a) mcf.add_src(lx[i], 1);
    rep(j, b) mcf.add_src(ly[j], 1);
    rep(i, a) mcf.add_dst(rx[i], 1);
    rep(j, b) mcf.add_dst(ry[j], 1);

    auto ret = mcf.run();
    assert(ret.first);
    gcj << ret.second/inf << ' ' << ret.second%inf << endl;
    return true;
}

signed main(){//{{{
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);
    std::cout << std::fixed << std::setprecision(10);
    constexpr int max_thread = 4;

    const int T = []{
        std::string s;
        std::getline(std::cin, s);
        return std::stoi(s);
    }();

    std::mutex job_mutex;
    int job_count = 0;
    auto get_job = [&job_mutex, &job_count, &T]{
        std::lock_guard<std::mutex> job_lock(job_mutex);
        return job_count++ < T;
    };
    std::vector<std::promise<std::string>> results(T);

    auto runner = [&job_mutex, &get_job, &results]{
        while(get_job()){
            GCJ::Runner gcj(std::cin, std::cout);
            job_mutex.unlock();
            solve(gcj);
            // cout << "CASE #" << gcj.id << ": " << endl << gcj.get_result() << endl;
            results[gcj.id].set_value(gcj.get_result());
        }
    };
    std::vector<std::thread> threads(max_thread);
    for(auto &th : threads) th = std::thread(runner);
    for(int i = 0; i < T; ++i){
        std::future<std::string> res = results[i].get_future();
        std::cout << "Case #" << i+1 << ": " << res.get() << std::flush;
    }
    for(auto &th : threads) th.join();
    return 0;
}//}}}
// vim:set foldmethod=marker commentstring=//%s:
