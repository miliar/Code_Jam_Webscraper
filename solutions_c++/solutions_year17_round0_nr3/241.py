#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int N = 1e4;
bool used[N];
int L[N];
int R[N];

void stupid(ll n, ll k) {
    fill(used, used + N, false);
    used[0] = true;
    used[n + 1] = true;
    for (int i = 0; i < k; i++) {
        for (int j = 0; j < n + 2; j++) {
            L[j] = 0;
            if (!used[j])
                L[j] = L[j - 1] + 1;
        }
        for (int j = n + 1; j >= 0; j--) {
            R[j] = 0;
            if (!used[j])
                R[j] = R[j + 1] + 1;
        }
        int a = -1000, b = -1000, l;
        for (int i = 0; i < n + 2; i++) {
            if (min(L[i], R[i]) > a || (min(L[i], R[i]) == a && max(L[i], R[i]) > b)) {
                a = min(L[i], R[i]);
                b = max(L[i], R[i]);
                l = i;
            }
        }
        used[l] = true;
        if (i == k - 1)
            cout << b - 1 << " " << a - 1 << " ";
    }
}

void solve() {
    ll n, k;
    cin >> n >> k;
    ll num1 = n;
    ll num2 = n;
    ll val1 = 1;
    ll val2 = 0;
    while (k > 0) {
        ll new_num1 = (num1 - 1) / 2;
        ll new_num2 = num2 / 2;
        ll new_val1 = 0;
        ll new_val2 = 0;
        if (val1 + val2 < k) {
            new_val1 += val1;
            if (num1 / 2 == new_num1)
                new_val1 += val1;
            else
                new_val2 += val1;
            if ((num2 - 1) / 2 == new_num1)
                new_val1 += val2;
            else
                new_val2 += val2;
            if (num2 / 2 == new_num1)
                new_val1 += val2;
            else
                new_val2 += val2;
            k -= val1 + val2;
            val1 = new_val1;
            val2 = new_val2;
            num1 = new_num1;
            num2 = new_num2;
            continue;
        }
        if (k <= val2)
            cout << num2 / 2 << " " << (num2 - 1) / 2 << "\n";
        else
            cout << (num1 / 2) << " " << (num1 - 1) / 2 << "\n";
        return;
    }

}

int main()
{
    ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
    }
    cin.tie(nullptr);
    return 0;
}
