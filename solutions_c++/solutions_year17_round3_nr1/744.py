#include<iostream>
#include<cstdio>
#include<algorithm>

const double PI = 3.141592653589793;
const int MAX_N = 1000;

using namespace std;

typedef pair<double, pair<double, double> > P;

P cake[MAX_N];

int main(void)
{
    int T;  cin >> T;

    for (int t = 1; t <= T; t ++)
    {
        int N, K; scanf("%d %d", &N, &K);

        for (int i = 0; i < N; i ++)
        {
            scanf("%lf %lf", &cake[i].first, &cake[i].second.second);
            cake[i].second.first = cake[i].first * cake[i].second.second * 2 * PI;
        }

        sort(cake, cake + N);

        double res, max_val = 0, max_r;

        for (int i = N-1; i >= K - 1; i --)
        {
            max_r = 0;
            res = 0;

            sort(cake, cake + i, [](const P& a, const P& b){return a.second.first < b.second.first;});

            for (int j = i; j >= i - K + 1; j--)
            {
                res += cake[j].second.first;
                max_r = max(cake[j].first, max_r);
            }

            sort(cake, cake + i);

            res += max_r * max_r * PI;

            if (max_val < res)
                max_val = res;
        }

        printf("Case #%d: %lf\n", t, max_val);
    }
}
