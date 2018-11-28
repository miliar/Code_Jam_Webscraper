#include <bits/stdc++.h>

using namespace std;

int main(){

    int T, K; cin >> T;
    for(int t = 1; t <= T; t++) {
    string s; cin >> s >> K;
    cout << "Case #" << t << ": ";
    int n = s.length();
    int ans = 0;
    bool ok = true;
    for(int i = 0; i + K <= n; i++) {
        if(s[i] == '-') {
            ans++;
            for(int j = i; j < i + K; j++) s[j] = (s[j] == '+')? '-' : '+';
        }
    }
    for(int i = n - K; i < n; i++) {
        if(s[i] == '-') {
            cout << "IMPOSSIBLE" << endl;
            ok = false;
            break;
        }
    }
    if(ok) cout << ans << endl;
    }
    return 0;
}
