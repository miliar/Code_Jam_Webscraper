#include <iostream>
#include <string>
using namespace std;

typedef long long ll;

int t, x = 1;
ll N, ans;

ll solve() {
    ll n = N;
    string s;
    bool flag = true;

    while (true) {
        s = to_string(n);
        flag = true;
        //cout << n << endl;
        if (s.size() == 1) {
            return n;
        }

        int size_ = s.size();

        for (int i = 0; i < size_ - 1; ++i) {
            if (s[i] > s[i + 1]) {
                n--;
                flag = false;
                break;
            }
        }

        if (flag) return n;
    }
}

int main(void) {
    cin.tie(0);
    ios::sync_with_stdio(false);

    cin >> t;

    while (t--) {
        cin >> N;
        ans = solve();
        cout << "Case #" << x << ": " << ans << "\n";
        x++;
    }

    return 0;
}