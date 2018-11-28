#include <cstdio>
#include <cstring>

int main()
{
    int T;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++)
    {
        long N;
        scanf("%ld", &N);
        char buf[30];
        sprintf(buf, "%ld", N);
        for (int i = 0; buf[i]; i++)
        {
            if (buf[i+1] && buf[i] > buf[i+1])
            {
                buf[i]--;
                for (int j = i+1; buf[j]; j++)
                    buf[j] = '9';
                i = -1;
            }
        }
        char* p = buf;
        while (*p == '0') p++;
        printf("Case #%d: %s\n", tt, p);
    }
}
