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

void calc_pref(vector<ld>& pref, const vector<ld>& dist) {
    pref[0] = dist[0];
    for (int i = 1; i < pref.size(); i++) {
        pref[i] = dist[i];
        pref[i] += pref[i - 1];
    }
}

ld getSum(vector<ld>& pref, int left, int right) {
    assert(right > 0);
    ld res = pref[right - 1];
    if (left > 0)
        res -= pref[left - 1];
    return res;    
}

void solve(int t) {
    int n, q;
    cin >> n >> q;
    
    vector<pair<ld, ld>> ver(n);
    for (int i = 0; i < n; i++) {
        ld e, s;
        cin >> e >> s;
        ver[i] = make_pair(e, s);
    }

    vector<ld> dist(n);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            ld d;
            cin >> d;
            if (fabs(d + 1) < 1e-9) {
            } else {
                dist[i] = d;
            }
        }
    }

    int start, finish;
    for (int i = 0; i < q; i++) {
        cin >> start >> finish;
    }

    vector<ld> pref(n);
    calc_pref(pref, dist);

    vector<ld> dp(n, 1e18);
    dp[n - 1] = 0;
    for (int i = 0; i < n - 1; i++) {
        ld d = getSum(pref, i, n - 1);
        if (d < ver[i].first + 1e-9) {
            dp[i] = d / ver[i].second;
        }
    }

    for (int i = n - 2; i >= 0; i--) {
        for (int j = i + 1; j < n - 1; j++) {
            ld d = getSum(pref, i, j);
            if (d < ver[i].first + 1e-9) {
                ld cur_t = d / ver[i].second;
                dp[i] = min(dp[i], cur_t + dp[j]);
            }
        }
    }

    cout << fixed << setprecision(9) << dp[0] << "\n";
}

void solve1() {
    int t;
    cin >> t;
    for (int i = 0; i < t; i++) {
        cout << "Case #" << i + 1 << ": ";
        solve(t);
    }
}

