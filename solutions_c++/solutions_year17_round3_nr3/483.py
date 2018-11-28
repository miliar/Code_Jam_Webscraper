#define _USE_MATH_DEFINES
#define _CRT_SECURE_NO_DEPRECATE
#define _SCL_SECURE_NO_WARNINGS

#pragma warning(disable:4146)  // unary minus operator applied to unsigned type, result still unsigned
#pragma warning(disable:4800)  // 'int' : forcing value to bool 'true' or 'false' (performance warning)

//#define _CRT_RAND_S

//#include <windows.h>
//#include <tchar.h>
//#include <atlbase.h>
//#include <winerror.h>

//#define BOOST_FILESYSTEM_NO_DEPRECATED
//#include <boost/filesystem.hpp>
//#include <boost/filesystem/fstream.hpp>
//#include <boost/regex.hpp>
//#include <boost/algorithm/string.hpp>

#include <intrin.h>
#pragma intrinsic(__rdtsc)

#include <type_traits>
#include <stdint.h>
#include <stdexcept>
#include <climits>
#include <ctime>
#include <chrono>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <map>
#include <set>
#include <list>
#include <queue>
#include <deque>
#include <string>
#include <bitset>
#include <vector>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

#include <thread>
#include <mutex>
#include <atomic>
#include <condition_variable>
#include <ppl.h>

#include <unordered_set>
#include <unordered_map>

#include "concurrency/concurrency.h"
#include "algorithm/collections/collections.h"
#include "algorithm/hash/polynomial_hash.h"
#include "algorithm/hash/std_tuple_hash.h"
#include "algorithm/graph/graph.h"
#include "algorithm/graph/iterative_dfs.h"
#include "algorithm/graph/topological_sort.h"
#include "algorithm/graph/tarjan_scc.h"
#include "algorithm/graph/chain_decomposition.h"
#include "algorithm/graph/chromatic_polynomial.h"
#include "algorithm/graph/transitive_closure.h"
#include "algorithm/graph/floyd_warshall.h"
#include "algorithm/graph/dijkstra.h"
#include "algorithm/graph/dinic_flow.h"
#include "algorithm/graph/push_relabel_flow.h"
#include "algorithm/graph/bipartite_matching.h"
#include "algorithm/graph/lowest_common_ancestor.h"
#include "algorithm/graph/heavy_light_decomposition.h"
#include "algorithm/math/base.h"
#include "algorithm/math/gmp_helpers.h"
#include "algorithm/math/bits.h"
#include "algorithm/math/convolutions.h"
#include "algorithm/math/comb_primes.h"
#include "algorithm/math/comb_mod_pp.h"
#include "algorithm/math/combinatorics.h"
#include "algorithm/math/counting.h"
#include "algorithm/math/fft.h"
#include "algorithm/math/fractions.h"
#include "algorithm/math/modulos.h"
#include "algorithm/math/pell.h"
#include "algorithm/math/triples.h"
#include "algorithm/math/polynom_mod.h"
#include "algorithm/math/polynoms.h"
#include "algorithm/math/primes.h"
#include "algorithm/math/prime_counting.h"
#include "algorithm/math/prime_pi.h"
#include "algorithm/math/ranges.h"
#include "algorithm/math/recurrence.h"
#include "algorithm/math/reduce.h"
#include "algorithm/math/sequences.h"
#include "algorithm/math/sums.h"
#include "algorithm/math/divisor_sums.h"
#include "algorithm/random/xorshift.h"
#include "algorithm/search/binary_search.h"
#include "algorithm/search/kmp_search.h"
#include "structure/math/complex.h"
#include "structure/math/fenwick_tree.h"
#include "structure/math/fraction.h"
#include "structure/math/galois_field_2.h"
#include "structure/math/matrix.h"
#include "structure/math/modulo.h"
#include "structure/math/nimber.h"
#include "structure/math/permutation.h"
#include "structure/math/polynom.h"
#include "structure/math/prime_holder.h"
#include "structure/math/quadratic.h"
#include "structure/math/series.h"
#include "structure/math/vector2d.h"
#include "structure/math/vector3d.h"
#include "structure/math/vectorNd.h"
#include "structure/container/bit_vector.h"
#include "structure/container/lohi_map.h"
#include "structure/container/sqrt_map.h"
#include "structure/container/segment_tree.h"
#include "structure/container/lazy_segment_tree.h"
#include "structure/container/palindrome_tree.h"
#include "structure/container/aho_corasick_trie.h"
#include "structure/container/range_minimum_query.h"
#include "structure/container/suffix_array.h"
#include "structure/graph/disjoint_set.h"
#include "io/fast_io.h"
#include "io/reader.h"
#include "io/writer.h"
#include "io/iostream_overloads.h"

