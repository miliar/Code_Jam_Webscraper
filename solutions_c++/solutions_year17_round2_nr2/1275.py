#include <bits/stdc++.h>

using namespace std;
using ll = long long;

#define gc getchar
int getint() { unsigned int c; int x = 0; while (((c = gc()) - '0') >= 10) { if (c == '-') return -getint(); if (!~c) exit(0); } do { x = (x << 3) + (x << 1) + (c - '0'); } while (((c = gc()) - '0') < 10); return x; }
int getstr(char *s) { int c, n = 0; while ((c = gc()) <= ' ') { if (!~c) exit(0); } do { s[n++] = c; } while ((c = gc()) > ' ' ); s[n] = 0; return n; }
template<class T> inline bool chmin(T &a, T b) { return a > b ? a = b, 1 : 0; }
template<class T> inline bool chmax(T &a, T b) { return a < b ? a = b, 1 : 0; }

char buf[1 << 10];

struct Parameters {
    int n;
    int colors[6];
    string res;
    //-- read ----------------------------------------------------------------//
    void get() {
        n = getint();
        for (auto i = 0; i < 6; ++i) colors[i] = getint();
    }

    //-- write ---------------------------------------------------------------//
    void put(int test_case) {
        printf("Case #%d: ", test_case);
        if (res.empty()) puts("IMPOSSIBLE");
        else cout << res << endl;
    }
};

mutex mtx;
struct CaseSolver {
    int n;
    int colors[6];
    string res;
    void solve(Parameters& par) {
        n = par.n;
        for (auto i = 0; i < 6; ++i) colors[i] = par.colors[i];
        res = "";

        // R Y B
        int cs[3] = {colors[0], colors[2], colors[4]};

        int maxn = n / 2;
        int maxp = max({cs[0], cs[1], cs[2]});
        if (maxp > maxn) {
            return;
        }
        int who = -1;
        if (maxp == cs[0]) res += 'R', cs[0]--, who = 0;
        else if (maxp == cs[1]) res += 'Y', cs[1]--, who = 1;
        else if (maxp == cs[2]) res += 'B', cs[2]--, who = 2;
        for (auto i = 1; i < n; ++i) {
            if (~i & 1) {
                if (cs[who]) {
                    res += "RYB"[who];
                    cs[who]--;
                    continue;
                }
            }
            if (res.back() == 'R') {
                if (cs[1] > cs[2]) res += 'Y', cs[1]--;
                else res += 'B', cs[2]--;
            } else if (res.back() == 'Y') {
                if (cs[0] > cs[2]) res += 'R', cs[0]--;
                else res += 'B', cs[2]--;
            } else if (res.back() == 'B') {
                if (cs[0] > cs[1]) res += 'R', cs[0]--;
                else res += 'Y', cs[1]--;
            }
        }

        int t1 = 0, t2 = 0, t3 = 0;
        for (auto i = 0; i < res.size(); ++i) {
            if (res[i] == 'R') t1++;
            if (res[i] == 'Y') t2++;
            if (res[i] == 'B') t3++;
        }
        assert(res.size() == n);
        for (auto i = 0; i < res.size(); ++i) {
            if (res[i] == res[(i + 1) % res.size()]) {
                cout << "i = " << i << endl;
                cout << res << endl;
                puts("failed");
                exit(1);
            }
        }

        assert(t1 == colors[0]);
        assert(t2 == colors[2]);
        assert(t3 == colors[4]);

        par.res = res;
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
    const auto thread_count = 1;//thread::hardware_concurrency();
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
