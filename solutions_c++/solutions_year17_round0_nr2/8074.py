#include <cstdio>
#include <cstring>

int main() {
    int n, k;
    char s[1005], res[1005];
    int ans[1005];
    scanf("%d", &n);
    for(int cas = 1; cas <= n; cas++) {
        scanf("%s", s);
        memset(ans, -1, sizeof(ans));
        int len = strlen(s);
        ans[0] = s[0] - '0';
        bool lead = true, ign=false;
        for(int i = 1; i < len; i++) {
            if(ign == true) {
                ans[i] = 9;
                continue;
            }
            int v = s[i] - '0', pos = -1;
            if(v >= ans[i-1]) {
                ans[i] = v;
                continue;  
            }
            ans[i] = 9;
            ign = true;
            bool ign2 = false;
            for(int j = i-1;j>=0;j--) {
                ans[j] -= 1;
                if(ans[j] < 0) {
                    ans[j] = 9;
                    ign2 = true;
                    pos = j;
                    continue;
                }
                if(j == 0) {
                    break;
                }
                if(ans[j] >= ans[j-1]) {
                    break;
                }
                pos = j;
                ign2 = true;
                ans[j] = 9;
            }
            if(ign2 == true) {
                ign = true;
                for(int j = pos; j < i ; j++) {
                    ans[j] = 9;
                }
            }
        }
        int size = 0;
        for(int i = 0; i < len; i++) {
//            printf("%d ", ans[i]);
            if(ans[i] == -1 || ans[i] == 0) {
                if(size != 0) {
                    puts("EROR");
                }
                continue;
            }
            res[size++] = char(ans[i] + '0');
        }
//        puts("");

        if(size == 0) res[size++] = '0';
        res[size] = '\0';

        printf("Case #%d: %s\n", cas, res);
    }
        
}
