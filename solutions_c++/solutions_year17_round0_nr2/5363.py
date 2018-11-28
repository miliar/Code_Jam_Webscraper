#include <cstdio>
#include <cstring>

char input[20];

int lower(int d) {
    d--;
    if (d == -1) return 9;
    return d;
}

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++) {
        scanf("%s", input);

        int len = strlen(input);

        for (int j = 0; j < len - 1; j++) {
            int a = input[j] - '0';
            int b = input[j + 1] - '0';
            if (a > b) {
                input[j] = '0' + lower(a);
                for (int k = j + 1; k < len; k++) input[k] = '9';
                j -= 2;
            }
        }

        printf("Case #%d: ", i);
        int start = 0;
        while(input[start] == '0') start++;
        for (int i = start; i < len; i++) printf("%c", input[i]);
        printf("\n");
    }
    return 0;
}
