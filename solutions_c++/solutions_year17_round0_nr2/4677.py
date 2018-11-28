#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int T;
ll N;

int len, digs[20];

ll powersoften[20];

ll dp[21][2][10];


ll f(int idx, int flag, int biggestdigsofar) {
    if (idx == len) {
        return 0;
    }
    if (dp[idx][flag][biggestdigsofar] != -1) {
        return dp[idx][flag][biggestdigsofar];
    }
    ll tmp = -1000000000LL;
    if (flag) {
        for(int dig = biggestdigsofar; dig < 10; dig++) {
            ll tmp2 = f(idx + 1, true, dig);
            if (tmp2 < 0) continue;
            tmp = max(tmp, f(idx + 1, true, dig) + (dig * powersoften[len - idx - 1]));
        }
    } else {
        for(int dig = biggestdigsofar; dig < digs[idx]; dig++) {
            ll tmp2 = f(idx + 1, true, dig);
            if (tmp2 < 0) continue;
            tmp = max(tmp, f(idx + 1, true, dig) + (dig * powersoften[len - 1 - idx]));
        }
        if (biggestdigsofar <= digs[idx] && f(idx + 1, false, digs[idx]) >= 0) tmp = max(tmp, f(idx+1, false, digs[idx]) + (digs[idx] * powersoften[len - 1 - idx]));
    }
    //cout << "f(" << idx << ", " << flag << ", " << biggestdigsofar << ") = " << tmp << endl;
    return dp[idx][flag][biggestdigsofar] = tmp;
}

void toDigList() {

    int idx = 0;
    while (N > 0) {
        digs[idx++] = N % 10;
        N /= 10;
    }
    len = idx;
    reverse(digs, digs + len);
}

void precomptens() {
    ll tn = 1;
    for(int i = 0; i <= 18; i++) {
        powersoften[i] = tn;
        tn *= 10;
    }
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    cin >> T;
    precomptens();
    for(int kase = 1; kase <= T; kase++) {
        cin >> N;
        toDigList();
        memset(dp, -1, sizeof dp);
        cout << "Case #" << kase << ": " << f(0, false, 0) << endl;
    }
}
