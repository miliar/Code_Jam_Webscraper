#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> inline bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> inline bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

struct Parameters {
    int n;
    double res[111];
    double max_dists[111], speeds[111];
    double graph[111][111];
    int q, q1[111], q2[111];


    //-- read ----------------------------------------------------------------//
    void get() {
        n = getint();
        q = getint();
        for (auto i = 0; i < n; ++i) {
            max_dists[i] = getint();
            speeds[i] = getint();
        }
        for (auto i = 0; i < n; ++i) {
            for (auto j = 0; j < n; ++j) {
                graph[i][j] = getint();
            }
        }
        for (auto i = 0; i < q; ++i) {
            q1[i] = getint() - 1;
            q2[i] = getint() - 1;
        }
    }

    //-- write ---------------------------------------------------------------//
    void put(int test_case) {
        printf("Case #%d: ", test_case);
        for (auto i = 0; i < q; ++i) {
            if (i) putchar(' ');
            printf("%.10f", res[i]);
        }
        puts("");
    }
};

const double inf = 1e30;

const auto one = bitset<111>(1);

mutex mtx;
struct CaseSolver {
    int n;
    double res[111];
    double max_dists[111], speeds[111];
    double graph[111][111];
    int q, q1[111], q2[111];
    double min_time[111];
    int t = 0;
    double best;

    void solve(int u, double now, double rest, double speed, bitset<111> vis) {
        if (best > 0 && now > best) return;
        if (u == t) {
            if (best < 0) best = now;
            chmin(best, now);
            return;
        }
        for (auto v = 0; v < n; ++v) if (vis.test(v) == 0) {
            double d = graph[u][v];
            if (d < 0) continue;
            double nrest = rest - d;
            if (nrest < 0) continue;
            auto nvis = vis;
            nvis.set(v);
            // keep horse
            solve(v, now + d / speed, nrest, speed, nvis);
            // change horse
            solve(v, now + d / speed, max_dists[v], speeds[v], nvis);
        }
    }

    void solve(Parameters& par) {
        n = par.n;
        q = par.q;
        for (auto i = 0; i < n; ++i) {
            max_dists[i] = par.max_dists[i];
            speeds[i] = par.speeds[i];
        }
        for (auto i = 0; i < n; ++i) for (auto j = 0; j < n; ++j) {
            graph[i][j] = par.graph[i][j];
        }
        for (auto i = 0; i < q; ++i) q1[i] = par.q1[i], q2[i] = par.q2[i];
        for (auto qq = 0; qq < q; ++qq) {
            int s = q1[qq];
            t = q2[qq];
            best = -1.0;
            bitset<111> vis;
            vis.set(s);
            solve(s, 0.0, max_dists[s], speeds[s], vis);
            par.res[qq] = best;
        }
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
