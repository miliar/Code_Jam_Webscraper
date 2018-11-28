#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

int main()
{
    int t, k;
    int flips, pSize;
    int nCase = 1;
    char pancakes[1001];

    scanf("%d", &t);
    while(t--) {
        scanf("%s %d", &pancakes, &k);
        flips = 0;
        pSize = strlen(pancakes);

        for (int i = 0; i < pSize; i++) {
            if (pancakes[i] == '-') {
                if (i+k > pSize) {
                    break;
                }
                for (int j = i; j < i+k; j++) {
                    if (pancakes[j] == '-')
                        pancakes[j] = '+';
                    else
                        pancakes[j] = '-';
                }
                flips++;
            }
        }

        bool impossible = false;
        for (int i = 0; i < pSize; i++) {
            //printf("%c ", pancakes[i]);
            if (pancakes[i] == '-') {
                impossible = true;
                break;
            }
        }

        if (impossible) {
            printf("Case #%d: IMPOSSIBLE\n", nCase++);
        } else {
            printf("Case #%d: %d\n", nCase++, flips);
        }
       
    }

    return 0;
}
