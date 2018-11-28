#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 105;

char s[N];

void solve(int nt) {
    scanf("%s", s);
    int n = strlen(s);

    printf("Case #%d: ", nt);

    bool dau = true;
    bool nhohon = false;

    for (int i = 0; i < n; i++) {
        int j;
        for (j = '9'; j >= '0'; j--) {
            bool ok = true;
            if (!nhohon)
            for (int k = i; k < n; k++)
                if (s[k] > j) break;
                else if (s[k] < j) {
                    ok = false; break;
                }
            if (ok) {
                if (!dau || (dau && j > '0')) putchar(j);
                if (j > '0') dau = false;
                break;
            }
        }
        if (j < s[i]) nhohon = true;
    }

    printf("\n");
}

int main() {
    int ct;
    scanf("%d", &ct);

    for (int nt = 1; nt <= ct; nt++) {
        solve(nt);
        fprintf(stderr, "Case %d done.", nt);
    }
}
