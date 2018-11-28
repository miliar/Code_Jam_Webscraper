#include <iostream>

using namespace std;

string s;
int k;

void solve(int x) {
    cin >> s;
    cin >> k;
    int u = s.size();
    int c = 0;
    for (int i = 0; i <= u-k; i++) {
        if (s[i] != '+') {
            for (int j = 0; j < k; j++) {
                if (s[i+j] == '+') s[i+j] = '-';
                else s[i+j] = '+';
            }
            c++;
        }
    }
    bool ok = true;
    for (int i = 0; i < u; i++) {
        if (s[i] != '+') ok = false;
    }
    cout << "Case #" << x << ": ";
    if (ok) cout << c << "\n";
    else cout << "IMPOSSIBLE\n";
}

int main() {
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) solve(i);
}
