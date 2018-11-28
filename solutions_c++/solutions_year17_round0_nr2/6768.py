#include <bits/stdc++.h>
using namespace std;

#define inf (long long)1e18

vector<int> A;
long long dp[20][10][2];

long long solve(int N, int prev, int lo, long long ten)
{
    if(N==A.size())
        return 0;

    if(dp[N][prev][lo]!=-1)
        return dp[N][prev][lo];

    long long ans = -inf;

    for(int i=prev; i<=9; i++)
    {
        if(lo==0 && i>A[N])
            break;

        ans = max(ans, ten*i + solve(N+1, i, (lo|(i<A[N])), ten/10));
    }

    return dp[N][prev][lo] = ans;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output2.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int test=1; test<=T; test++)
    {
        long long N;
        scanf("%lld", &N);

        A.clear();
        long long ten = 1;

        while(N)
        {
            A.push_back(N%10);
            N /= 10;

            if(N)
                ten *= 10;
        }

        memset(dp, -1, sizeof(dp));

        reverse(A.begin(), A.end());
        printf("Case #%d: %lld\n", test, solve(0, 0, 0, ten));
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
