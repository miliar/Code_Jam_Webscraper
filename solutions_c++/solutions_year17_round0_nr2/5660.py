#include <bits/stdc++.h>

using namespace std;

typedef long long ll;


void solve(int case_number) {
    string s;
    cin >> s;
    int n = s.length();

    for (int i=n-2; i>-1; --i) {
        if (s[i] > s[i+1]) {
            s[i]--;
            for (int j=i+1; j<n; ++j)
                s[j] = '9';
        }
    }
    ll x = 0;
    for (int i=0; i<n; ++i) {
        x *= 10;
        x += (ll)(s[i]-'0');
    }
    cout << "Case #" << case_number << ": " << x << endl;
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

