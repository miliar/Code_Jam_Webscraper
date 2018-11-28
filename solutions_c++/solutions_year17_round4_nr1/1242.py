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
#include "algorithm/math/convergents.h"
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
#include "structure/container/binary_heap.h"
#include "structure/container/binary_search_tree.h"
#include "structure/container/treap.h"
#include "structure/container/rope.h"
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

int f[101][101][101][4];

int main() {
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, p; cin >> n >> p;
        int c[4] = {0,0,0,0};
        for (int i = 0; i < n; i++) {
            int g;  cin >> g;
            c[g % p]++;
        }
        int r = c[0];
        //if (p == 2) {
        //    r += (c[1] + 1) / 2;
        //} else if (p == 3) {
        //    int cc = min(c[1], c[2]);
        //    c[1] -= cc; c[2] -= cc;
        //    r += cc;
        //    r += (c[1] + c[2] + 2) / 3;
        //} else if (p == 4) {
            int c1 = c[1], c2 = c[2], c3 = c[3];
            for (int i1 = 0; i1 <= c1; i1++) {
                for (int i2 = 0; i2 <= c2; i2++) {
                    for (int i3 = 0; i3 <= c3; i3++) {
                        for (int q = 0; q < p; q++) {
                            f[i1][i2][i3][q] = -1000000;
                            f[0][0][0][0] = 0; int o;
                            o = (q + p - 1) % p; if (i1 > 0) f[i1][i2][i3][q] = max(f[i1][i2][i3][q], f[i1 - 1][i2][i3][o] + (o == 0));
                            o = (q + p - 2) % p; if (i2 > 0) f[i1][i2][i3][q] = max(f[i1][i2][i3][q], f[i1][i2 - 1][i3][o] + (o == 0));
                            o = (q + p - 3) % p; if (i3 > 0) f[i1][i2][i3][q] = max(f[i1][i2][i3][q], f[i1][i2][i3 - 1][o] + (o == 0));
                        }
                    }
                }
            }
        //}
        int r2 = 0;
        for (int q = 0; q < p; q++) {
            r2 = max(r2, f[c1][c2][c3][q]);
        }
        printf("Case #%d: %d\n", t, r2 + c[0]);
    }
    return 0;
}
