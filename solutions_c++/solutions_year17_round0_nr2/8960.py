#include<cstdio>
#include<cstring>

bool isTidy(int num) {
    char s[20];
    sprintf(s, "%d", num);
    int len = strlen(s);
    for(int i = 1; i < len; i++) {
        if(s[i-1] > s[i]) return false;
    }
    return true;
}

int main() {
    int T, t = 0, N;
    scanf("%d", &T);
    while(T--) {
        int ans = 0;
        scanf("%d", &N);
        for(int i = N; i >= 0; i--) {
            if(isTidy(i)) {
                ans = i;
                break;
            }
        }
        printf("Case #%d: %d\n", ++t, ans);
    }
    return 0;
}
