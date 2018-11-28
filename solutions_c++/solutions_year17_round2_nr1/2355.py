#include <bits/stdc++.h>
using namespace std;

int K[1003], S[1003];
long double endTime[1003];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output2.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int test=1; test<=T; test++)
    {
        int D, N;
        scanf("%d %d", &D, &N);

        for(int i=1; i<=N; i++)
            scanf("%d %d", &K[i], &S[i]);

        endTime[N] = (long double)(D-K[N])/S[N];

        for(int i=N-1; i>=1; i--)
        {
            endTime[i] = (long double)(D-K[i])/S[i];
            endTime[i] = max(endTime[i], endTime[i+1]);
        }

        printf("Case #%d: ", test);
        cout << fixed << setprecision(8) << D/endTime[1] << "\n";
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
