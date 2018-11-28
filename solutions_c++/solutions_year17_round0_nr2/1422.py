#include <bits/stdc++.h>
using namespace std;

const int N = 55;
long long comb[N][N];

bool check(int x) {
    vector <int> v;
    while (x > 0) v.push_back(x % 10), x /= 10;
    for (int i = 0; i < (int) v.size() - 1; i++) {
        if (v[i] < v[i + 1]) return false;
    }
    
    return true;
}

int naive(int x) {
    int ret = 0;
    for (int i = 0; i <= x; i++) {
        if (check(i)) ret++;
    }

    return ret;
}

long long findPosition(long long x) {
    vector <int> s;
    while (x > 0) s.push_back(x % 10), x /= 10;

    for (int i = 0; i < s.size() / 2; i++) 
        swap(s[i], s[s.size() - i - 1]);
    
    int now = 0;
    long long ans = 0;
    bool stillValid = true;
    for (int i = 0; i < s.size(); i++) {
        for (int j = now; j < s[i]; j++) {
            ans += comb[(int) s.size() - i - 1 + 9 - j][9 - j];
        }

        stillValid &= (now <= s[i]);
        if (!stillValid) break;
        now = max(now, s[i]);
    }
    
    if (stillValid) ans++;
    return ans;
}

int main() {
    for (int i = 0; i < N; i++)
        comb[i][0] = comb[i][i] = 1;
    
    for (int i = 1; i < N; i++)
        for (int j = 0; j < i; j++)
            comb[i][j] = comb[i - 1][j - 1] + comb[i - 1][j];

    /*
    for (int i = 0; i < 11111; i++)
        if (naive(i) != findPosition(i))
            cout << i << endl;
    */

    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        cerr << tc << endl;
        long long x;
        cin >> x;
        long long pos = findPosition(x);
        long long l = 0, r = x, ans = x;

        while (l <= r) {
            long long mid = l + r >> 1;
            //cerr << l << " " << r << " " << mid << " " << findPosition(mid) << " " << pos << endl;
            if (findPosition(mid) == pos)
                ans = mid, r = mid - 1;
            else l = mid + 1;
        }

        cout << "Case #" << tc << ": " << ans << endl;
    }
    return 0;
}