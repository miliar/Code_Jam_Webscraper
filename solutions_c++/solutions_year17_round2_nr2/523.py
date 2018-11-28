#include <bits/stdc++.h>
#define pb push_back
typedef long long ll;
const int N = 1e5 + 10;
const int INF = 1e9;

using namespace std;

int test, hd, ad, hk, ak, b, d;
int id, ans;

// x = health me
// y = attack me
// u = health enemy
// v = attack enemy

void process(int lev, int total, int x, int y, int u, int v) {
    if (lev == 1) {
        process(lev + 1, total, x, y, u, v);
        if (d == 0) { return; }
        for (int i = 1; ; i++) {
            if (v <= 0) break;
            v -= d;
            int prev_x = x;
            x -= v;
            if (x <= 0) {
                v += d;
                x = hd - v;
                if (x <= prev_x) break;
            }
            else process(lev + 1, total + i, x, y, u, v);
        }
    }
    else
    if (lev == 2) {
        process(lev + 1, total, x, y, u, v);
        if (b == 0) { return; }
        for (int i = 1; ; i++) {
            if (y >= u) break;
            y += b;
            int prev_x = x;
            x -= v;
            if (x <= 0) {
                y -= b;
                x = hd - v;
                if (x <= prev_x) break;
            }
            else process(lev + 1, total + i, x, y, u, v);
        }
    }
    else {
        if (v <= 0) {  ans = min(ans, total + (u + y - 1) / y);  return; }
        int t = (x - 1) / v;
        if (y * (t + 1) >= u) { ans = min(ans, total + (u + y - 1) / y); return; }
        u -= y * t;
        total += t;
        x = hd - v;
        total++;
        t = (x - 1) / v;
        if (t == 0) return;
        while (1) {
            if (y * (t + 1) >= u) { ans = min(ans, total + (u + y - 1) / y); return; }
            u -= y * t;
            total += t;
            total++;
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin >> test;
    while (test--) {
        id++;
        cin >> hd >> ad >> hk >> ak >> b >> d;
        if (ak - d >= hd ) { cout << "Case #" << id << ": IMPOSSIBLE\n"; continue; }
        if (d == 0 && b == 0 && ak * 2 >= hd) { cout << "Case #" << id << ": IMPOSSIBLE\n"; continue; }
        ans = INF;
        process(1, 0, hd, ad, hk, ak);
        cout << "Case #" << id << ": ";
        if (ans == INF) cout << "IMPOSSIBLE\n";
        else cout << ans << endl; 
    }
    return 0;
}