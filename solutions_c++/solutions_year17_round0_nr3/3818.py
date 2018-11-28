#include <iostream>
#include <cstdio>
using namespace std;

const int MAXN = 100000 + 10;

bool v[MAXN];
int l[MAXN], r[MAXN];

int main()
{
    int testCase;
    scanf("%d", &testCase);
    for (int nowTestCase = 1; nowTestCase <= testCase; ++nowTestCase)
    {
        int N, K;
        scanf("%d%d", &N, &K);
        int choose = 0;

        for (int now = 1; now <= K; ++now)
        {
            memset(l, 0, sizeof(l));
            memset(r, 0, sizeof(r));

            int sum = 0;
            for (int i = 1; i <= N; ++i)
            {
                if (v[i]) continue;
                l[i] = sum;
                ++sum; 
            }

            sum = 0;
            for (int i = N; i >= 1; --i)
            {
                if (v[i]) continue;
                r[i] = sum;
                ++sum;
            }

            int VALUE = -1;
            for (int i = 1; i <= N; ++i)
            {
                if (v[i]) continue;
                int value = min(l[i], r[i]);
                if (value > VALUE)
                {
                    VALUE = value;
                    choose = i;
                }
            }
            v[choose] = 1;
        }

        memset(l, 0, sizeof(l));
        memset(r, 0, sizeof(r));

        int sum = 0;
        for (int i = 1; i <= N; ++i)
        {
            l[i] = sum;
            if (v[i]) continue;
            ++sum; 
        }

        sum = 0;
        for (int i = N; i >= 1; --i)
        {
            r[i] = sum;
            if (v[i]) continue;
            ++sum;
        }

        //int ans1 = -1, ans2 = 100000;
        //for (int i = 1; i <= N; ++i)
        //{
            //if (!v[i]) continue;
            //int value = min(l[i], r[i]);
            //if (value > ans1)
                //ans1 = value;
            //if (value < ans2)
                //ans2 = value;
        //}

        printf("Case #%d: ", nowTestCase);
        cout << max(l[choose], r[choose]) << " " << min(l[choose], r[choose]) << endl;
    }
    return 0;
}
