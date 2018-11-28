#include <stdio.h>

int tc, tt;

struct spc {
    long long len, cnt;
    };
spc a[1000];

int main()
{
    scanf("%d", &tt);
    int mj = 0;
    for (tc = 0; tc < tt; tc++){
        printf("Case #%d: ", tc + 1);

        long long k;
        long long rl[2];
        scanf("%I64d%I64d", &a[0].len, &k);
        a[0].cnt = 1;
        for (int i =0, j = 0; k > 0;++i){
            rl[0] = (a[i].len    ) / 2;
            rl[1] = (a[i].len - 1) / 2;
            for (int z = 0; z < 2; ++z){
                if (a[j].len != rl[z]){
                    ++j;
                    a[j].len = rl[z];
                    a[j].cnt = a[i].cnt;
                    }
                else {
                    a[j].cnt += a[i].cnt;
                    }
                }
            k -= a[i].cnt;
            if (mj < j)
                mj = j;
            }
        printf("%I64d %I64d\n", rl[0], rl[1]);
        }
    fprintf(stderr, "%d\n", mj);
    return 0;
}
