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

void solve(i64 case_num) {
    i64 d, n; cin >> d >> n;
    double maxt = 0;
    times(n, i) {
        i64 p, v; cin >> p >> v;
        maxt = max(maxt, double(d - p) / v);
    }
    cout << "Case #" << case_num << ": ";
    cout << fixed << setprecision(10) << d/maxt << endl;
}

i32 main()
{
    cin >> t;
    times(t, i) {
        solve(i+1);
    }
    return 0;
}