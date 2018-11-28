#include <bits/stdc++.h>
using namespace std;

#define PI acos(-1.0)

int N, K;
double dp[1001][1001];
long long R[1001], H[1001];
vector<pair<int,int>> V;
double solve(int i, int j)
{
    if (i == N || j == 0) return 0;
    if (fabs(dp[i][j]+1.0) < 1e-8)
    {
        dp[i][j] = max(solve(i+1,j),solve(i+1,j-1)+2*PI*R[i]*H[i]);
    }
    return dp[i][j];
}

int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        cin >> N >> K;
        V.resize(N);
        for (int i = 0; i < N; i++)
            cin >> V[i].first >> V[i].second;

        sort(V.begin(),V.end(),greater<pair<int,int>>());
        for (int i = 0; i < N; i++)
        {
            R[i] = V[i].first;
            H[i] = V[i].second;
        }
        for (int i = 0; i < N; i++)
            for (int j = 0; j <= K; j++)
                dp[i][j] = -1;
        double ans = 0;
        for (int i = 0; i < N; i++)
        {
            ans = max(ans, PI*R[i]*R[i]+solve(i+1,K-1)+2*PI*R[i]*H[i]);
        }
        cout << "Case #" << t << ": ";
        cout << fixed << setprecision(10) << ans << endl;
    }
}
