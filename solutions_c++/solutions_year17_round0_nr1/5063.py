#include <cstdio>
#include <cstring>

int main() {
    int t;
    scanf("%d", &t);
    for(int k = 1; k <= t; k++) {
        char str[1001], str2[1001];
        scanf("%s", str);

        strcpy(str2, strrev(str));
        
        int l, cnt = 0, temp = '+'^'-', cnt2 = 0;

        bool flag1 = true, flag2 = true;

        scanf("%d", &l);
        for (int i = 0; str[i+l-1]; i++) {
            if (str[i] == '-') {
                cnt++;
                for (int j = 0; j < l; j++)
                    str[i+j] ^= temp;
               // printf("%s ", str);
            }

            if (!str[i+l]) {
                for (int j = 1; j < l; j++)
                    if (str[i+j] == '-')
                        flag1 = false;
            }
        }



        for (int i = 0; str2[i+l-1]; i++) {
            if (str2[i] == '-') {
                cnt2++;
                for (int j = 0; j < l; j++)
                    str2[i+j] ^= temp;
                //printf("%s ", str2);
            }
            if (!str2[i+l]) {
                for (int j = 1; j < l; j++)
                    if (str2[i+j] == '-')
                        flag2 = false;
            }
        }
        printf("Case #%d: ", k);
        if (flag1 || flag2) {
            printf("%d\n", ((cnt<cnt2)?cnt:cnt2));
        }
        else
            printf("IMPOSSIBLE\n");
        
    }   
    return 0;
}