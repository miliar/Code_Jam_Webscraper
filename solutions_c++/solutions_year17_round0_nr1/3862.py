#include<bits/stdc++.h>

using namespace std;

char s[1005];

int main() {
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int T, K;
    scanf("%d",&T);
    for(int cs = 1; cs <= T; cs++) {
        scanf("%s%d",&s,&K);
        int res = 0;
        int gg = 0;
        int n = strlen(s);
        for(int i = 0; i + K - 1 < n; i++) {
            if(s[i] == '-') {
                res++;
                for(int j = i + 1; j < i + K; j++) {
                    if(s[j] == '+') s[j] = '-';
                    else s[j] = '+';
                }
            }
        }
        for(int i = n - K + 1; i < n; i++) {
            if(s[i] == '-') {
                gg = 1;
                break;
            }
        }
        printf("Case #%d: ",cs);
        if(gg) printf("IMPOSSIBLE\n");
        else printf("%d\n",res);
    }

}