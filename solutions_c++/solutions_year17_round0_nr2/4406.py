#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main() {
    int t;
    cin >> t;
    for (int test = 1; test <= t; ++test) {
        string n;
        cin >> n;
        for (int i = n.length() - 2; i >= 0; --i) {
            if (n[i] > n[i + 1]) {
                n[i]--;
                for (int j = i + 1; j < n.length(); ++j) {
                    n[j] = '9';
                }
            }
        }

        cout << "Case #" << test << ": ";

        if (n[0] != '0') {
            cout << n[0];
        }
        for (int i = 1; i < n.length(); ++i) {
            cout << n[i];
        }
        cout << endl;
    }

    return 0;
}
