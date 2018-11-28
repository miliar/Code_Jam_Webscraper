#include <cstdio>
#include <cstring>
int nTest;

char origin[22];
char res[22];
void genRes(int pos = 0){
    if (pos >= 22) return;
    int start = '0';
    if (pos > 0) start = res[pos - 1];

    for (char num = start; num <= '9'; num++){
        for (int j = pos; j < 22; j++) res[j] = num;
        if (strcmp(res, origin) > 0){
            res[pos]--;
            break;
        }
    }
    genRes(pos + 1);
    return;
}
int main(){
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    scanf("%d", &nTest);
    for (int test = 1; test <= nTest; test++){
        printf("Case #%d: ", test);
        long long n;
        scanf("%lld", &n);
        for (int j = 21; j >= 0; j--){
            origin[j] = n % 10 + '0';
            n /= 10;
            res[j] = '0';
        }

        genRes();
        long long ans = 0;
        for (int i = 0; i < 22; i++){
            ans *= 10;
            ans += res[i] - '0';
        }
        printf("%lld\n", ans);
    }
}