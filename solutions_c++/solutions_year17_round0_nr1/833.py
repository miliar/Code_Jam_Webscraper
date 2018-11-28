#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int t, n, k;
string s;

void doit(int x) {
    cout << "Case #" << x+1 << ": ";
    cin >> s >> k;
    n = s.length();
    int ct = 0;

    for (int i = 0; i < n; ++i) {
        if (s[i] == '-')
            s[i] = 1;
        else
            s[i] = 0;
    }

    for (int i = 0; i < n; ++i) {
        if (s[i] == 0)
            continue;
        if (i > n-k && s[i] == 1) {
            cout << "IMPOSSIBLE\n";
            return;
        }

        if (s[i] == 1)
            for (int j = i; j <= i+k-1; ++j)
                s[j] = 1-s[j];
        ++ct;
    }

    cout << ct << endl;
}

int main() {
    cin >> t;
    for (int i = 0; i < t; ++i)
        doit(i);
}