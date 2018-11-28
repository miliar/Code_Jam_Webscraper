#include <cstdio>
#include <cstring>

typedef unsigned long long llu;

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {

        llu n;
        scanf("%llu", &n);
        char s[20];
        sprintf(s, "%llu", n);
        int l = strlen(s);

        int lastFlip = l;
        for (int i = l-1; i >= 1; --i) {
            if (s[i] < s[i-1]) {
                --s[i-1];
                lastFlip = i;
            }
        }
        for (int i = lastFlip; i < l; ++i)
            s[i] = '9';
        int pad;
        for (pad = 0; pad < l-1; ++pad) {
            if (s[pad] != '0')
                break;
        }
        
        printf("Case #%d: %s\n", t, s+pad);

    }
    return 0;
}