#include <iostream>
#include <string.h>
#include <cmath>

using namespace std;

bool confere(char *s) {
    int len = (int) strlen(s);
    for (int i = len-1; i > 0; --i) {
        if (s[i] != s[i - 1]) return false;
    }
    return true;
}

void flip(char *s, int i, int k) {
    for (int j = i; j < k; ++j) {
        s[j] = (s[j] == '-' )? '+' : '-';
    }
}

int OversizedPancakeFlipper(char *s, int k) {
    int len = (int) strlen(s);
    int flipo= 0;
    for (int i = 0; i < len; ++i) {
        for (int j = 0; j < len; ++j) {
            if(s[j] == '-') {
                flip(s, j, j+k);
                flipo++;
            }
            if (confere(s))return flipo;
        }
    }

    return -1;
}
int main() {

    int T, K;
    char S[10001];
    scanf("%d", &T);
    int i =1;
    while (i <= T) {
        scanf("%s %d", S, &K);
        int r = OversizedPancakeFlipper(S, K);
        if (r >= 0)
            printf("Case #%d: %d\n", i, r);
        else
            printf("Case #%d: IMPOSSIBLE\n", i);
        i++;
    }


    return 0;
}
