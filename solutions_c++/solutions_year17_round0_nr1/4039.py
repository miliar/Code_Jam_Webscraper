#include <iostream>
#include <cstdio>
#include <string.h>

using namespace std;

int a[10111];

void solve()
{
    int k;
    string s;
    cin >> s >> k;

    memset(a, 0, sizeof(a));
    int ans = 0;

    for (int i = 0; i < s.length(); i++) {
        a[i + 1] ^= a[i];

        int x = a[i + 1];
        if (s[i] == '-') x ^= 1;

        if (x == 1) {
            if (i < s.length() - k + 1) {
                ans++;
                a[i + 1] ^= 1;
                a[i + k + 1] ^= 1;
            }
            else {
                cout << "IMPOSSIBLE\n";
                return;
            }
        }
    }

    cout << ans << "\n";
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);

    int cntTests;
    cin >> cntTests;
    for (int numTest = 1; numTest <= cntTests; numTest++) {
        cout << "Case #" << numTest << ": ";
        solve();
    }
}
