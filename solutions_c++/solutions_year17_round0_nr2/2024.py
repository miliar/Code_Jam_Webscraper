#include <stdio.h>
#include <string.h>

char N[19];

void f(int len) {
    int i, j;
    for(i = 1; i < len; i++) if(N[i - 1] > N[i]) {
        for(j = i; j < len; j++) N[j] = '9';
        N[i - 1]--;
        f(len - 1);
    }
}

int main() {
    int T;
    int i, j;
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &T);
    for(i = 0; i < T; i++) {
        scanf("%s", N);
        f((int)strlen(N));
        for(j = 0; N[j] == '0'; j++);
        printf("Case #%d: %s\n", i + 1, &N[j]);
    }
    return 0;
}
