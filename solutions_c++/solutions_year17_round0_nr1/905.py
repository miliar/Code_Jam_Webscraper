#include <bits/stdc++.h>

using namespace std;

int ans, sum[2007], k;
string s;

bool check() {
    s = " " + s;
    memset(sum, 0, sizeof(sum));
    for(int i = 1; i < s.length(); i++) {
        sum[i] = sum[i-1] + sum[i];
        if (s[i] == '-' && i > s.length() - k && sum[i] % 2 == 0) {
            return false;
        }
        else if (s[i] == '+' && i > s.length() - k && sum[i] % 2 == 1) {
            return false;
        }
        else if (s[i] == '-' && sum[i] % 2 == 0) {
            sum[i]++;
            ans++;
            sum[i+k]--;
        }
        else if (s[i] == '+' && sum[i] % 2 == 1) {
            sum[i]++;
            ans++;
            sum[i+k]--;
        }
    }
    return true;
}

int test;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    cin >> test;
    for(int i = 1; i <= test; i++) {
        cin >> s >> k;
        ans = 0;
        cout << "Case #" << i << ": ";
        if (check()) cout << ans;
        else cout << "IMPOSSIBLE";
        if (i != test) cout << endl;
    }
    fclose(stdin);
    fclose(stdout);
}
