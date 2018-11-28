#include<stdio.h>
#include<string.h>
char ch[30];
bool check() {
    int l = strlen(ch);
    for (int i = 0; i < l - 1; i++) {
        if (ch[i] > ch[i + 1]) {
            ch[i]--;
            for (int j = i + 1; j < l; j++) {
                ch[j] = '9';
            }
            return false;
        }
    }
    return true;
}
int main() {
    int ca;
    scanf("%d", &ca);
    for (int cas = 1; cas <= ca; cas++) {
        scanf("%s", ch);
        while (!check()) {
        }
        long long d;
        sscanf(ch, "%lld", &d);
        printf("Case #%d: %lld\n", cas, d);
    }
}
