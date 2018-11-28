#include <cstdio>
#include <cstring>

using namespace std;



int main() {
    int T = 0;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; kase++) {
        int k = 0;
        int res = 0;
        bool possible = true;
        char buf[1100] = {0};
        scanf("%s %d", buf, &k);
        int start = 0;
        int buf_len = strlen(buf);
        while (start < buf_len) {
            if (buf[start] == '+') {
                while (start < buf_len && buf[start] == '+') {
                    start += 1;
                }
            }
            if (start < buf_len) {
                if (buf_len - start >= k) {
                    res += 1;
                    for (int i = 0; i < k; i++) {
                        buf[start + i] = (buf[start + i] == '+' ? '-' : '+');
                    }
                } else {
                    res = -1;
                    start = buf_len;
                }
            }
        }
        printf("Case #%d: ", kase);
        if (res >= 0) {
            printf("%d\n", res);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
