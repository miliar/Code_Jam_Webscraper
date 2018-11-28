#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

string n;
int k;

int solve () {
    int ans = 0;
    string s = n;
    
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] != '+') {
            if (i + k - 1 >= s.size())
                return INT_MAX;
            for (int j = i; j < i + k; ++j)
                s[j] = '+' + '-' - s[j];
            ans += 1;
        }  
    }
    return ans;
}

int main() {
    int t, cas = 1;
    cin >> t;
    while (t--) {
        string ans;
        cin >> n >> k;
        ans = to_string (solve());
        if (stoi (ans) == INT_MAX)
            ans = "IMPOSSIBLE";
        cout << "Case #" << cas << ": " << ans << '\n';
        cas += 1;
    }
    return 0;
}