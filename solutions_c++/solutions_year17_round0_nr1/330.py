#include <cstdio>
#include <iostream>
using namespace std;

void solve()
{
    string s;
    cin >> s;
    int k;
    cin >> k;

    int ans = 0;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '-') {
            if (i + k - 1 >= s.size()) {
                printf("IMPOSSIBLE\n");
                return;
            }

            ans++;
            for (int j = 0; j < k; j++) {
                s[i + j] = s[i + j] == '+' ? '-' : '+';
            }
        }
    }

    printf("%d\n", ans);
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        printf("Case #%d: ", i);
        solve();
    }
    return 0;
}
