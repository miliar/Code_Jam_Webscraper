#include <cstdio>
#include <cstring>

int main()
{
    int t;

    scanf("%d", &t);
    for (int tc = 1; tc <= t; ++tc) {
        char buf[24];
        char *p;
        int len;
        int last;

        scanf("%s", buf);
        len = strlen(buf);
        for (int i = 1; i < len; ++i) {
            if (buf[i] < buf[i-1]) {
                do {
                    --buf[--i];
                } while (buf[i] < buf[i-1]);

                for (int j = i+1; j < len; ++j) {
                    buf[j] = '9';
                }
            }
        }

        p = buf;
        while (*p == '0') {
            ++p;
        }
        printf("Case #%d: %s\n", tc, p);
    }
}
