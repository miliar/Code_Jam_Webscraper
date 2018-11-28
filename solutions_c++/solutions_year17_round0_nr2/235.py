#include <bits/stdc++.h>

using namespace std;
typedef long long ll;


void solve() {
    ll n;
    cin >> n;
    vector<int> digits;
    while (n > 0) {
        digits.push_back(n % 10);
        n /= 10;
    }
    reverse(digits.begin(), digits.end());
    int len = digits.size();
    for (int i = 0; i < len; i++) {
        int cur_res = digits[i];
        for (int j = i + 1; j < len; j++) {
            if (digits[j] > cur_res)
                break;
            else  if (digits[j] < cur_res) {
                cur_res--;
                break;
            }
        }
        if (cur_res != 0)
            cout << cur_res;
        if (digits[i] > cur_res) {
            for (int j = i + 1; j < len; j++)
                cout << "9";
            cout << "\n";
            return;
        }
    }
    cout << "\n";
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
