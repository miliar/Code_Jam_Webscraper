#include <bits/stdc++.h>
using namespace std;

int N;

int customer[1003];
vector<int> X[1003];

int func(int days)
{
    int rem = 0;

    for(int i=1; i<=N; i++)
    {
        rem += days;

        if(X[i].size()>rem)
            return 0;

        rem -= X[i].size();
    }

    return 1;
}

int solve(int days)
{
    int rem = 0, ans = 0;

    for(int i=N; i>=1; i--)
    {
        if(X[i].size()<=days)
        {
            int canFit = days - X[i].size();

            if(rem>=canFit)
                ans += canFit, rem -= canFit;
            else
                ans += rem, rem = 0;
        }
        else
            rem += X[i].size() - days;
    }

    return ans;
}

int main()
{
    freopen("B-large (1).in", "r", stdin);
    freopen("output4.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int test=1; test<=T; test++)
    {
        int C, M;
        scanf("%d %d %d", &N, &C, &M);

        memset(customer, 0, sizeof(customer));

        for(int i=1; i<=N; i++)
            X[i].clear();

        int left = 0, right = M;

        while(M--)
        {
            int p, b;
            scanf("%d %d", &p, &b);

            X[p].push_back(b);
            customer[b]++;
            left = max(left, customer[b]);
        }

        int ans1 = 0, ans2 = 0;

        while(left<=right)
        {
            int mid = (left+right)/2;

            if(func(mid))
            {
                ans1 = mid;
                right = mid-1;
            }
            else
                left = mid+1;
        }

        printf("Case #%d: %d %d\n", test, ans1, solve(ans1));
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
