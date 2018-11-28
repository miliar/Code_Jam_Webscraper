#include <bits/stdc++.h>
using namespace std;

int mc[1441],mj[1441];
int dp[1441][2][721], dpj[1441][2][721];
int solve(int i, int j, int k)
{
    if (k > 720 || i-k > 720) return 9999;
    if (i == 1440) return (j==1)?1:0;
    if (dp[i][j][k]==-1)
    {
        if (j == 0)
        {
            if (mc[i]) dp[i][j][k] = solve(mc[i],0,k+(mc[i]-i));
            else if (mj[i]) dp[i][j][k] = solve(mj[i],1,k)+1;
            else dp[i][j][k] = min(solve(i+1,0,k+1),solve(i+1,1,k)+1);
        }
        else
        {
            if (mc[i]) dp[i][j][k] = solve(mc[i],0,k+(mc[i]-i))+1;
            else if (mj[i]) dp[i][j][k] = solve(mj[i],1,k);
            else dp[i][j][k] = min(solve(i+1,0,k+1)+1,solve(i+1,1,k));
        }
    }
    return dp[i][j][k];
}
int solvj(int i, int j, int k)
{
    if (k > 720 || i-k > 720) return 9999;
    if (i == 1440) return (j==0)?1:0;
    if (dpj[i][j][k]==-1)
    {
        if (j == 0)
        {
            if (mc[i]) dpj[i][j][k] = solvj(mc[i],0,k+(mc[i]-i));
            else if (mj[i]) dpj[i][j][k] = solvj(mj[i],1,k)+1;
            else dpj[i][j][k] = min(solvj(i+1,0,k+1),solvj(i+1,1,k)+1);
        }
        else
        {
            if (mc[i]) dpj[i][j][k] = solvj(mc[i],0,k+(mc[i]-i))+1;
            else if (mj[i]) dpj[i][j][k] = solvj(mj[i],1,k);
            else dpj[i][j][k] = min(solvj(i+1,0,k+1)+1,solvj(i+1,1,k));
        }
    }
    return dpj[i][j][k];
}
int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        int Ac, Aj, X, Y; cin >> Ac >> Aj;
        memset(mc,0,sizeof(mc));
        memset(mj,0,sizeof(mj));
        for (int i = 0; i < Ac; i++)
        {
            cin >> X >> Y;
            mc[X] = Y;
        }
        for (int i = 0; i < Aj; i++)
        {
            cin >> X >> Y;
            mj[X] = Y;
        }
        cout << "Case #" << t << ": ";
        memset(dp,-1,sizeof(dp));
        memset(dpj,-1,sizeof(dpj));
        int ans = 9999;
        if (mc[0]) ans = solve(mc[0],0,mc[0]);
        else if (mj[0]) ans = solvj(mj[0],1,0);
        else ans = min(solve(0,0,0),solvj(0,1,0));
        cout << ans << endl;
    }
}
