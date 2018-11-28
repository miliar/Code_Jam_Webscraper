#include <cstdio>
#include <cstring>
char s[1005];
int f[1005];
int k, cnt, len;

int main() {
    int T;
    scanf("%d",&T);
    for(int t = 1; t <= T; t++) {
        scanf("%s%d", s, &k);
        len = strlen(s);
        for(int i = 0; i < len; i++) {
            f[i] = s[i] == '+' ? 1 : 0;
        }
        cnt = 0;
        for(int i = 0; i + k <= len; i++) {
            if(f[i] == 0){
                cnt++;
                for(int j = 0; j < k; j++) {
                    f[i+j] ^= 1;
                }
            }
        }
        bool flag = true;
        for(int i = 0; i < len; i++) {
            if(f[i] == 0) flag = false;
        }
        printf("Case #%d: ",t);
        if(flag) {
            printf("%d\n", cnt);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}