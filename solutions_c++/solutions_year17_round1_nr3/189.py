#include <bits/stdc++.h>

using namespace std;

int t, hd, ad, hk, ak, b, d;

bool entered[105][105][105][105];
int mem[105][105][105][105];

int go(int mhd, int mad, int mhk, int mak) {
    // cout << mhd << " " << mad << " " << mhk << " " << mak << endl;
    if (mem[mhd][mad][mhk][mak] != -1) {
        return mem[mhd][mad][mhk][mak];
    }

    if (mhk == 0) return 0;
    if (mhd == 0) return 999999999;


    if (entered[mhd][mad][mhk][mak]) return 999999999;
    entered[mhd][mad][mhk][mak] = true;


    int newHP = max(mhd - mak, 0);
    int debufedAttack = max(mak - d, 0);
    // buff/debuf
    int mins = min(go(newHP, min(mad + b, 100), mhk, mak), go(max(mhd - debufedAttack, 0), mad, mhk, debufedAttack));
    // attack
    if (mad > 0) {
        mins = min(mins, go(newHP, mad, max(mhk - mad, 0), mak));
    }
    // cure
    if (mhd > 0) {
        mins = min(mins, go(max(hd - mak, 0), mad, mhk, mak));
    }

    if (mins >= 999999999) mins = 999999998;
    return mem[mhd][mad][mhk][mak] = mins + 1;
}

int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> hd >> ad >> hk >> ak >> b >> d;

        memset(mem, -1, sizeof(mem));
        memset(entered, 0, sizeof(entered));

        cout << "Case #" << test << ": ";
        if (go(hd, ad, hk, ak) == 999999999) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            cout << go(hd, ad, hk, ak) << endl;
        }
    }
}