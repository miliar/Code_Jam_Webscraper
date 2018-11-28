#include <bits/stdc++.h>

using namespace std;

bool istidy(int i) {
    stringstream ss; ss << i;
    string s = ss.str();
    bool b = true;
    for (int k = 0; k < s.length()-1; k++) {
        b &= s[k] <= s[k+1];
    }
    return b;
}

int main() {
    int a[1010]; a[0] = 0;
    for (int i = 1; i <= 1000; i++) {
        if (istidy(i)) a[i] = i;
        else a[i] = a[i-1];
    }
    int t, c = 0; cin >> t;
    while (t--) {
        int n; cin >> n;
        cout << "Case #" << ++c << ": " << a[n] << endl;;
        // if (n < 10) cout << n << endl;
        // else {
            // while (!istidy(n)) {
                // n--;
            // }
            // cout << n << endl;
        // }
    }
}