using namespace std;
using namespace tr1;
using namespace chrono;
using namespace concurrency;

using namespace altruct::math;
using namespace altruct::collections;
using namespace altruct::container;
using namespace altruct::concurrency;
using namespace altruct::graph;
using namespace altruct::hash;
using namespace altruct::search;
using namespace altruct::io;
using namespace altruct::random;

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, int> pli;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef long double ld;

typedef fraction<ll> frac;
typedef moduloX<int> modx;
typedef modulo<int, 1000000007, modulo_storage::CONSTANT> mod;
typedef modulo<int, 1000000006, modulo_storage::CONSTANT> mode;
//typedef modulo<int, 1000000000, modulo_storage::CONSTANT> mod;
//typedef modulo<int, 400000000, modulo_storage::CONSTANT> mode;
typedef polynom<mod> poly;
typedef moduloX<poly> polymod;
//typedef series<mod, 10000+1> ser;
typedef series<mod, 500 + 1> ser;
typedef permutation<int> perm;
typedef vector2d<double, int> pnt2;
typedef vector3d<double> pnt3;
typedef altruct::math::complex<int> gaussian;
typedef nimber<int> nim;
//typedef polynomial_hash<2, int64_t> phash;
//template<> int64_t phash::M[2] = { 758986603, 1000000007 };
//template<> int64_t phash::B[2] = { 36759071, 32547971 };
//template<> int64_t phash::BI[2] = { 366621061, 624567078 };
typedef polynomial_hash1<758986603, 36759071, 366621061> phash;

// uses my own open source library: https://github.com/plamenko/altruct

// altruct::chrono

namespace x {
    struct rdtsc_clock {
        typedef unsigned long long rep;
        typedef std::ratio<1, 2666666666> period; // My machine is 2.67 GHz
        typedef std::chrono::duration<rep, period> duration;
        typedef std::chrono::time_point<rdtsc_clock> time_point;
        static const bool is_steady = true;
        static time_point now() { return time_point(duration(__rdtsc())); }
    };
} // x

namespace x {
    typedef rdtsc_clock clock;
    //typedef std::chrono::high_resolution_clock clock;
    typedef std::chrono::duration<double, typename clock::period> duration;
    duration since(clock::time_point t0) { return duration(clock::now() - t0); }
} // x

template <class clock>
void test_empty_loop() {
    // Define real time units
    typedef std::chrono::duration<unsigned long long, std::pico> picoseconds;
    typedef std::chrono::nanoseconds nanoseconds;
    // Define double-based unit of clock tick
    typedef std::chrono::duration<double, typename clock::period> Cycle;
    using std::chrono::duration_cast;
    const int N = 100000000;
    // Do it
    auto t0 = clock::now();
    for (volatile int j = 0; j < N; ++j);
    auto t1 = clock::now();
    // Get the clock ticks per iteration
    auto ticks_per_iter = Cycle(t1 - t0) / N;
    std::cout << ticks_per_iter.count() << " clock ticks per iteration\n";
    // Convert to real time units
    std::cout << duration_cast<nanoseconds>(ticks_per_iter).count() << "ns per iteration\n";
    std::cout << duration_cast<picoseconds>(ticks_per_iter).count() << "ps per iteration\n";
}

int main_clock() {
    std::cout << "\nUsing rdtsc:\n";
    test_empty_loop<x::rdtsc_clock>();

    std::cout << "\nUsing std::chrono::high_resolution_clock:\n";
    test_empty_loop<std::chrono::high_resolution_clock>();

    std::cout << "\nUsing std::chrono::system_clock:\n";
    test_empty_loop<std::chrono::system_clock>();
    return 0;
}



