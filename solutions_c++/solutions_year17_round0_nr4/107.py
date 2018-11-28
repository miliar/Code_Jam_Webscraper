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

template<class ...Ts> struct Zipper{//{{{
    using Key = typename std::conditional<sizeof...(Ts) == 1, typename std::tuple_element<0, std::tuple<Ts...>>::type,
          typename std::conditional<sizeof...(Ts) == 2, std::pair<typename std::tuple_element<0, std::tuple<Ts...>>::type, typename std::tuple_element<1, std::tuple<Ts..., void>>::type>,
          std::tuple<Ts...>>::type>::type;

    mutable map<Key, int> zip;
    mutable vector<Key> unzip;
    template<class It> void add(It b, It e){ while(b != e) add(*b++); }
    void add(const Ts &...ts){ this->operator()(ts...); }
    void compile(){
        int i = 0;
        for(auto &x : zip) unzip[x.second = i++] = x.first;
    }
    const Key operator[](const int &i) const { return unzip[i]; }
    int operator()(const Ts &...ts) const {
        const Key key(ts...);
        auto it = zip.find(key);
        if(it != std::end(zip)) return it->second;
        const int n = unzip.size();
        unzip.emplace_back(key);
        zip.insert(make_pair(std::move(key), n));
        return n;
    }
    int size() const { return unzip.size(); }
    int count(const Ts &...ts) const { return zip.count(Key(ts...)); }
    typename vector<Key>::const_iterator begin(){ return unzip.begin(); }
    typename vector<Key>::const_iterator end(){ return unzip.end(); }
};//}}}

struct BMatch{//{{{
    struct E{
        int src, dst;
        E(int src, int dst) : src(src), dst(dst) {}
    };
    typedef vector<E> V;
    typedef vector<V> G;
    const int L, R, n;
    vector<int> match;
    G g;
    BMatch(const int L, const int R)
        : L(L), R(R), n(L+R), match(n, -1), g(n) {
    }
    void add_edge(int src, int dst){ g[src].emplace_back(src, L + dst); }
    vector<int> visited;
    bool augment(int u){
        if(u < 0) return true;
        for(auto &e : g[u]) if(!visited[e.dst]){
            visited[e.dst] = true;
            if(augment(match[e.dst])){
                match[e.src] = e.dst;
                match[e.dst] = e.src;
                return true;
            }
        }
        return false;
    }
    int run(){
        int res = 0;
        rep(u, L) if(match[u] == -1){
            visited.assign(n, 0);
            if(augment(u)) ++res;
        }
        return res;
    }
    int operator[](int l) { return match[l] >= 0 ? match[l] - L : -1; }
    int operator()(int r) { return match[r]; }
};//}}}

bool solve(GCJ::Runner &gcj){
    int n;
    cin >> n;
    vector<vector<char>> initial(n, vector<char>(n, '.'));
    vector<vector<char>> A(n, vector<char>(n, false));
    vector<vector<char>> B(n, vector<char>(n, false));
    {
        int m;
        cin >> m;
        rep(_, m) {
            char c; cin >> c;
            int x, y; cin >> x >> y; --x; --y;
            initial[x][y] = c;
            if(c != '+') A[x][y] = true;
            if(c != 'x') B[x][y] = true;
        }
    }
    gcj.end_input();

    {   // for +
        vector<int> xs, ys;
        rep(i, n) {
            bool matched = false;
            rep(j, n) matched |= A[i][j];
            if(!matched) xs.push_back(i);
        }
        rep(j, n) {
            bool matched = false;
            rep(i, n) matched |= A[i][j];
            if(!matched) ys.push_back(j);
        }
        assert(size(xs) == size(ys));
        rep(t, size(xs)) A[xs[t]][ys[t]] = true;
    }
    {   // for *

        Zipper<int> szip, dzip;
        rep(i, n) rep(j, n) szip.add(i+j), dzip.add(i-j);

        set<int> used_s, used_d;
        rep(i, n) rep(j, n) if(B[i][j]) {
            used_s.insert(szip(i + j));
            used_d.insert(dzip(i - j));
        }
        BMatch bm(szip.size(), dzip.size());
        rep(i, n) rep(j, n) {
            if(used_s.count(szip(i+j)) || used_d.count(dzip(i-j))) continue;
            bm.add_edge(szip(i+j), dzip(i-j));
        }
        bm.run();
        rep(i, n) rep(j, n) if(bm[szip(i+j)] == dzip(i-j)){
            assert(!used_s.count(szip(i+j)) and !used_d.count(dzip(i-j)));
            B[i][j] = true;
            used_s.insert(szip(i+j));
            used_d.insert(dzip(i-j));
        }
    }
    int res = 0;
    rep(i, n) rep(j, n) res += A[i][j];
    rep(i, n) rep(j, n) res += B[i][j];
    gcj << res << ' ';
    {
        auto optimal = initial;
        rep(i, n) rep(j, n) {
            if( A[i][j] &&  B[i][j]) optimal[i][j] = 'o';
            if( A[i][j] && !B[i][j]) optimal[i][j] = 'x';
            if(!A[i][j] &&  B[i][j]) optimal[i][j] = '+';
            if(!A[i][j] && !B[i][j]) optimal[i][j] = '.';
        }
        vector<tuple<char, int, int>> update;
        rep(i, n) rep(j, n) if(initial[i][j] != optimal[i][j])
            update.emplace_back(optimal[i][j], i+1, j+1);
        gcj << update.size() << endl;
        for(auto upd : update)
            gcj << get<0>(upd) << ' ' << get<1>(upd) << ' ' << get<2>(upd) << endl;
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
