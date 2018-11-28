#include <bits/stdc++.h>

using namespace std;

const int maxn = 200200;

int length(long long n) {
    long long k = 1;
    int ans = 0;
    while (k <= n) {
        k *= 10;
        ans++;
    }
    return ans;
}

long long get(int k, int length) {
    long long ans = 0;
    for (int i = 0; i < length; ++i) {
        ans *= 10;
        ans += k;
    }
    return ans;
}

long long first(long long n) {
    int len = length(n);
    long long k = 1;
    for (int i = 0; i < len - 1; ++i) {
        k *= 10;
    }
    return n / k;
}

long long solve(long long n) {
    if (n < 10) return n;
    int l = length(n);
    int f = first(n);
    if (get(f, l) <= n) {
        long long ans = f;
        for (int i = 0; i < l - 1; ++i) {
            ans *= 10;
        }
        return ans + solve(n - ans);
    } else {
        long long ans = f - 1;
        for (int i = 0; i < l - 1; ++i) {
            ans *= 10;
            ans += 9;
        }
        return ans;
    }
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    int t;
    cin >> t;
    for (int z = 0; z < t; ++z) {
        long long n;
        cin >> n;
        cout << "Case #" << z + 1 << ": " << solve(n) << "\n";
    }

    return 0;
}
