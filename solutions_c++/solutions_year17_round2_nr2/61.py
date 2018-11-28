#include <cstdio>
#include <cassert>

int main()
{
    int T;
    scanf("%d", &T);
    for (int tt = 1; tt <= T; tt++)
    {
        int N, C[6];
        scanf("%d%d%d%d%d%d%d", &N, C+0, C+1, C+2, C+3, C+4, C+5);
        const char* c = "ROYGBV";
        bool done = false;
        printf("Case #%d: ", tt);
        for (int i = 0; i < 3; i++)
        {
            if (N == C[i] + C[i+3])
            {
                if (C[i] == C[i+3])
                {
                    for (int j = 0; j < C[i]; j++)
                    {
                        putchar(c[i]);
                        putchar(c[i+3]);
                    }
                    puts("");
                    done = true;
                    break;
                }
                else
                {
                    puts("IMPOSSIBLE");
                    done = true;
                    break;
                }
            }
        }
        if (done) continue;
        for (int i = 1; i < 6; i += 2)
        {
            int other = (i+3)%6;
            if (C[i] != 0 && C[i] >= C[other])
            {
                puts("IMPOSSIBLE");
                done = true;
                break;
            }
            else
            {
                C[other] -= C[i];
            }
        }
        if (done) continue;
        int primary = C[0] + C[2] + C[4];
        for (int i = 0; i < 6; i += 2)
        {
            if (C[i] > primary - C[i])
            {
                puts("IMPOSSIBLE");
                done = true;
                break;
            }
        }
        if (done) continue;
        char buf[1001];
        int pos = 0;
        for (int ii = 0; ii < 3; ii++)
        {
            int i = 0;
            if (C[2] > C[i]) i = 2;
            if (C[4] > C[i]) i = 4;
            for (int j = 0; j < C[i]; j++)
            {
                buf[pos] = i;
                pos += 2;
                if (pos >= primary)
                    pos = 1;
            }
            C[i] = 0;
        }
        for (int p = 0; p < primary; p++)
        {
            int i = buf[p];
            putchar(c[i]);
            int other = (i+3)%6;
            while (C[other])
            {
                putchar(c[other]);
                putchar(c[i]);
                C[other]--;
            }
        }
        puts("");
        for (int i = 1; i < primary; i++)
            assert(buf[i] != buf[i-1]);
        assert(buf[0] != buf[primary-1]);
    }
}
