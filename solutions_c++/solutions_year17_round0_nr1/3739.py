#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 1000 + 10;

int main()
{
    int TestCase;
    scanf("%d", &TestCase);
    
    for (int nowTestCase = 1; nowTestCase <= TestCase; ++ nowTestCase)
    {
        char s[MAXN];
        int N, K;

        scanf("%s", s + 1);
        scanf("%d", &K);
        N = strlen(s + 1);

        //int f[MAXN][MAXN];
        //memset(f, 0, sizeof(f));
//
        ////+ / -
        //for (int i = 1; i <= N; ++i)
        //{
            //for (int t = i - K + 1; t <= i; ++t)
            //{
                //if (t < 1 || t + K - 1 > N) continue;
//
                //f
//
            //}
        //}
        
        int mark[MAXN];
        memset(mark, 0, sizeof(mark));

        int ans = 0;
        bool flag = true;
        int nowSum = 0;
        for (int i = 1; i <= N; ++i)
        {
            int offset;
            if (s[i] == '+') offset = 0; else offset = 1;
            
            nowSum += mark[i];
            
            if ((offset + nowSum) % 2 == 0)
            {

            }
            else
            {
                if (i + K - 1 > N)
                {
                    flag = false;
                    break;
                }
                ++nowSum;
                ++ans;
                --mark[i + K];
            }
        }

        printf("Case #%d: ", nowTestCase);

        if (flag == false)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);

        
    }
    return 0;
}
