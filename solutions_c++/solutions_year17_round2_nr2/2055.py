#define _USE_MATH_DEFINES

#include <bits/stdc++.h>
using namespace std;
using i32 = int; using i64 = long long int; using f64 = double; using str = string;
template <typename T> using vec = vector<T>;
template <typename T> using heap = priority_queue<T, vec<T>, greater<T>>;
#define times(n, i) for (i32 i = 0; i < (n); ++i)
#define range(a, b, i) for (i32 i = (a); i < (b); ++i)
#define upto(a, b, i) for (i32 i = (a); i <= (b); ++i)
#define downto(a, b, i) for (i32 i = (a); i >= (b); --i)
#define all(xs) (xs).begin(), (xs).end()
#define sortall(xs) sort(all(xs))
#define reverseall(xs) reverse(all(xs))
#define uniqueall(xs) (xs).erase(unique(all(xs)), (xs).end())
#define even(x) (((x) & 1) == 0)
#define odd(x) (((x) & 1) == 1)
#define head(xs) *(xs).begin()
#define last(xs) *(xs).rbegin()
#define append emplace_back
#define findge lower_bound
#define findgt upper_bound
const i64 MOD = 1000000007;
const f64 EPS = 1e-10;

i64 t;
//
//str rec(char h, char l, i64 c, i64 r, i64 o, i64 y, i64 g, i64 b, i64 v) {
//    str s;
//    i64 n = r + o + y + g + b + v;
//    if (r > 0 && (l != 'R' && l != 'O' && l != 'V') && (n > 1 || (n == 1 && h != 'R' && h != 'O' && h != 'V'))) {
//        if (c == 0) h = 'R';
//        s = rec(h, 'R', c+1, r - 1, o, y, g, b, v);
//        if (s != "ERR")
//            return "R" + s;
//    }
//    if (o > 0 && (l != 'O' && l != 'R' && l != 'Y') && (n > 1 || (n == 1 && h != 'O' && h != 'R' && h != 'Y'))) {
//        if (c == 0) h = 'O';
//        s = rec(h, 'O', c + 1, r, o - 1, y, g, b, v);
//        if (s != "ERR")
//            return "O" + s;
//    }
//    if (y > 0 && (l != 'Y' && l != 'O' && l != 'G') && (n > 1 || (n == 1 && h != 'Y' && h != 'O' && h != 'G'))) {
//        if (c == 0) h = 'Y';
//        s = rec(h, 'Y', c + 1, r, o, y - 1, g, b, v);
//        if (s != "ERR")
//            return "Y" + s;
//    }
//    if (g > 0 && (l != 'G' && l != 'Y' && l != 'B') && (n > 1 || (n == 1 && h != 'G' && h != 'Y' && h != 'B'))) {
//        if (c == 0) h = 'G';
//        s = rec(h, 'G', c + 1, r, o, y, g - 1, b, v);
//        if (s != "ERR")
//            return "G" + s;
//    }
//    if (b > 0 && (l != 'B' && l != 'G' && l != 'V') && (n > 1 || (n == 1 && h != 'B' && h != 'G' && h != 'V'))) {
//        if (c == 0) h = 'B';
//        s = rec(h, 'B', c + 1, r, o, y, g, b - 1, v);
//        if (s != "ERR")
//            return "B" + s;
//    }
//    if (v > 0 && (l != 'V' && l != 'R' && l != 'B') && (n > 1 || (n == 1 && h != 'V' && h != 'R' && h != 'B'))) {
//        if (c == 0) h = 'V';
//        s = rec(h, 'V', c + 1, r, o, y, g, b, v - 1);
//        if (s != "ERR")
//            return "V" + s;
//    }
//    if (n == 0) {
//        return "";
//    }
//    return "ERR";
//}
//
//bool valid(i64 n, i64 r, i64 o, i64 y, i64 g, i64 b, i64 v) {
//    if (2 * (r + o) > n) return false;
//    if (2 * (r + v) > n) return false;
//    if (2 * (o + v) > n) return false;
//    if (2 * (r + o + v) > n) return false;
//    if (2 * (y + o) > n) return false;
//    if (2 * (y + g) > n) return false;
//    if (2 * (y + o + g) > n) return false;
//    if (2 * (b + g) > n) return false;
//    if (2 * (b + v) > n) return false;
//    if (2 * (b + g + v) > n) return false;
//    if (o == 0 && g == 0 && v == 0) {
//        return max(r, max(y, b)) * 2 <= n;
//    }
//    return true;
//}

void solve(i64 case_num) {
    i64 n, r, o, y, g, b, v; cin >> n >> r >> o >> y >> g >> b >> v;
    vec<pair<i64, char>>s;
    s.append(make_pair(r, 'R'));
    s.append(make_pair(y, 'Y'));
    s.append(make_pair(b, 'B'));
    sortall(s);
    i64 d = s[2].first - s[1].first;
    i64 c = s[0].first - d;
    str ans = "";
    if (c < 0) {
        ans = "ERR";
    }
    else {
        if (odd(c))
            ans += s[0].second;
        times(c/2, i) {
            ans += s[1].second;
            ans += s[0].second;
        }
        times(s[1].first - c / 2, i) {
            ans += s[1].second;
            ans += s[2].second;
        }
        times(s[0].first - (c+1) / 2, i) {
            ans += s[0].second;
            ans += s[2].second;
        }
    }
    cout << "Case #" << case_num << ": ";
    cout << (ans == "ERR" ? "IMPOSSIBLE" : ans) << endl;
}

i32 main()
{
    cin >> t;
    times(t, i) {
        solve(i+1);
    }
    return 0;
}