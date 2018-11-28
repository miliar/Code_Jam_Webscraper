#include <stdio.h>
#include <string.h>
#include <iostream>

char S[20];

int main(int argc, char *argv[])
{
    int i;
    int j;
    int T;
    int N;
    int change;
    char a;
    char b;

    std::cin >> T;

    for(i=1; i<=T; i++) {
        std::cin >> S;

        N = strnlen(S, 20);
        change = 1;

        while(change) {
            change = 0;

            for(j=0; j<N-1; j++) {
                a = S[j];
                b = S[j+1];

                if(b < a) {
                    change = 1;
                    S[j] = a-1;
                    memset(S+j+1, (int)'9', N-j-1);
                }
            }
        }

        if(S[0] == '0')
            std::cout << "Case #" << i << ": " << S+1 << std::endl;
        else
            std::cout << "Case #" << i << ": " << S << std::endl;
    }
    
    return 0;
}
