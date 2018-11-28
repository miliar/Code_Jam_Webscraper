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

PII test(int md, int mb, int M, vector<PII>& TCS) {
    int cc[1001], pro = 0;
    priority_queue<int, vector<int>, greater<int> > ee;
    memset(cc, 0, sizeof cc);
    if (md < mb) {
        return PII(0, pro);
    }
    int prev = 1;
    for(int i = 0; i < M; i++) {
        PII p = TCS[i];
        if (p.first != prev) {
            for(int t = prev; t < p.first; t++) {
                ee.push(md - cc[t-1]);
            }
            prev = p.first;
        }
        cc[p.first]++;
        if (cc[p.first] > md) {
            cc[p.first]--;
            pro++;
            if (!ee.size() || ee.top() <= 0) {
                return PII(0, pro);
            } else {
                int k = ee.top();
                ee.pop();
                ee.push(k-1);
            }
        }
    }
    return PII(1, pro);
}

void solve() {
    int TT;
    scanf("%d", &TT);
    for(int tt = 1; tt <= TT; tt++) {
        int N, C, M, bb, pp, mb = -1;
        vector<PII> TCS;
        vector<int> BY (1001, 0);
        scanf("%d %d %d", &N, &C, &M);
        for(int i = 0; i < M; i++) {
            scanf("%d %d", &pp, &bb);
            TCS.emplace_back(PII(pp, bb));
            BY[bb]++;
        }
        for(int i = 1; i <= C; i++) {
            mb = max(mb, BY[i]);
        }
        sort(TCS.begin(), TCS.end());
        int lo = 0, hi = M+2, pro = 0;
        // cerr << tt << endl;
        while((hi - lo) > 1) {
            int md = lo + (hi - lo) / 2;
            PII p1 = test(md, mb, M, TCS);
            PII p2 = test(md+1, mb, M, TCS);
            // cerr << md << "," << p1.first << "!" << p2.first << endl;
            if (p1.first && p2.first) {
                hi = md;
                pro = p1.second;
            } else if ((!p1.first) && (!p2.first)) {
                lo = md;
            } else {
                hi = md+1;
                pro = p2.second;
                break;
            }
        }
        printf("Case #%d: %d %d\n", tt, hi, pro);
    }
}

int main() {
    // std::ios::sync_with_stdio(false);
    freopen("Bs.out", "w+", stdout);
    freopen("B-small-attempt0.in", "r", stdin);
    // freopen("input.txt", "r", stdin);
    solve();
    return 0;
}
