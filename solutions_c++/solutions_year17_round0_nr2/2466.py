#include <bits/stdc++.h>
using namespace std;

#define TRACE(x) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define WATCHR(a, b) TRACE(for (auto it=a; it!=b;) cout << *(it++) << " "; cout << endl)
#define WATCHC(V) TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})

#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;

void gen(vll &tidy, ll value, int len) {
    if (len != 0) tidy.push_back(value);
    if (len == 18) return;

    for (int nd = (value % 10); nd <= 9; nd++) {
        if (len == 0 && nd == 0) continue;
        gen(tidy, 10 * value + nd, len + 1);
    }
}

void solve(vll &tidy) {
    ll N;
    cin >> N;
    auto it = upper_bound(all(tidy), N);
    cout << *prev(it);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    cout << fixed << setprecision(15);

    vll tidy;
    gen(tidy, 0, 0);
    sort(all(tidy));

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve(tidy);
        cout << "\n";
    }

    return 0;
}

