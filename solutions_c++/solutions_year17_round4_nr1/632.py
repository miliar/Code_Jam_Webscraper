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

const int N = 100;
int dp4[N+10][N+10][N+10];
void pre() {
    rep(i, N) rep(j, N) rep(k, N) if(i|j|k) dp4[i][j][k] = 1;
    rep(i, N) rep(j, N) rep(k, N) {
        chmax(dp4[i+4][j][k], dp4[i][j][k] + 1);
        chmax(dp4[i][j+2][k], dp4[i][j][k] + 1);
        chmax(dp4[i][j][k+4], dp4[i][j][k] + 1);
        chmax(dp4[i+1][j][k+1], dp4[i][j][k] + 1);
        chmax(dp4[i+2][j+1][k], dp4[i][j][k] + 1);
        chmax(dp4[i][j+1][k+2], dp4[i][j][k] + 1);

        chmax(dp4[i][j][k+1], dp4[i][j][k]);
        chmax(dp4[i][j+1][k], dp4[i][j][k]);
        chmax(dp4[i+1][j][k], dp4[i][j][k]);
    }
}

bool solve(GCJ::Runner &gcj){
    int p, n;
    cin >> n >> p;
    vector<int> c(p);
    rep(i, n) {
        int k; cin >> k;
        ++c[k % p];
    }

    gcj.end_input();

    if(p == 3){
        int res = c[0];
        res += min(c[1], c[2]);
        int tmp = max(c[1], c[2]) - min(c[1], c[2]);
        res += (tmp + 2) / p;
        gcj << res << endl;
    } else if(p == 2) {
        int res = c[0];
        int tmp = c[1];
        res += (tmp + 1) / p;
        gcj << res << endl;
    } else {
        gcj << c[0] + dp4[c[1]][c[2]][c[3]] << endl;
    }
    return true;
}

signed main(){//{{{
    pre();
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);
    std::cout << std::fixed << std::setprecision(10);
    constexpr int max_thread = 1;

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
