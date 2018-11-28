#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<int, int> pii;

void sub() {
    int n, p;
    cin >> n >> p;
    vector<int> cnt(4);
    for (int i = 0; i < n; i++) {
        int tmp;
        cin >> tmp;
        cnt[tmp % p]++;
    }

    int ans = cnt[0];
    cnt[0] = 0;
    if (cnt[1] + cnt[2] > 0)
        ans++;

    if (p == 3) {
        while (cnt[1] >= 1 && cnt[2] >= 1) {
            cnt[1]--;
            cnt[2]--;
            if (cnt[1] + cnt[2] > 0)
                ans++;
        }

        while (cnt[1] >= 3) {
            cnt[1] -= 3;
            if (cnt[1] + cnt[2] > 0)
                ans++;
        }

        while (cnt[2] >= 3) {
            cnt[2] -= 3;
            if (cnt[1] + cnt[2] > 0)
                ans++;
        }
    } else {
        while (cnt[1] >= 2) {
            cnt[1] -= 2;
            if (cnt[1] + cnt[2] > 0)
                ans++;
        }
    }

    cout << ans << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        sub();
    }
}
