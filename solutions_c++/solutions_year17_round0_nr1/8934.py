#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main()
{
    char input[1010];
    char tmp[1010];
    int tc;

    while(scanf("%d", &tc) == 1) {
        getchar();
        for(int y = 1; y <= tc; ++y) {
            int K, len, i = 0, countt = 0, flag = 0;
            memset(input, '\0', sizeof(input));
            memset(tmp, '\0', sizeof(tmp));
            fgets(input, sizeof(input), stdin);

            while(1) {
                if(input[i] != '+' && input[i] != '-') {
                    strcpy(tmp, input + i + 1);
                    break;
                }
                ++i;
            }
            len = i;
            K = atoi(tmp);

            for(i = 0; i < len && !flag; ++i) {
                if(input[i] == '-') {
                    for(int j = 0; j < K; ++j) {
                        if(i + j >= len) {
                            flag = 1;
                            break;
                        }
                        if(input[i + j] == '-')
                            input[i + j] = '+';
                        else input[i + j] = '-';
                    }
                    ++countt;
                }
            } 
            if(!flag) {
                for(i = 0; i < len; ++i) {
                    if(input[i] == '-') {
                        flag = 1;
                        break;
                    }
                }
            }

            if(!flag)
                printf("Case #%d: %d\n", y, countt);
            else printf("Case #%d: IMPOSSIBLE\n", y);
        }
    }
    return 0;
}
