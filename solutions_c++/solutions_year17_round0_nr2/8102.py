#include <stdio.h>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

char a[2010];
int n;

long long gen_num(int pos) {
    long long res = 0;
    for (int i = 0; i < n; ++i) {
        res *= 10;
        if (i < pos) {
            res += a[i] - '0';
        } else if (i == pos) {
            res += a[i] - '0' - 1;
        } else {
            res += 9;
        }
    }
    return res;
}

void solve(int idx) {
    cin >> a;
    n = strlen(a);
    cout << "Case #" << idx << ": ";
    long long ans = gen_num(0);
    for (int i = 1; i <= n; ++i) {
        if (i == n) {
            cout << a << '\n';
            return;
        }
        if (a[i] < a[i - 1]) {
            break;
        }
        if (a[i] == a[i - 1]) {
            continue;
        }
        ans = gen_num(i);
    }
    cout << ans << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
    return 0;
}
