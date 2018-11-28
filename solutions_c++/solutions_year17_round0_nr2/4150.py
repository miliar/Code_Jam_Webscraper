#include <cstdio>
#include <cstring>

void mapp(char ans[]) {
    char *ptr = ans;
    while (*ptr) {
        *ptr -= '0';
        ptr++;
    }
}
void rmapp(char ans[], int len) {
    for (int i = 0; i < len ;i++) {
        if (ans[i] < 0) {
            fprintf(stderr, "ERROR\n");
        }
        ans[i] += '0';
    }
    long long int a = 0;
    sscanf(ans, "%lld", &a);
    sprintf(ans, "%lld", a);
}
int check(char ans[], int len) {
    for (int i = len-1; i > 0; i--) {
        if (ans[i] < ans[i-1] || ans[i] < 0) {
            return i-1;
        }
    }
    return -1;
}
void calc(char ans[], int len) {
    if (len == 1)
        return;
    for (int i = 0; i < len; i++) {
        //printf("BF ans = ");
        //for (int j = 0; j < len; j++) {
            //printf("%d", ans[j]);
        //}
        //printf("\n");

        int cks = check(ans, len);
        //printf("CKS = %d\n", cks);
        if (cks == -1) {
            return ;
        }
        ans[cks]-=1;

        for (int j = cks+1; j < len; j++) {
            ans[j] = 9;
        }
        //printf("AF ans = ");
        //for (int j = 0; j < len; j++) {
            //printf("%d", ans[j]);
        //}
        //printf("\n");
    }
}
int main() {
    int t;
    char ans[100];
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        printf("Case #%d: ", tt);
        scanf("%s", ans);
        int len = strlen(ans);
        mapp(ans);
        calc(ans, len);
        rmapp(ans, len);
        printf("%s\n", ans);
    }
}
