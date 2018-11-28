#include <bits/stdc++.h>

using namespace std;

typedef long long ll;


void solve(int case_number) {
    string s;
    int k;
    cin >> s >> k;
    int n = s.length();

    int i=0;
    while (s[i] == '+')
        ++i;
    int ans = 0;
    while (i < n-k+1) {
        for (int j=0; j<k; ++j) {
            if (s[i+j] == '+')
                s[i+j] = '-';
            else
                s[i+j] = '+';
        }
        ++ans;
        while(i < n && s[i] == '+')
            ++i;        
    }
    for (int i=0; i<n; ++i) {
        if (s[i] == '-') {
            cout << "Case #" << case_number << ": IMPOSSIBLE" << endl;
            return;
        }
    }
    
    cout << "Case #" << case_number << ": " << ans << endl;
}


int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;

    for (int t=1; t<=T; ++t) {
        solve(t);
    }


    return 0;
}

