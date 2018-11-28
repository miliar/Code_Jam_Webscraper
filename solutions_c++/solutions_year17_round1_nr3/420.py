#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;

#define pb push_back
#define mp make_pair
#define f first
#define s second

#define FOR(i, a, b) for (int i=a; i<b; i++)
#define F0R(i, a) FOR(i, 0, a)

int hd, ad, hk, ak, b, d;
int play(int buff, int debuff) {
    int atkme = ad;
    int atkno = ak;
    int hme = hd;
    int hno = hk;
    int t = 0;
    F0R(i, debuff) {
        t++;
        int newatkno = max(0, atkno-d);
        if (hme <= newatkno) { hme = hd; }
        else { atkno = newatkno; }
        hme -= atkno;
        if (hme <= 0) { return -1; }
    }
    F0R(i, buff) {
        t++;
        if (hme <= atkno) { hme = hd; }
        else { atkme += b; }
        hme -= atkno;
        if (hme <= 0) { return -1; }
    }

    while (1) {
        pair<pii, pii> pv = {{hme, atkme}, {hno, atkno}};
        t++;
        if (hno - atkme <= 0) { return t; }
        if (hme - atkno <= 0) { hme = hd; }
        else { hno -= atkme; }
        hme -= atkno;
        if (hme <= 0) { return -1; }
        if (hme == pv.f.f && atkme == pv.f.s && hno == pv.s.f && atkno == pv.s.s) { return -1; }
    }
}
int main() {
    freopen("lol.txt", "w", stdout);
    int tcs; cin >> tcs;
    F0R(tc, tcs) {
        cin >> hd >> ad >> hk >> ak >> b >> d;

        int mini = 1000000000;
        F0R(i, 101) { F0R(j, 101) {
            int ok = play(i, j);
            if (ok != -1) { mini = min(mini, play(i, j)); }
        } }

        cout << "Case #" << tc+1 << ": ";
        if (mini == 1000000000) { cout << "IMPOSSIBLE" << endl; }
        else { cout << mini << endl; }
    }
}

