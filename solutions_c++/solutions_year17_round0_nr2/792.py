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

bool check(LL x) {
    string X = to_string(x);
    for(int i = 0, len = X.size(); i < len - 1; i++) {
        if (X[i] > X[i+1]) return false;
    }
    return true;
}

int T;
LL res;
string s;
void solve() {
    cin >> T;
    for(int a = 1; a <= T; a++) {
        cin >> res;
        while(!check(res)) {
            s = to_string(res);
            int l = s.size();
            for(int i = 0; i < l - 1; i++) {
                if (s[i] > s[i+1]) {
                    res -= (stoll(s.substr(i+1)) + 1);
                    break;
                }
            }
        }
        printf("Case #%d: ", a);
        cout << res << endl;
    }

}

int main() {
    // std::ios::sync_with_stdio(false);
    freopen("B-large.in", "r", stdin);
    freopen("Bl.out", "w+", stdout);
    // freopen("input.txt", "r", stdin);
    solve();
    return 0;
}
