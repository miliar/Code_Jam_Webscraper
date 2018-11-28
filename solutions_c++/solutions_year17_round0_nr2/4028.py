#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

int main()
{
    int test;
    while(scanf("%d", &test) == 1) {
        char s1[25];
        int len, tmp, j;
        for(int i = 1; i <= test; ++i) {
            memset(s1, 0, sizeof(s1));
            scanf("%s", s1);
            len = strlen(s1);
            tmp = len;
            for(j = 1; j < tmp && j > 0; ++j) {
                if(s1[j] < s1[j-1]) {
                    tmp = j;
                    for(int k = j; k < len; ++k) s1[k] = '9';
                    if(s1[j-1] >= '0') {
                        s1[j-1]--;
                        j -= 2;
                    }
                }
            }
            if(s1[j] != '0') printf("Case #%d: %s\n", i, s1);
            else printf("Case #%d: %s\n", i, &s1[1]);
            
        }
    }

    return 0;
}