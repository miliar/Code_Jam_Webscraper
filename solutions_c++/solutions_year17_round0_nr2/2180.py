#include<cstdio>
#include<cstring>

int T;
char S[1010];
char ans[1010];

int minus[1010];

bool check(int pos, int l) {
    char c = S[pos];
    for (int j = pos + 1; j < l; j++) {
        if (S[j] > c) return true;
        if (S[j] < c) return false;
    }
    return true;
}

int main() {
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++) {
        scanf("%s", S);
        
        int l = strlen(S);
        for (int i = 0; i < l; i++) {
            if (check(i, l)) ans[i] = S[i];
            else {
                ans[i] = S[i] - 1;
                for (int j = i + 1; j < l; j++) {
                    ans[j] = '9';
                }
                break;
            }
        }
        printf("Case #%d: ", cas);
        for (int i = (ans[0] == '0'); i < l; i++) printf("%c", ans[i]);
        puts("");
    }
    return 0;
}