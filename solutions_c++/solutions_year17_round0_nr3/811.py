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

int T;
LL N, K;

void solve() {
    cin >> T;
    for(int a = 1; a <= T; a++) {
        cin >> N >> K;
        LL no = N % 2, ne = 1 - no, nop, nep;
        LL k = 1;
        while(K > k) {
            if (N % 4 < 2) {
                nop = ne, nep = ne + no * 2;
            } else {
                nep = ne, nop = ne + no * 2;
            }
            no = nop;
            ne = nep;
            K -= k;
            k *= 2;
            N = (N-1) / 2;
        }
        LL r1, r2;
        if (N % 2) {
            if (ne >= K) {
                r1 = (N + 1) / 2; r2 = N / 2;
            } else {
                r1 = N / 2; r2 = N / 2;
            }
        } else {
            if (no >= K) {
                r1 = N / 2; r2 = N / 2;
            } else {
                r1 = N / 2; r2 = (N - 1) / 2;
            }

        }
        printf("Case #%d: ", a);
        cout << r1 << " " << r2 << endl;
    }
}

int main() {
    // std::ios::sync_with_stdio(false);
    freopen("C-large.in", "r", stdin);
    freopen("Cl.out", "w+", stdout);
    // freopen("input.txt", "r", stdin);
    solve();
    return 0;
}
