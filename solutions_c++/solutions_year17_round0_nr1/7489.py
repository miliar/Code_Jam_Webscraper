#include <bits/stdc++.h>
using namespace std;
char a[201];

int main(){
    freopen("A_large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int i, j, N, T;
    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        int x, ans = 0;
        scanf("%s %d", a, &x);
        N = strlen(a);
        for(i=0; i<=N-x; i++){
            if(a[i] == '-'){
                for(j=i; j<i+x; j++) {
                    if(a[j] == '-') a[j] = '+';
                    else a[j] = '-';
                }
                ans++;
            }
        }
        int flag = 0;
        for(i=0; i<N; i++){
            if(a[i] == '-') flag = 1;
        }
        if(!flag) printf("Case #%d: %d\n", t, ans);
        else printf("Case #%d: IMPOSSIBLE\n", t);
    }
}
