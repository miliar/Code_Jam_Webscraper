#include <bits/stdc++.h>
using namespace std;

const int NMAX = 1024;

int ant, n, k;

char str[NMAX], mars[NMAX];

int main() {
//    freopen("dat.in", "r", stdin);
  //  freopen("dat.out", "w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    int tsk, op;
    bool flag;

    cin >> tsk;
    for (int t = 1; t <= tsk; ++t) {
        cin >> str >> k; n = strlen(str);

        for_each(str + 0, str + n, [](char &x) { x = ((x == '+') ? 0 : 1); });
        fill(mars, mars + n, 0);

        ant = op = 0;
        flag = true;

        for (int i = 0; i <= n - k; ++i) {
            op^= mars[i];
            if (str[i] ^ op) {
                mars[i + k]^= 1;
                mars[i]^= 1;
                op^= 1;
                ++ant; } }

        for (int i = n - k + 1; i < n && flag; ++i) {
            op^= mars[i];
            if (str[i] ^ op)
                flag = false; }

        cout << "Case #" << t << ": ";
        if (flag)
            cout << ant << '\n';
        else
            cout << "IMPOSSIBLE\n"; }


    return 0; }
