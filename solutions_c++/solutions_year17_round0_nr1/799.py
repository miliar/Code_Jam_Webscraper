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

int T, K;
char st[1001];
string s;

void solve() {
    scanf("%d", &T);
    for(int a = 1; a <= T; a++) {
        memset(st, 0, sizeof st);
        int sta = 1;
        cin >> s >> K;
        int l = s.size(), res = 0;
        for(int i = 0; i < l; i++) {
            st[i] = s[i] == '+';
        }
        for(int i = 0; i <= l - K; i++) {
            if (!st[i]) {
                res++;
                for(int j = i; j < i + K; j++) {
                    st[j] = 1 - st[j];
                }
            }
        }
        for(int i = 0; i < l; i++) {
            if (!st[i]) sta = 0;
        }
        if (sta) printf("Case #%d: %d\n", a, res);
        else printf("Case #%d: IMPOSSIBLE\n", a);
    }

}

int main() {
    // std::ios::sync_with_stdio(false);
    freopen("A-large.in", "r", stdin);
    freopen("ALout.out", "w+", stdout);
    solve();
    return 0;
}
