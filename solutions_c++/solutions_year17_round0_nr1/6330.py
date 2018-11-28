#include <bits/stdc++.h>

using namespace std;

int main() {
    int tt;
    scanf("%d", &tt);

    for (int qq = 1; qq <= tt; qq++) {
        printf("Case #%d: ", qq);
        fflush(stdout);
        char S[1234];
        int k;
        scanf("%s %d", S, &k);
        int len = (int) strlen(S);
        bool impossible = false;
        int ans = 0;
        for (int i = 0; i < len; i++) {
            if (S[i] == '-') {
                if (i + k - 1 < len) {
                    ans++;
                    for (int j = 0; j < k; j++) {
                        S[i + j] = (S[i + j] == '-') ? '+' : '-';
                    }
                } else {
                    impossible = true;
                    break;
                }
            }
        }
        if (impossible) printf("IMPOSSIBLE");
        else printf("%d", ans);
        printf("\n");
        fflush(stdout);
    }

    return 0;
}
