#include <bits/stdc++.h>

using namespace std;

char s[1100];

int main() {
    int t, k;
    scanf("%d", &t);

    for(int c = 1 ; c <= t ; c++) {
        scanf(" %s %d", s, &k);

        int cnt = 0;
        int i = 0;
        for( ; s[i + k - 1] ; i++) {
            if(s[i] == '-') {
                cnt++;
                for(int j = i ; j < i + k ; j++)
                    s[j] = s[j] == '-' ? '+' : '-';
            }
        }

        bool ok = true;
        for( ; s[i] ; i++)
            if(s[i] == '-') {
                ok = false;
                break;
            }

        if(ok)
            printf("Case #%d: %d\n", c, cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n", c);
    }

    return 0;
}
