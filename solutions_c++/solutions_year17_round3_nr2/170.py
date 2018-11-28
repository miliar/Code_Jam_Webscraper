#include <bits/stdc++.h>
using namespace std;

int inf = 1001;
int dp[505][729][3][3];

vector< pair<int, int> > Z;
vector< pair< pair<int, int>, int > > X, Y;

int solve(int pos, int cRem, int prev, int st)
{
    if(cRem<0)
        return inf;

    if(pos<0)
    {
        if(cRem)
            return inf;

        if(st==prev)
            return 0;

        return 1;
    }

    if(dp[pos][cRem][prev][st]!=-1)
        return dp[pos][cRem][prev][st];

    int ans = inf;

    if(Z[pos].second!=2)
    {
        if(prev==1)
            ans = min(ans, solve(pos-1, cRem, 2, st) + 1);
        else
            ans = min(ans, solve(pos-1, cRem, 2, st));
    }

    if(Z[pos].second!=1)
    {
        if(prev==2)
            ans = min(ans, solve(pos-1, cRem-Z[pos].first, 1, st) + 1);
        else
            ans = min(ans, solve(pos-1, cRem-Z[pos].first, 1, st));
    }

    if(Z[pos].second==0)
    {
        for(int i=1; i<Z[pos].first; i++)
        {
            if(prev==1)
                ans = min(ans, solve(pos-1, cRem-i, 1, st) + 2);
            else
                ans = min(ans, solve(pos-1, cRem-i, 1, st) + 1);

            int rem = Z[pos].first - i;

            if(prev==2)
                ans = min(ans, solve(pos-1, cRem-rem, 2, st) + 2);
            else
                ans = min(ans, solve(pos-1, cRem-rem, 2, st) + 1);
        }
    }

    return dp[pos][cRem][prev][st] = ans;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("output5.txt", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int test=1; test<=T; test++)
    {
        int C, J;
        scanf("%d %d", &C, &J);

        X.clear(), Y.clear(), Z.clear();

        for(int i=1; i<=C; i++)
        {
            int L, R;
            scanf("%d %d", &L, &R);

            Y.push_back({{L, R}, 1});
        }

        for(int i=1; i<=J; i++)
        {
            int L, R;
            scanf("%d %d", &L, &R);

            Y.push_back({{L, R}, 2});
        }

        int prevTime = 0;
        sort(Y.begin(), Y.end());

        for(int i=0; i<Y.size(); i++)
        {
            if(Y[i].first.first!=prevTime)
            {
                X.push_back({{prevTime, Y[i].first.first}, 0});
                prevTime = Y[i].first.first;
            }

            X.push_back({{prevTime, Y[i].first.second}, Y[i].second});
            prevTime = Y[i].first.second;
        }

        if(prevTime!=1440)
            X.push_back({{prevTime, 1440}, 0});

        for(int i=0; i<X.size(); i++)
            Z.push_back({X[i].first.second-X[i].first.first, X[i].second});

        memset(dp, -1, sizeof(dp));
        printf("Case #%d: %d\n", test, min(solve(Z.size()-1, 720, 1, 1), solve(Z.size()-1, 720, 2, 2)));
    }

    fclose(stdin);
    fclose(stdout);

    return 0;
}
