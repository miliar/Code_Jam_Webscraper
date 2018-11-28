#include <bits/stdc++.h>
#define err(...) fprintf(stderr, __VA_ARGS__), fflush(stderr)

typedef long long ll;
using namespace std;

map<ll, ll> M[101];
map<ll, ll> Q;

int main() {
    int t;
    cin >> t;

    for (int test = 1; test <= t; test++) {
        ll n, k;
        cin >> n >> k;

        for (int i = 0; i < 101; i++) M[i].clear();
        Q.clear();

        M[0][n] = 1;


        for (int lvl = 0; lvl < 70; lvl++) {
            for (auto c : M[lvl]) {

                Q[-c.first] += c.second;

                ll a = (c.first - 1) / 2;
                ll b = c.first - 1 - a;
                if (a) M[lvl + 1][a] += c.second;
                if (b) M[lvl + 1][b] += c.second;
            }
        }

        ll lx = -1, rx = -1;
        for (auto c : Q) {
            //err("Q[%lld] = %lld\n", c.first, c.second);
            if (c.second >= k) {
                lx = (-c.first - 1) / 2;
                rx = -c.first - 1 - lx;
                break;
            } else {
                k -= c.second;
            }
        }
        //cout << (int)Q.size() << "\n";
        cout << "Case #" << test << ": " << rx << " " << lx << "\n";
    }
    return 0;
}


