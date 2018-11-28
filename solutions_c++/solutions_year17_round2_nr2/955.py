#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int T, N, R, O, Y, G, B, V;
const char c[3] = {'R', 'Y', 'B'};
const char d[3] = {'G', 'V', 'O'};
const string IMP = "IMPOSSIBLE";
int a[3], b[3], p[3];
int s[3];
bool f[3];

bool myfunction (int i, int j) {
    return a[i] > a[j];
}

void pr(int i) {
    if (f[i]) {
        for (int j = 0; j < b[i]; j++) cout << c[i] << d[i];
        f[i] = false;
    }
    cout << c[i];
}

void solve() {
    for (int i = 0; i < 3; i++) {
        if (a[i] < b[i]) {
            cout << IMP;
            return;
        }
        if (a[i] == b[i] && a[i] != 0) {
            if (a[i]+b[i] == N) {
                for (int j = 0; j < N/2; j++) {
                    cout << c[i] << d[i];
                }
            }
            else cout << IMP;
            return;
        }
    }
    for (int i = 0; i < 3; i++) {
        N = N - 2*b[i];
        a[i] -= b[i];
    }

    for (int i = 0; i < 3; i++) s[i] = i;
    sort(s, s+3, myfunction);
    for (int i = 0; i < 3; i++) f[i] = true;

    if (a[s[0]] > N/2) {
        cout << IMP;
        return;
    }
    while (a[s[1]] > a[s[2]]) {
        pr(s[0]); a[s[0]]--;
        pr(s[1]); a[s[1]]--;
    }
    if (a[s[0]] == 0) return;
    while (a[s[0]] > 1) {
        pr(s[0]); a[s[0]]--;
        if (a[s[1]] > a[s[2]]) {
            pr(s[1]); a[s[1]]--;
        }
        else {
            pr(s[2]); a[s[2]]--;
        }
    }
    pr(s[0]); a[s[0]]--;
    while (a[s[2]] > 0) {
        pr(s[1]); a[s[1]]--;
        pr(s[2]); a[s[2]]--;
    }
    if (a[s[1]] > 0) {
        pr(s[1]); a[s[1]]--;
    }
}

int main() {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        cin >> N >> a[0] >> b[2] >> a[1] >> b[0] >> a[2] >> b[1];
        solve();
        cout << endl;
    }
    return 0;
}