int main_max_flow_perf_test() {
    xorshift_64star rnd(12345);
    for (int n = 0; n <= 1000; n += 10) {
        if (n == 0) continue;
        //int iter_goal = sqT(n); // all pairs
        int iter_goal = sqT(n) / sqT(ilog2(uint32_t(n))); // fewer pairs

        auto gen_cap = [&](){ return int(rnd.next() % 1000 + 1000); }; // random capacity
        //auto gen_cap = [&](){ return 1; }; // unit capacity
        
        vector<vector<int>> cap(n, vector<int>(n));
        int m_actual = 0;
        if (false) { // random
            int m_goal = n * n; // dense E=V^2
            //int m_goal = int(pow(n, 1.5)); // dense E=V^1.5
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (rnd.next() % (n * n) >= m_goal) continue;
                    m_actual++;
                    cap[i][j] = gen_cap();
                }
            }
        }
        if (true) { // grid
            int q = isqrt(n);
            for (int i = 0; i < n; i++) {
                //vector<pii> vd{ { -1, 0 }, { +1, 0 }, { 0, -1 }, { 0, +1 } }; // 4-grid
                vector<pii> vd{ { -1, 0 }, { +1, 0 }, { 0, -1 }, { 0, +1 }, { -1, -1 }, { +1, +1 }, { +1, -1 }, { -1, +1 } }; // 8-grid
                for (auto d : vd) {
                    int y = i / q, x = i % q;
                    int j = (y + d.first) * q + (x + d.second);
                    if (j < 0 || j >= n) continue;
                    m_actual++;
                    cap[i][j] = gen_cap();
                }
            }
        }
        if (false) { // bipartite
            int h = n / 2;
            for (int i = 1; i < h; i++) {
                m_actual++;
                cap[0][i] = gen_cap();
                for (int j = h; j < n - 1; j++) {
                    m_actual++;
                    cap[i][j] = gen_cap();
                }
            }
            for (int j = h; j < n - 1; j++) {
                m_actual++;
                cap[j][n-1] = gen_cap();
            }
        }
        //cerr << cap << endl;

        //auto T0 = clock();
        auto T0 = x::clock::now();
        //dinic_flow<int> d(cap, 1000000);
        push_relabel_flow<int> d(cap, 1000000);
        int r = 0, iter = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (rnd.next() % (n * n) >= iter_goal) continue;
                r += d.calc_max_flow(i, j); // all-pairs
                //r += d.calc_max_flow(0, n-1); // source-sink only
                iter++;
            }
        }
        //auto dT = double(clock() - T0) / CLOCKS_PER_SEC;
        auto dT = duration_cast<duration<double>>(x::since(T0)).count();
        printf("%d %d %d %0.3lf ms %0.3f s  %x\n", n, m_actual, iter, dT * 1e3 / iter, dT, r);
    }
    return 0;
}


int main_SPOJ_FASTFLOW() {
    int n, m; cin >> n >> m;
    vector<vector<int64_t>> cap(n, vector<int64_t>(n, 0));
    for (int i = 0; i < m; i++) {
        int u, v; cin >> u >> v; --u, --v;
        int64_t c; cin >> c; cap[u][v] += c; cap[v][u] += c;
    }
    dinic_flow<int64_t> d(cap);
    cout << d.calc_max_flow(0, n - 1) << endl;
    return 0;
}


int main_flow() {
    //return main_max_flow_perf_test();
    //return main_SPOJ_FASTFLOW();
    return 0;
}






//// finds the longest path in a DAG
//vector<int> dist(nodes.size());
//for (int i : topo) {
//    for (const edge& e : adjl[i]) {
//        dist[e.i] = max(dist[e.i], dist[i] + e.score);
//    }
//}


