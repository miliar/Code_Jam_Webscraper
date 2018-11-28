#include <bits/stdc++.h>

using namespace std;

int main() {
//    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin >> tc;
    for (int ti = 1; ti <= tc; ++ti) {
        printf("Case #%d: ", ti);
        string s;
        int k;
        cin >> s >> k;
        int n = s.length();
        int cnt = 0;
        for (int i = 0; i < n-k+1; ++i)
            if (s[i] == '-') {
                ++cnt;
                for (int j = i; j < i+k; ++j)
                    s[j] = s[j] == '-' ? '+' : '-';
            }
        bool ok = true;
        for (int j = n-k; j < n; ++j)
            if (s[j] == '-')
                ok = false;
        if (ok)
            printf("%d\n", cnt);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
