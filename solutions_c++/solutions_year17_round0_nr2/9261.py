#include<bits/stdc++.h>
#define tr(x) cout << #x << " " << x << endl
using namespace std;

const int inf = (int) 1e8;

int t, n;

char s[20];

bool read() {
    if (scanf("%s", s) < 1) {
        return false;
    }
    n = strlen(s);
    return true;
}

void solve() {
    if (n == 1) {
        printf("%s\n", s);
        return;
    }
    bool baseCase = true;
    for (int i = 0; i < n - 1; i++) {
        baseCase &= (s[i] <= s[i + 1]);
    }
    if (baseCase) {
        printf("%s\n", s);
        return;
    }
    for (int i = 0; i < n - 1; i++) {
        if (s[i] < s[i + 1]) {
            continue;
        }
        int numDecr = s[i] - '0';
        int nines = n - i - 1;
        while (numDecr == 1 && i > 0) {
            ++nines;
            --i;
            if (i >= 0) {
                numDecr = s[i] - '0';
            }
            else {
                numDecr = 0;
            }
        }
        for (int j = 0; j < i; j++) {
            printf("%c", s[j]);
        }
        --numDecr;
        if (numDecr > 0) {
            printf("%d", numDecr);
        }
        while (nines--) {
            printf("9");
        }
        puts("");
        return;
    }
}

int main() {
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        read();
        printf("Case #%d: ", tt);
        solve();
    }
    return 0;
}

