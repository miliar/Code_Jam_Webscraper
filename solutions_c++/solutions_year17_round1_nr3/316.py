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
#include <cmath>
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
constexpr ll infll = ll(1e18)+9;
ll solve(ll hd, ll ad, ll hk, ll ak, ll b, ll d) {
    ll turns_to_kill = infll; { // if no cure / debuf are required, this value is the result
        int buf_count_limit = sqrt(hk) + 100;
        repeat (buf, buf_count_limit) {
            ll buffed_ad = ad + buf * b; // Buf
            setmin(turns_to_kill, buf + (hk + buffed_ad-1) / buffed_ad); // Attack
        }
    }
    ll result = infll;
    int debuf_count_limit = d == 0 ? 0 : min<int>(1000000, ak / d + 3);
    ll turns_to_debuf = 0;
    ll hd_after_debuf = hd;
    repeat (debuf, debuf_count_limit+1) {
        ll debuffed_ak = ak - debuf * d;
        if (debuffed_ak <= 0) {
            setmin(result, turns_to_debuf + turns_to_kill);
            break;
        }
        ll initial_turns_to_cure = (hd_after_debuf - 1) / debuffed_ak;
        ll turns_to_cure = (hd - 1) / debuffed_ak - 1;
        if ((turns_to_kill - 1) <= initial_turns_to_cure) {
            setmin(result, turns_to_debuf + turns_to_kill);
        } else if (turns_to_cure >= 1) {
            ll remaining_turns_to_kill = turns_to_kill - initial_turns_to_cure;
            ll cure_count = ((remaining_turns_to_kill - 1) + turns_to_cure - 1) / turns_to_cure;
            setmin(result, turns_to_debuf + turns_to_kill + cure_count);
        }
        ll next_debuffed_ak = max<ll>(0, debuffed_ak - d);
        if (hd_after_debuf <= next_debuffed_ak) {
            hd_after_debuf = hd - debuffed_ak; // Cure
            turns_to_debuf += 1;
            if (hd_after_debuf <= next_debuffed_ak) break;
        }
        hd_after_debuf -= next_debuffed_ak; // Debuf
        turns_to_debuf += 1;
    }
    return result;
}
int main() {
    int t; scanf("%d", &t);
    repeat (x,t) {
        int hd, ad, hk, ak, b, d; scanf("%d%d%d%d%d%d", &hd, &ad, &hk, &ak, &b, &d);
        ll result = solve(hd, ad, hk, ak, b, d);
        printf("Case #%d: ", x+1);
        if (result == infll) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%lld\n", result);
        }
    }
    return 0;
}
