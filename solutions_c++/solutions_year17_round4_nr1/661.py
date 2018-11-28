#include<bits/stdc++.h>
using namespace std;
int N, P;

int dp[101][101][101][4];
int tmain()
{
    memset(dp, 0x8f, sizeof(dp));
    scanf("%d %d", &N, &P);
    int cnt[4] = {0, 0, 0, 0};
    for(int i=0; i<N; ++i)
    {
        int x;
        scanf("%d", &x);
        cnt[x%P]++;
    }
    int v1 = cnt[1], v2 = cnt[2], v3 = cnt[3];
    dp[0][0][0][0] = 0;
    for(int i=0; i<=v1; ++i)
        for(int j=0; j<=v2; ++j)
            for(int k=0; k<=v3; ++k)
                for(int s=0; s<P; ++s)
                {
                    if(i!=v1) dp[i+1][j][k][(s+1)%P] = max(dp[i+1][j][k][(s+1)%P], dp[i][j][k][s] + ((s==0)?1:0));
                    if(j!=v2) dp[i][j+1][k][(s+2)%P] = max(dp[i][j+1][k][(s+2)%P], dp[i][j][k][s] + ((s==0)?1:0));
                    if(k!=v3) dp[i][j][k+1][(s+3)%P] = max(dp[i][j][k+1][(s+3)%P], dp[i][j][k][s] + ((s==0)?1:0));
                }
    //cerr << cnt[0] << " " << dp[1][0][0][1] << endl;
    int ans = -1;
    for(int i=0; i<P; ++i) ans = max(ans, dp[v1][v2][v3][i]);
    return ans+cnt[0];
    
}
int main()
{
    int T;
    scanf("%d", &T);
    for(int i=1; i<=T; ++i)
    {
        printf("Case #%d: %d\n", i, tmain());
    }
    return 0;
}
