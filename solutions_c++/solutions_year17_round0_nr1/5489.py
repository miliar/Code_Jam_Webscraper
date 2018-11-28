#include <stdio.h>
#include <string.h>

#define FLIP(x) ((x)=='+'?'-':'+')

int main(void) {
    int T;
    char S[101];
    int K;
    int len;
    char to_plus[101];
    int cnt_flip_to_plus;
    
    scanf("%d ", &T);
    for (int t = 0; t < T; t++) {
        scanf("%s %d", S, &K);
    
        len = strlen(S);
        strcpy(to_plus, S);
        
        cnt_flip_to_plus = 0;
        
        for (int i = 0; i < len - K + 1; i++) {
            if (to_plus[i] == '-') {
                cnt_flip_to_plus++;
                for (int j = 0; j < K; j++) {
                    to_plus[i+j] = FLIP(to_plus[i+j]);
                }
            }
        }
        
        for (int i = len - K + 1; i < len; i++) {
            if (to_plus[i] == '-') {
                cnt_flip_to_plus = 999;
                break;
            }
        }
        if (cnt_flip_to_plus != 999) {
            printf("Case #%d: %d\n", t+1, cnt_flip_to_plus);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", t+1);
        }
    }
    
    return 0;
}
