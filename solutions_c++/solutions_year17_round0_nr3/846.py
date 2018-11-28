#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pii;

#define A first
#define B second

ll t, n, k;

void doit(int abc) {
    cout << "Case #" << abc+1 << ": ";
    cin >> n >> k;
    map<ll, ll> m;
    m[n] = 1;

    while(true) {
        pii t = (*m.rbegin());
        if (k <= t.B) {
            cout << (t.A)/2 << ' ' << (t.A-1)/2 << endl;
            return;
        }

        k -= t.B;
        m[(t.A-1)/2] += t.B;
        m[t.A/2] += t.B;
        m.erase(t.A);
    }
}

int main() {
    cin >> t;
    for (int i = 0; i < t; ++i)
        doit(i);
}