#include <cstdio>
#include <cstdlib>
#include <cstring>
void flip(char input[], int k) {
    for (int i = 0; i < k; i++) {
        input[i] = (input[i] == '+')?'-':'+';
    }
}
int check(char input[]) {
    char *ptr = input;
    while(*ptr) {
        if (*ptr == '-')
            return 0;
        ptr++;
    }
    return 1;
}
int main() {
    char input[1001];
    const char imp[] = "IMPOSSIBLE";
    int t, k;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        printf("Case #%d: ", tt);
        scanf("%s", input);
        scanf("%d", &k);
        int len = strlen(input);
        int flip_count = 0;
        for (int i = 0; i <= len-k; i++) {
            if (input[i] == '-') {
                //printf("BE %s\n", input);
                flip(input+i, k);
                //printf("AF %s\n", input);
                flip_count++;
            }
        }
        if (check(input)) {
            printf("%d\n", flip_count);
        } else {
            printf("%s\n", imp);
        }
    }
    return 0;
}
