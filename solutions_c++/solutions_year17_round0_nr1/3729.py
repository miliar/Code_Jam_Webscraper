#include <cstdio>
#include <cstring>

char pancakes[1005];
int main(){
    int T; scanf("%d", &T); int test_id = 0;
    while (T--) {
        test_id += 1;
        int flips, ans = 0;
        scanf("\n%s %d", pancakes, &flips);
        int count = strlen(pancakes);
        for(int i = 0; i <= count - flips; i++) {
            if (pancakes[i] == '-') {
                for(int shift = 0; shift < flips; shift++) {
                    if (pancakes[i + shift] == '-') pancakes[i + shift] = '+';
                    else pancakes[i + shift] = '-';
                }
                ans ++;
            }
        }
        for(int i = 0; i < count; i++) {
            if (pancakes[i] == '-') ans = -1;
        }
        if (ans == -1) {
            printf("Case #%d: IMPOSSIBLE\n", test_id);
        } else {
            printf("Case #%d: %d\n", test_id, ans);
        }
    }   
}
