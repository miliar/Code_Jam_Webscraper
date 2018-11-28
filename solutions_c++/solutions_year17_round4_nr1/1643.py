#ifndef _GLIBCXX_NO_ASSERT
#include <cassert>
#endif
#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

#if __cplusplus >= 201103L
#include <ccomplex>
#include <cfenv>
#include <cinttypes>
#include <cstdbool>
#include <cstdint>
#include <ctgmath>
#include <cwchar>
#include <cwctype>
#endif

// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>

#if __cplusplus >= 201103L
#include <array>
#include <atomic>
#include <chrono>
#include <condition_variable>
#include <forward_list>
#include <future>
#include <initializer_list>
#include <mutex>
#include <random>
#include <ratio>
#include <regex>
#include <scoped_allocator>
#include <system_error>
#include <thread>
#include <tuple>
#include <typeindex>
#include <type_traits>
#include <unordered_map>
#include <unordered_set>
#endif

using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
typedef pair<LL, LL> PLL;

void solve() {
    int T;
    scanf("%d", &T);
    for(int tt = 1; tt <= T; tt++) {
        int res = 0, kmin, kd, C[4], N, P, t;
        memset(C, 0, sizeof C);
        scanf("%d %d", &N, &P);
        for(int i = 0; i < N; i++) {
            scanf("%d", &t);
            C[t%P]++;
        }
        // for(int i = 0; i < P; i++) cerr << C[i] << " "; cerr << endl;
        res += C[0];
        if (P == 2) {
            res = res + (C[1] / 2) + (C[1] % 2);
        } else if (P == 3) {
            kmin = min(C[1], C[2]);
            kd = max(C[1], C[2]) - kmin;
            res = res + kmin + (kd / 3);
            if (kd % 3) res++;
        } else {
            res += (C[2] / 2);
            kmin = min(C[1], C[3]);
            kd = max(C[1], C[3]) - kmin;
            if (C[2] % 2) {
                if (kd >= 2) {
                    res++;
                    kd -= 2;
                } else {
                    res++;
                    kd = 0;
                }
            }
            if (kd) {
                res += (kd / 4);
                if (kd % 4) res++;
            }
        }
        printf("Case #%d: %d\n", tt, res);
    }

}

int main() {
    // std::ios::sync_with_stdio(false);
    freopen("As.out", "w+", stdout);
    freopen("A-small-attempt1.in", "r", stdin);
    // freopen("input.txt", "r", stdin);
    solve();
    return 0;
}
