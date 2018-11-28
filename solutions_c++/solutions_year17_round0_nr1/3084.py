#include <stdio.h>
#include <string.h>
#include <queue>

#define CONT true

using namespace std;

int T;
int k;
char S[1005];
queue <int> Q;

int main () {
    freopen("sol.out", "w", stdout);
    if ( CONT )
        freopen("A-large.in","r",stdin);
    else
        freopen("sol.in","r",stdin);
    scanf("%d", &T);
    for (int i = 1; i <= T; i ++) {
        printf("Case #%d: ", i);
        scanf("%s %d", S, &k);

        int len = strlen(S);
        while ( !Q.empty() ) Q.pop();
        int flips = 0;
        int ans = 0;
        bool impo = false;

        for (int j = 0; j < len; j++) {
            // printf("\nP %c F %d j %d len %d k %d Qf %d\n", S[j], flips, j, len, k, Q.empty()?-1:Q.front());
            if ( !Q.empty() && Q.front() == j ) {
                flips --;
                Q.pop();
            }
            if ((S[j] == '+' && flips % 2 == 1) || (S[j] == '-' && flips % 2 == 0)) {
                // S[j] = 1;
                if ( j + k > len ) {
                    impo = true;
                    printf("IMPOSSIBLE\n");
                    break;
                }
                Q.push(j + k);
                flips ++;
                ans ++;
            }
        }
        if ( !impo )
            printf("%d\n", ans);
    }
}