#include <cstdio>
#include <cstring>
char s[11111];
int nTest;
int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        scanf("%s", s);
        int k;
        scanf("%d\n", &k);
        int n = strlen(s);
        // printf("%d\n", n);
        int cnt = 0;
        for (int i = 0; i < n - k + 1; i++){
            if (s[i] == '-'){
                cnt++;
                //flip from i
                for (int j = i; j - i < k; j++){
                    if (s[j] == '-') s[j] = '+';
                    else s[j] = '-';
                }
            }
        }
        int impossible = 0;
        for (int i = n - k; i < n; i++){
            if (s[i] == '-') impossible = 1;
        }
        // printf("%s\n", s);
        if (impossible){
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", cnt);
        }
    }
}