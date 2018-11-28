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

// usage: vec_n<double, 3>::type hoge; auto dp = make_vec<double, 3>(n,n,n,0.0);
template<class T,size_t n>struct vec_n{//{{{
    typedef std::vector<typename vec_n<T,n-1>::type> type;
    template<class...S> static type init(const size_t&s,const S&...ss){
        return type(s,vec_n<T,n-1>::init(ss...));}
};
template<class T>struct vec_n<T,0>{
    typedef T type;
    static type init(){return type();}
    static type init(const type&x){return x;}
};
template<class T,size_t n,class...S>
typename vec_n<T,n>::type make_vec(const S&...s){return vec_n<T,n>::init(s...);}//}}}

bool solve(GCJ::Runner &gcj){
    int r, c; cin >> r >> c;
    vector<string> in(r);
    rep(i, r) cin >> in[i];

    gcj.end_input();

    vector<vector<vector<vector<string>>>> dp = make_vec<string, 4>(1<<r, 1<<r, 1<<r, 0);
    vector<vector<vector<vector<string>>>> qb = make_vec<string, 4>(1<<r, 1<<r, 1<<r, 0);

    dp[0][0][0] = vector<string>(r, "");
    rep(j, c){
        rep(A, 1<<r) rep(NG, 1<<r) rep(NEED, 1<<r){
            if(dp[A][NG][NEED].empty()) continue;

            // Beam doesn't break turret.
            if([&](){
                rep(i, r) if(in[i][j] == '|' or in[i][j] == '-') if(A>>i&1) return true;
                return false;
            }()) continue;

            rep(B, 1<<r) {//{{{
                auto nex = dp[A][NG][NEED];
                int mask = 0;
                int ngmask = 0;
                rep(i, r) {
                    if(in[i][j] == '.') {
                        mask |= (A>>i&1)<<i;
                        ngmask |= (NG>>i&1)<<i;
                        nex[i] += '.';
                    }else if(in[i][j] == '#') {
                        nex[i] += '#';
                    }else{
                        ngmask |= 1<<i;
                        assert(!(A>>i&1));
                        if(B>>i&1) nex[i] += '-';
                        else nex[i] += '|';
                    }
                }
                int need = 0;
                bool ok = true;

                rep(i, r) if(NEED>>i&1) if(nex[i][j] == '#') ok = false;
                rep(i, r) if(NEED>>i&1) if(nex[i][j] == '|') ok = false;
                rep(i, r) if(NEED>>i&1) if(nex[i][j] == '.') need |= 1<<i;

                rep(i, r) if(NG>>i&1) if(nex[i][j] == '-') ok = false;
                rep(i, r) if(nex[i][j] == '|' or nex[i][j] == '-') {
                    for(int k = i+1; k < r and nex[k][j] != '#'; ++k)
                        if(nex[k][j] == '|') ok = false;
                    for(int k = i-1; k >=0 and nex[k][j] != '#'; --k)
                        if(nex[k][j] == '|') ok = false;
                }
                rep(i, r) if(nex[i][j] == '.'){
                    bool has_beam = mask>>i&1;
                    for(int k = i+1; k < r and nex[k][j] != '#'; ++k)
                        if(nex[k][j] == '|') has_beam = true;
                    for(int k = i-1; k >=0 and nex[k][j] != '#'; --k)
                        if(nex[k][j] == '|') has_beam = true;
                    if(!has_beam) need |= 1<<i;
                }
                rep(k, r) if(nex[k][j] == '-') mask |= 1<<k;
                if(!ok) continue;
                // cout << mask << ' ' << need << endl;
                // rep(x, r) cout << nex[x] << endl; cout << endl;
                qb[mask][ngmask][need] = nex;
            }//}}}
        }
        dp = qb;
        qb = make_vec<string, 4>(1<<r, 1<<r, 1<<r, 0);
    }
    vector<string> res;
    for(auto &a : dp) for(auto &b : a) if(!b[0].empty()) res = b[0];
    if(res.empty()){
        gcj << "IMPOSSIBLE" << endl;
    }else{
        gcj << "POSSIBLE" << endl;
        rep(i, r) gcj << res[i] << endl;
    }
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
