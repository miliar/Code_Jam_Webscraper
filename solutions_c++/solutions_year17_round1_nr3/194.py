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

int ceil(int A, int B) { return (A + B - 1) / B; }

int calc(int health, int attack, int debuff, int times, int turns, int heal) {
    for (int actions = 1; actions < 500; actions++) {
        if (turns == 1) return actions;

        if (health <= (times ? (attack - debuff) : attack)) {
            health = heal;
        } else {
            if (times) {
                attack = max(attack - debuff, 0);
                times--;
            } else turns--;
        }

        health -= attack;
        if (health <= 0) break;
    }
    return INT_MAX;
}

void solve() {
    int Hd, Ad, Hk, Ak, B, D;
    cin >> Hd >> Ad >> Hk >> Ak >> B >> D;

    // first minimize number of "offensive" turns
    int off = INT_MAX;
    for (int buff = 0; buff <= 100; buff++) {
        int power = Ad + buff * B;
        int hits = ceil(Hk, power);
        off = min(off, buff + hits);
    }

    assert(off < INT_MAX);

    int ans = INT_MAX;
    // now see how many defensive moves we need to add
    for (int debuff = 0; debuff <= 100; debuff++) {
        ans = min(ans, calc(Hd, Ak, D, debuff, off, Hd));
    }

    if (ans == INT_MAX) cout << "IMPOSSIBLE" << endl;
    else cout << ans << endl;
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