int main7_0() {
    int n; cin >> n;
    vector<int64_t> w(n);
    for (auto& e : w) {
        cin >> e;
    }
    graph<edge> g(n);
    for (int i = 0; i < n - 1; i++) {
        int u, v; cin >> u >> v; --u, --v;
        g.add_edge(u, v);
        g.add_edge(v, u);
    }
    // this solves a different problem where w[i] is weight for i-th engineer, and not a weight for a path of length i :(
    //vector<int> par(n, -1);
    //vector<int> lev(n);
    //vector<int> top;
    //int64_t S0 = 0, S1 = 0;
    //iterative_dfs(g, [&](int root, int parent, int node, int depth) {
    //    if (node != -1) {
    //        par[node] = parent;
    //        lev[node] = depth;
    //        S0 += w[node];
    //        S1 += w[node] * lev[node];
    //    } else {
    //        top.push_back(parent);
    //    }
    //    return true;
    //});
    //vector<int64_t> s(n);
    //for (int u : top) { // bottom-up pass
    //    s[u] = w[u]; // add self
    //    for (auto v : g[u]) s[u] += s[v.v]; // add children
    //}
    //reverse(top.begin(), top.end());
    //vector<int64_t> z(n);
    //for (int u : top) { // top-down pass
    //    if (par[u] != -1) z[u] = z[par[u]] + s[u];
    //}
    //for (int j = 0; j < n; j++) {
    //    cout << (S1 + lev[j] * S0 - 2 * z[j]) << endl;
    //}
    return 0;
}

auto petersen_graph = [&]() {
    graph<edge> g(10);
    vector<full_edge> ve{
        { 0, 1 }, { 1, 2 }, { 2, 3 }, { 3, 4 }, { 4, 0 },
        { 0, 5 }, { 1, 6 }, { 2, 7 }, { 3, 8 }, { 4, 9 },
        { 5, 7 }, { 6, 8 }, { 7, 9 }, { 8, 5 }, { 9, 6 },
    };
    for (auto e : ve) g.add_edge2(e.u, e.v);
    return g;
};

int main_g() {
    auto gp = petersen_graph();
    auto p = chromatic_polynomial(gp, 1);
    cout << p << endl;
    return 0;
}



const double PI = 3.1415926535897932384626433832795;


int main_A() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, k; cin >> n >> k;
        vector<pair<double, double>> rh(n);
        for (int i = 0; i < n; i++) {
            cin >> rh[i].first >> rh[i].second;
        }
        sort(rh.begin(), rh.end());
        reverse(rh.begin(), rh.end());
        vector<vector<double>> f(n + 1, vector<double>(k + 1, 0)); // [n+1][k+1]
        for (int i = 1; i <= n; i++) {
            auto t = rh[i - 1];
            f[i][1] = max(
                f[i - 1][1], // don't take it
                f[i - 1][0] + t.first * (t.first + t.second * 2) * PI); // take it (the first one)
            for (int j = 2; j <= k; j++) {
                f[i][j] = max(
                    f[i - 1][j], // don't take it
                    f[i - 1][j - 1] + t.first * t.second * 2 * PI); // take it
            }
        }
        //cout << "Case #" << t << ": " << setprecision(15) << f[n][k] << endl;
        printf("Case #%d: %.15lf\n", t, f[n][k]);
    }
    return 0;
}

const int SZ = 24 * 60;
int f[SZ + 1][SZ / 2 + 1][2][2] = {}; // [time_slot][minutes_used_by_1][last_person_at_previous_slot][person_at_the_end_of_the_previous_day]

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, k; cin >> n >> k;
        double U; cin >> U;
        vector<double> p(n);
        for (int i = 0; i < n; i++) {
            cin >> p[i];
        }
        sort(p.begin(), p.end());

        // u[i] == (p[0] + ... + p[n-1] + U) / n - p[i]
        
        vector<double> u(n);
        for (int m = n; m > 0; m--) {
            int m0 = m;
            double s = U;
            for (int i = 0; i < m; i++) {
                s += p[i];
            }
            for (int i = 0; i < m; i++) {
                u[i] = s / m - p[i];
            }
            if (u[m - 1] >= 0) break;
            u[m - 1] = 0;
        }
        double P = 1;
        for (int i = 0; i < n; i++) {
            P *= p[i] + u[i];
        }
        printf("Case #%d: %.15lf\n", t, P);
    }
    return 0;
}
