#include <bits/stdc++.h>
using namespace std;

long double X[55];

int N;
long double U, total;

long double power(long double N, int expo)
{
    long double ans = 1;

    while(expo)
    {
        if(expo%2)
            ans *= N;

        N *= N;
        expo/= 2;
    }

    return ans;
}

int func(long double x)
{
    long double req = 0;

    for(int i=1; i<=N; i++)
    {
        if(X[i]>x)
            continue;

        req += (x - X[i]);

        if(req>U)
            return 0;
    }

    return 1;
}

long double solve(long double left, long double right)
{
    long double mid = (left+right)/2;

    if(right-left<1e-8)
        return mid;

    if(func(mid)==0)
        return solve(left, mid);

    return solve(mid, right);
}

int main()
{
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("output3.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int test=1; test<=T; test++)
    {
        int K;
        scanf("%d %d", &N, &K);

        cin >> U;
        total = 0;

        for(int i=1; i<=N; i++)
            cin >> X[i];

        long double ans = 1;
        long double lim = solve(0, 1);

        for(int i=1; i<=N; i++)
            ans *= max(lim, X[i]);

        printf("Case #%d: ", test);
        cout << fixed << setprecision(7) << ans << "\n";
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
