#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<map>

using namespace std;

int T;

int D, N, K[1005], S[1005];
double tm[1005];


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("result.out", "w", stdout);
    scanf("%d", &T);
    int t = 1;
    while(t <= T)
    {

        scanf("%d %d", &D, &N);
        for(int i=0; i<N; ++i)
        {
            scanf("%d %d", &K[i], &S[i]);
            tm[i] = (D - K[i]) * 1.0 / S[i];
        }
        sort(tm, tm + N);
        double result = (D - tm[N - 1] * (1e-8)) / tm[N - 1];

        printf("Case #%d: %lf\n", t++, result);
    }
    return 0;
}
