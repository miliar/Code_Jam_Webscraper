#include <bits/stdc++.h>
using namespace std;
const int N = 1004;

char str[N];
int side[N];
int main(){

    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int T, t;
    int k;
    scanf("%d", &T);
    for(t = 1; t <= T; t++){
        printf("Case #%d: ", t);
        scanf("%s%d", str, &k);
        int n = strlen(str);
        for(int i = 0; i < n; i++){
            if(str[i] == '+') side[i] = 1;
            else side[i] = 0;
        }
        int ans = 0;
        for(int i = 0; i <= n -k; i++){
            if(side[i]) continue;
            ans ++;
            for(int j = 0; j < k; j++){
                side[i+j] ^= 1;
            }
        }
        for(int i = 0; i < n; i++){
            if(!side[i]) {ans = -1; break;}
        }
        if(ans == -1) printf("IMPOSSIBLE\n");
        else printf("%d\n", ans);
    }
    return 0;
}
