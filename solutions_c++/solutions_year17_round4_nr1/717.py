#include <bits/stdc++.h>
using namespace std;
int n, p;
int in[10];
void solve(int Case) {
    cin >> n >> p;
    for (int i = 0; i <= 5; i++) {
        in[i] = 0;
    }
    int a;
    for (int i = 0; i < n; i++) {
        cin >> a;
        in[a%p]++;
    }

    int ans = 0;

    if (p == 2) {
        ans = in[0] + in[1]/2 + in[1]%2;
    } else if (p == 3) {
        ans = in[0];
        if (in[1] < in[2]) {
            ans += in[1];
            in[2] -= in[1];
            ans += in[2]/3;
            if(in[2]%3 != 0) ans++;
        } else {
            ans += in[2];
            in[1] -= in[2];
            ans += in[1]/3;
            if(in[1]%3 != 0) ans++;
        }
    } else if (p == 4) {
        ans = in[0];

        if (in[1] > in[3]) {
            ans += in[3];
            in[1] -= in[3];
            in[3] = 0;
        } else {
            ans += in[1];
            in[3] -= in[1];
            in[1] = 0;
        }

        int aa = min(in[1]/2, in[2]);
        if(aa != 0) {
            ans += aa;
            in[2] -= aa;
            in[1] -= 2*aa;
            if(in[2]) ans++;
        }
        int bb = min(in[3]/2, in[2]);
        if (bb != 0) {
            ans += bb;
            in[2] -= bb;
            in[3] -= 2*bb;
            if(in[2]) ans++;
        }

        ans += in[2]/2;
        in[2] %= 2;

        ans += in[1]/3 + in[3]/3;
        if(in[1]%3 || in[2] || in[3]%3) ans++;
    }

    cout << "Case #" << (Case+1) <<": ";
    printf("%d\n", ans);
}

int main () {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);
    int T;
    cin >> T;
    for (int i=0;i<T;i++) solve(i);
}
