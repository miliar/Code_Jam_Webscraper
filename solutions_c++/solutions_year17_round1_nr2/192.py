#include <bits/stdc++.h>
using namespace std;

#define all(x) (x).begin(), (x).end()

#define TRACE(x) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define WATCHR(a, b) TRACE(for (auto it=a; it!=b;) cout << *(it++) << " "; cout << endl)
#define WATCHC(V) TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;

ll ceil(ll A, ll B) { return (A + B - 1) / B; }
ll floor(ll A, ll B) { return A / B; }

pair<ll, ll> calc(ll have, ll need) {
    return { ceil( 10 * have, 11 * need),
             floor( 10 * have, 9 * need) };
}

void solve() {
    int N, P;
    cin >> N >> P;

    vll recipe(N);
    for (int i = 0; i < N; i++)
        cin >> recipe[i];

    vector<vector<pair<ll, ll>>> range(N);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < P; j++) {
            ll amt;
            cin >> amt;
            range[i].push_back(calc(amt, recipe[i]));
        }

        sort(all(range[i]));
        reverse(all(range[i]));
    }

    int ans = 0;

    while (true) {
        ll front = LLONG_MIN, back = LLONG_MAX;
        for (int i = 0; i < N; i++) {
            if (range[i].empty()) 
                goto DONE;

            front = max(front, range[i].back().first);
            back = min(back, range[i].back().second);
        }

        if (front <= back) {
            ans++;
            for (int i = 0; i < N; i++)
                range[i].pop_back();
        } else {
            for (int i = 0; i < N; i++) {
                if (range[i].back().second == back) {
                    range[i].pop_back();
                    break;
                }
            }
        }
    }

    DONE:
    cout << ans << endl;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    cout << fixed << setprecision(15);

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }

    return 0;
}

