#include <stdio.h>
#include <stdlib.h>
#include <cstring>

char *foo(char a[]) {

    size_t len = strlen(a);

    size_t i = len - 1;

    for(;;) {
        for (; i > 0; i--) {

            if (a[i] < a[i - 1]) {

           //     if (a[i] == '0') {
                for (size_t j = i; j < len; j++) {
                    a[j] = '9';
                }
                    //}
   /*             } else {
                    a[i] = '9';
                }*/

                a[i - 1]--;
            }
        }
        if (a[0] == '0') {

            --len;
            for (int c = 0; c < len; c++) {
                a[c] = '9';
            }
            a[len] = '\0';

        } else {
            break;
        }
    }

    return a;

}

int main() {

    FILE *fp = fopen("/home/yifan/Downloads/B-large.in", "r");

    char a[100];

    fscanf(fp, "%s", a);

    int count = 1;
    while ((fscanf(fp, "%s", a)) != EOF) {



        char *b = foo(a);

        printf("Case #%d: %s\n", count++, b);
    }
    return 0;


}