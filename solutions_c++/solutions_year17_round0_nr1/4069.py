#include <iostream>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

using namespace std;

int main()
{
    int test;
    while(scanf("%d", &test) == 1) {
        char input[2010];
        int dis, len, times = 0;

        for(int i = 1; i <= test; ++i) {
            times = 0;
            memset(input, 0, sizeof(input));
            scanf("%s %d", input, &dis);
            len = strlen(input);
            bool success = true;

            for(int j = 0; j < len && success; ++j) {
                if(input[j] == '-') {
                    for(int k = 0; k < dis; ++k) {
                        input[j+k] = (input[j+k] == '-') * '+' + (input[j+k] == '+') * '-';
                        if(j+k >= len) success = false;
                    }
                    times++;
                }
            }
            if(success) printf("Case #%d: %d\n", i, times);
            else printf("Case #%d: IMPOSSIBLE\n", i);
        }
    }

    return 0;
}