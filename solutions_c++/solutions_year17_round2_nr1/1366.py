#include <bits/stdc++.h>
using namespace std;

#define TASK ""

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int ui;
typedef long double ld;
typedef pair<int, int> pairi;
typedef pair<ll, ll> pairll;
typedef pair<ld, ld> pairld;

#define all(v) v.begin(),v.end()
#define forn(s, n) for (int i = s; i < n; i++)
#define mp make_pair
#define pb push_back
#define sz size
#define EPS 1e-7

const int INF = INT_MAX / 2, NINF = INT_MIN / 2;
const ld PI = acos(-1.0);

void prepareIO () {
}

void debout() {
}

template <typename Head, typename... Tail>
void debout(Head H, Tail... T) {
#ifdef _DEBUG
    cerr << H << ' ';
    debout(T...);
#endif
}

class Timer {
public:
    double begin;
    Timer () : begin(clock()) {}
    ~Timer() {
        fprintf(stderr, "%.6lf\n", (clock() - begin + .0) / CLOCKS_PER_SEC);
    }
} timer_;

void solve1();

int main() {
    prepareIO();
    solve1();
    return 0;
}

void solve(int t) {
    ld d;
    int n;
    cin >> d >> n;

    ld ans = 1e18;
    for (int i = 0; i < n; i++) {
        ld pos, speed;
        cin >> pos >> speed;

        ld len = d - pos,
           t = len / speed,
           cur_speed = d / t;
        ans = min(ans, cur_speed);
    }

    cout << setprecision(9) << fixed << ans << "\n";
}

void solve1() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve(i);
    }
}

