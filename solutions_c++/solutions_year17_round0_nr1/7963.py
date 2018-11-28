#include <bits/stdc++.h>

using namespace std;

int k;


int solve(string in) {
    int ans = 0;
    for(int n = in.size(), i = 0; i <= n-k; i++) {
        if(in[i] == '-') {
            ans++;
            for(int j = 0; j < k; j++) {
                if(in[i+j] == '-') in[i+j] = '+';
                else in[i+j] = '-';
            }
        }
    }
    for(int n = in.size(), i = 0; i < n; i++) {
        if(in[i] == '-') return in.size();
    }
    return ans;
}

int main() {
    int T;
    cin >> T;
    int t = T;

    while(t--) {
        string st;
        cin >> st;
        cin >> k;

        // cout << st << endl;
        int ans1 = solve(st);
        reverse(st.begin(), st.end());
        int ans2 = solve(st);
        // cout << ans1 << endl;
        // cout << st << endl;
        // cout << ans2 << endl;

        int ans = min(ans1, ans2);
        cout << "Case #" << T-t << ": "; 
        if(ans == st.size())
            cout << "IMPOSSIBLE\n";
        else
            cout << ans << endl;
    }
}