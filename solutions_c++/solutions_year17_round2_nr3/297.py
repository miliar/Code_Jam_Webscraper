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

bool solve(GCJ::Runner &gcj){
    int n, Q;
    cin >> n >> Q;
    vector<ll> hp(n), spd(n);
    rep(i, n) cin >> hp[i] >> spd[i];

    vector<vector<ll>> d(n, vector<ll>(n));
    rep(i, n) rep(j, n) cin >> d[i][j];
    rep(i, n) d[i][i] = 0;
    rep(i, n) rep(j, n) if(d[i][j] == -1) d[i][j] = 1LL<<55;
    rep(k, n) rep(i, n) rep(j, n) chmin(d[i][j], d[i][k] + d[k][j]);

    vector<int> start(Q), goal(Q);
    rep(i, Q) cin >> start[i] >> goal[i];
    rep(i, Q) --start[i], --goal[i];

    gcj.end_input();

    using R = double;
    vector<vector<R>> t(n, vector<R>(n));
    rep(i, n) rep(j, n) t[i][j] = 1E100 * (i != j);
    rep(i, n) rep(j, n) if(hp[i] >= d[i][j]) chmin(t[i][j], d[i][j] / (R)(spd[i]));
    rep(k, n) rep(i, n) rep(j, n) chmin(t[i][j], t[i][k] + t[k][j]);
    rep(q, Q) {
        if(q) gcj << ' ';
        gcj << t[start[q]][goal[q]];
    }
    gcj << endl;
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
