#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    int tc;
    while(scanf("%d", &tc) == 1) {
        getchar();
        char input[20];

        for(int y = 1; y <= tc; ++y) {
            memset(input, '\0', sizeof(input));
            fgets(input, sizeof(input), stdin);
            input[strlen(input) - 1] = '\0';

            int len = strlen(input);
            for(int i = 0; len != 1 && i < len - 1; ++i) {
                if(input[i] > input[i + 1]) {
                    for(int j = i + 1; j < len; ++j) 
                        input[j] = '9';
                    input[i] = input[i] - '0' - 1 + '0';
                    
                    if(input[i] == '0') {
                        if(i == 0) {
                            input[i] = '-';
                            break;
                        }
                        else {
                            input[i] = '9';
                            for(int j = i - 1; j >= 0; --j) {
                                input[j] = input[j] - '0' - 1 + '0';
                                if(input[j] != '0') 
                                    break;
                                else if(j == 0)
                                    input[j] = '-';
                                else 
                                    input[j] = '9';
                            }
                        }
                    }
                    if(input[i] < input[i - 1]) {
                        i -= 2;
                        continue;
                    }
                } 
            }
            
            printf("Case #%d: ", y);
            for(int i = 0; i < len; ++i) {
                if(input[i] != '-')
                    printf("%c", input[i]);
            }
            printf("\n");
        }
    }
    return 0;
}
