#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> inline bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> inline bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

const auto inf = 1 << 29;

struct Parameters {
    string in;
    int res;
    int full_hd;
    int ad;
    int hk;
    int ak;
    int b, d;

    //-- read ----------------------------------------------------------------//
    void get() {
        full_hd = getint();
        ad = getint();
        hk = getint();
        ak = getint();
        b = getint();
        d = getint();
    }

    //-- write ---------------------------------------------------------------//
    void put(int test_case) {
        printf("Case #%d: ", test_case);
        if (res >= inf) puts("IMPOSSIBLE");
        else cout << res << endl;
    }
};


ll gethash(int hd, int ad, int hk, int ak) {
    ll res = hd;
    res = res * 137LL + ad;
    res = res * 137LL + hk;
    res = res * 137LL + ak;
    return res;
}

mutex mtx;
struct CaseSolver {
    map<ll, int> vis;
    int best;
    int full_hd, b, d;

    void solve2(int hd, int ad, int hk, int ak, int turn, int cured) {
        ll hs = gethash(hd, ad, hk, ak);
        if (vis.count(hs) && vis[hs] <= turn) {
            return;
        }
        vis[hs] = turn;
        if (turn >= best) return;
        // attack
        {
            const auto nhd = hd - ak;
            const auto nhk = hk - ad;
            if (nhk <= 0) {
                best = turn + 1;
            } else {
                if (nhd > 0) solve2(nhd, ad, nhk, ak, turn + 1, 0);
            }
        }
        // buff
        {
            const auto nhd = hd - ak;
            if (nhd > 0) solve2(nhd, ad + b, hk, ak, turn + 1, 0);
        }
        // debuff
        if (ak > 0) {
            const auto nak = max(ak - d, 0);
            const auto nhd = hd - nak;
            if (nhd > 0) solve2(nhd, ad, hk, nak, turn + 1, 0);
        }
        // cure
        {
            const auto nhd = full_hd - ak;
            if (nhd > 0) solve2(nhd, ad, hk, ak, turn + 1, 1);
        }
    }

    void solve(Parameters& par) {
        vis.clear();
        best = inf;
        full_hd = par.full_hd;
        int ad = par.ad;
        int hk = par.hk;
        int ak = par.ak;
        b = par.b;
        d = par.d;
        solve2(full_hd, ad, hk, ak, 0, 0);
        par.res = best;
        return;
    }

    void set(vector<Parameters>& pars, atomic<int>& case_count) {
        auto cc = case_count++;
        if (cc >= static_cast<int>(pars.size())) return;
        {
            lock_guard<mutex> lck{mtx};
            cerr << " case : " << cc << " run in " << this_thread::get_id() << endl;
        }
        solve(pars[cc]);
        set(pars, case_count);
    }
};

int main () {
    const auto test_case = getint();
    const auto thread_count = thread::hardware_concurrency();
    cerr << "number of threads = " << thread_count << endl;
    vector<Parameters> pars(test_case);
    vector<CaseSolver> sols(thread_count);
    for (auto& p: pars) p.get();
    atomic<int> case_count{0};
    vector<thread> workers(thread_count - 1);
    for (int i = 0; i < thread_count - 1; i++) {
        workers[i] = thread(&CaseSolver::set, &sols[i], ref(pars), ref(case_count));
    }
    sols[thread_count - 1].set(pars, case_count);
    for (auto& t: workers) if (t.joinable()) t.join();
    for (auto i = 0; i < test_case; i++) pars[i].put(i + 1);
    return 0;
}
