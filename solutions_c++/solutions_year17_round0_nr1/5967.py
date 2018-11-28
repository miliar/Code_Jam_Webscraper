#include <bits/stdc++.h>

using namespace std;

int T, k, moves;
string str;
char st[1010];

int main() {

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++) {
        scanf("%s %d", st, &k);

        str = st;
        moves = 0;

        for(int i=0; i + k - 1< str.size(); i++) {
            if(str[i] == '-') {
                moves++;
                for(int K = i; K < i + k; K++) {
                    if(str[K] == '-') str[K] = '+';
                    else str[K] = '-';
                }
            }
        }

        int flag = 1;
        for(int i=0;i<str.size();i++) {
            if(str[i] == '-') flag = 0;
        }

        printf("Case #%d: ", t);
        if(flag) printf("%d\n", moves);
        else printf("IMPOSSIBLE\n");
    }

    return 0;
}
