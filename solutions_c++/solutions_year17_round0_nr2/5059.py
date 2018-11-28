#include <cstdio>

int main() {
    int t;
    scanf("%d", &t);
    for(int k = 1; k <= t; k++) {
        char num[20];
        scanf("%s", num);
        int i, j = -1;

        for (i = 0; num[i+1]; i++) {
            if (num[i] > num[i+1])
                j = i;
        }
        if (j != -1)
            i = j;
        if (num[i+1]) {
            while (i > -1) {
                if (num[i] > num[i+1]) {
                    num[i+1] = '0' + 9;
                    if (num[i] != '0')
                        num[i]--;
                    else {
                        while (i > -1 && num[i] == '0') {
                            num[i] = '0' + 9;
                            i--;
                        }
                        if (i != -1)
                            num[i]--;
                    }
                  //  printf("%s ", num);
                }
                i--;
            }
        }
        j = 0 + '0';
        for (i = 0; num[i]; i++) {
            if (j > num[i])
                num[i] = j;
            else
                j = num[i];
        }

        for (i = 0; num[i] && num[i] == '0'; i++);
        printf("Case #%d: %s\n", k, num + i);
    }   
    return 0;
}