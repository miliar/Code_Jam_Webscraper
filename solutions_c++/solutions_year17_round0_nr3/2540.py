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

void solve() {
    ll N, K;
    cin >> N >> K;

    priority_queue<ll> gaps;
    map<ll, ll> ct;

    gaps.push(N);
    ct[N] = 1;

    ll A, B; // store last min and max

    while (K) {
        ll len = gaps.top();
        gaps.pop();

        if (len & 1) {
            A = len/2;
            B = len/2;
        } else {
            A = len/2;
            B = len/2 - 1;
        }

        if (K <= ct[len]) {
            break;
        }
        K -= ct[len];

        if (A) {
            if (!ct[A]) gaps.push(A);
            ct[A] += ct[len];
        }
        if (B) {
            if (!ct[B]) gaps.push(B);
            ct[B] += ct[len];
        }
    }

    cout << A << " " << B;
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
        cout << "\n";
    }

    return 0;
}

