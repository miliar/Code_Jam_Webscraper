#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;

#define xx first
#define yy second

const int maxn = 1010;

int main() {
    freopen("output.out", "w", stdout);
    int t;
    cin >> t;
    for (int cs = 1; cs <= t; cs++) {
        printf("CASE #%d: ", cs);
        string s;
        char c[maxn];
        int len;
        cin >> s >> len;
        int n = s.size();
        for (int i = 0; i < n; i++) c[i] = s[i];
        int cnt = 0;
        for (int i = 0; i <= n-len; i++) {
            if (c[i] == '-') {
                for (int j = 0; j < len; j++) {
                    c[i+j] = (c[i+j] == '-' ? '+' : '-');
                }
                cnt++;
            }
        }
        bool works = true;
        for (int i = n-len+1; works && i < n; i++) {
            if (c[i] != '+') works = false;
        }
        if (!works) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", cnt);
        }
    }
    return 0;
}
