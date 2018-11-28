#include <stdio.h>

int T;
char num[25];

int main()
{
    scanf("%d", &T);
    for (int z = 1; z <= T; z++) {
        scanf("%s", num);
        for (int i = 1; num[i] != '\0'; i++) {
            if (num[i-1] > num[i]) {
                num[i-1] --;
                for (int j = i; num[j] != '\0'; j++) {
                    num[j] = '9';
                }

                for (int j = i - 2; j >= 0; j--) {
                    if (num[j] > num[j+1]) {
                        num[j] --;
                        num[j+1] = '9';
                    }
                }
                break;
            }
        }
        printf("Case #%d: %s\n", z, (num[0] == '0' ? num + 1 : num));
    }
    
	return 0;
}

