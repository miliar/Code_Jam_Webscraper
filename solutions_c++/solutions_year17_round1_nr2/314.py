#include <cstdio>
#include <vector>
#include <algorithm>
#include <array>
#include <set>
#include <map>
#include <queue>
#include <tuple>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <cassert>
#define repeat(i,n) for (int i = 0; (i) < int(n); ++(i))
#define repeat_from(i,m,n) for (int i = (m); (i) < int(n); ++(i))
#define repeat_reverse(i,n) for (int i = (n)-1; (i) >= 0; --(i))
#define repeat_from_reverse(i,m,n) for (int i = (n)-1; (i) >= int(m); --(i))
#define whole(f,x,...) ([&](decltype((x)) whole) { return (f)(begin(whole), end(whole), ## __VA_ARGS__); })(x)
#define debug(x) #x << " = " << (x) << " "
using ll = long long;
using namespace std;
template <class T> inline void setmax(T & a, T const & b) { a = max(a, b); }
template <class T> inline void setmin(T & a, T const & b) { a = min(a, b); }
template <typename X, typename T> auto vectors(X x, T a) { return vector<T>(x, a); }
template <typename X, typename Y, typename Z, typename... Zs> auto vectors(X x, Y y, Z z, Zs... zs) { auto cont = vectors(y, z, zs...); return vector<decltype(cont)>(x, cont); }
template <class T> using reversed_priority_queue = priority_queue<T, vector<T>, greater<T> >;
constexpr int inf = 1e9+7;
int solve(int n, int p, vector<int> const & required, vector<vector<int> > const & quantity) {
    auto low = vectors(n, p, int());
    auto high = vectors(n, p, int()); // [l, r]
    repeat (i,n) {
        repeat (j,p) {
            const int r = required[i];
            const int q = quantity[i][j];
            int & lo = low[i][j];
            int & hi = high[i][j];
            lo = (10*q + 11*r-1) / (11*r);
            hi = 10*q / ( 9*r);
            if (lo <= hi) {
                constexpr double eps = 1e-8;
                assert (0.9*r*lo < eps + q and q < eps + 1.1*r*lo);
                assert (0.9*r*hi < eps + q and q < eps + 1.1*r*hi);
                assert (not (0.9*r*(lo-1) < eps + q and q < eps + 1.1*r*(lo-1)));
                assert (not (0.9*r*(hi+1) < eps + q and q < eps + 1.1*r*(hi+1)));
            }
        }
    }
    reversed_priority_queue<tuple<int, bool, int> > que;
    repeat (i,n) {
        repeat (j,p) {
            if (low[i][j] <= high[i][j]) {
                que.emplace(low[i][j], false, i);
                que.emplace(high[i][j], true, i);
            }
        }
    }
    vector<int> used(n);
    vector<int> remaining(n);
    int result = 0;
    while (not que.empty()) {
        int cur_time; bool is_pop; int i; tie(cur_time, is_pop, i) = que.top(); que.pop();
        if (is_pop) {
            if (used[i]) {
                -- used[i];
            } else {
                assert (remaining[i]);
                -- remaining[i];
            }
        } else {
            ++ remaining[i];
            if (remaining[i] == 1) {
                if (*whole(min_element, remaining) >= 1) {
                    repeat (j,n) remaining[j] -= 1;
                    repeat (j,n) used[j] += 1;
                    result += 1;
                }
            }
        }
    }
    return result;
}
int main() {
    int t; scanf("%d", &t);
    repeat (x,t) {
        int n, p; scanf("%d%d", &n, &p);
        vector<int> r(n); repeat (i,n) scanf("%d", &r[i]);
        auto q = vectors(n, p, int()); repeat (i,n) repeat (j,p) scanf("%d", &q[i][j]);
        int result = solve(n, p, r, q);
        printf("Case #%d: %d\n", x+1, result);
    }
    return 0;
}
