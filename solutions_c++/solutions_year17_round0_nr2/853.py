#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    int T = 0;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; kase++) {
        char buf[20] = "0";
        scanf("%s", &buf[1]);
        int buf_len = strlen(buf);
        int pos = 0;
        for (pos = 1; pos < buf_len; pos++) {
            if (buf[pos] < buf[pos - 1]) {
                break;
            }
        }
        if (pos == buf_len) {
            printf("Case #%d: %s\n", kase, &buf[1]);
            continue;
        }
        for (int i = pos - 1; i > 0; i--) {
            int prev = i - 1;
            if (buf[prev] < buf[i]) {
                buf[i] -= 1;
                for (int j = i + 1; j < buf_len; j++) {
                    buf[j] = '9';
                }
                break;
            }
        }
        char *ptr = &buf[1];
        while (*ptr == '0') {
            ptr++;
        }
        printf("Case #%d: %s\n", kase, ptr);
    }
    return 0;
}
