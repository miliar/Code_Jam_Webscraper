#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

const int MAXN = 100;

int demand[MAXN];

int main()
{
    int testCase;
    scanf("%d", &testCase);

    for (int nowTestCase = 1; nowTestCase <= testCase; ++nowTestCase)
    {
        int N, P;
        scanf("%d%d", &N, &P);

        for (int i = 0; i < N; ++i)
            scanf("%d", &demand[i]);

        vector< vector<int> > pack;

        for (int i = 1; i <= N; ++i)
        {
            pack.push_back(vector<int>());
            for (int j = 1; j <= P; ++j)
            {
                int tmp;
                scanf("%d", &tmp);
                pack.back().push_back(tmp);
            }

            sort(pack.back().begin(), pack.back().end());
        }

        vector <int> head(N + 1);
        for (int i = 0; i < N; ++i)
            head[i] = 0;

        int ans = 0;

        for (int num = 1; num <= 1000000; ++num)
        {
            bool fuckyou = false;
            bool flag = true;
            while (flag)
            {
                for (int i = 0; i < N; ++i)
                {
                    long long l = 1LL * demand[i] * 9 * num;
                    long long r = 1LL * demand[i] * 11 * num;

                    long long now = 10LL * pack[i][head[i]];

                    while (head[i] < P && now < l)
                    {
                        head[i]++;
                        now = 10LL * pack[i][head[i]];
                    }

                    if (head[i] >= P || now > r)
                        flag = false;

                    if (head[i] >= P) fuckyou = true;
                }
                if (flag) 
                {
                    ++ans;
                    for (int i = 0; i < N; ++i) ++head[i];
                }
            }   
            if (fuckyou) break;
        }

        printf("Case #%d: %d\n", nowTestCase, ans);

    }
    return 0;
}
