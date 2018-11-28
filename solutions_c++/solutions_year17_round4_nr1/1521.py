#include <bits/stdc++.h>

using namespace std;

#define _FILES
#define PB push_back
#define MP make_pair

typedef long long ll;
typedef pair<int,int> pii;

const int MAXN = 105;
const int INF = 1e8;
int dp[MAXN][MAXN][5];
int dp1[MAXN][MAXN][MAXN][5];
int g[MAXN];


int solve()
{
    int n, p, ans, k, k1, k2, k3, mx;
    cin>>n>>p;
    for (int i=0;i<n;i++)
    {
        cin>>g[i];
        g[i] %= p;
    }

    if (p == 2)
    {
        ans = 0;
        k = 0;
        for (int i=0;i<n;i++)
        {
            if (!g[i]) ans++; else k++;
        }
        ans += (k/2 + (k&1));
    }

    if (p == 3)
    {
        for (int i=0;i<MAXN;i++)
        {
            for (int j=0;j<MAXN;j++)
            {
                for (int jj=0;jj<5;jj++) dp[i][j][jj] = -INF;
            }
        }

        dp[1][0][2] = 1;
        dp[1][1][1] = 1;

        for (int i=1;i<101;i++)
        {
            for (int j=0;j<=i;j++)
            {
                for (int cur=0;cur<3;cur++)
                {
                    //1
                    if (!cur)
                    {
                        dp[i+1][j+1][(cur+1)%p] = max(dp[i+1][j+1][(cur+1)%p], dp[i][j][cur] + 1);
                    }
                    else
                    {
                       dp[i+1][j+1][(cur+1)%p] = max(dp[i+1][j+1][(cur+1)%p], dp[i][j][cur]);
                    }

                    //2
                    if (!cur)
                    {
                        dp[i+1][j][(cur+2)%p] = max(dp[i+1][j][(cur+2)%p], dp[i][j][cur] + 1);
                    }
                    else
                    {
                       dp[i+1][j][(cur+2)%p] = max(dp[i+1][j][(cur+2)%p], dp[i][j][cur]);
                    }
                }
            }
        }

        ans = 0;
        k1 = 0;
        k2 = 0;

        for (int i=0;i<n;i++)
        {
            if (!g[i]) ans++;
            if (g[i]==1) k1++;
            if (g[i]==2) k2++;
        }
        if (k1+k2) ans += max(dp[k1+k2][k1][0], max(dp[k1+k2][k1][1],dp[k1+k2][k1][2]));
    }

    if (p == 4)
    {
       for (int i=0;i<MAXN;i++)
        {
            for (int j=0;j<MAXN;j++)
            {
                for (int ii=0;ii<MAXN;ii++)
                {
                    for (int jj=0;jj<5;jj++) dp1[i][j][ii][jj] = -INF;
                }
            }
        }

        dp1[1][1][0][1] = 1;
        dp1[1][0][1][2] = 1;
        dp1[1][0][0][3] = 1;

        for (int i=1;i<101;i++)
        {
            for (int j=0;j<101;j++)
            {
                for (int w=0;w<101;w++)
                {
                    if (j+w>i) continue;
                    for (int cur=0;cur<4;cur++)
                    {
                       //1
                       if (!cur)
                       {
                           dp1[i+1][j+1][w][(cur+1)%p] = max(dp1[i+1][j+1][w][(cur+1)%p], dp1[i][j][w][cur] + 1);
                       }
                       else
                       {
                           dp1[i+1][j+1][w][(cur+1)%p] = max(dp1[i+1][j+1][w][(cur+1)%p], dp1[i][j][w][cur]);
                       }

                       //2
                       if (!cur)
                       {
                           dp1[i+1][j][w+1][(cur+2)%p] = max(dp1[i+1][j][w+1][(cur+2)%p], dp1[i][j][w][cur] + 1);
                       }
                       else
                       {
                           dp1[i+1][j][w+1][(cur+2)%p] = max(dp1[i+1][j][w+1][(cur+2)%p], dp1[i][j][w][cur]);
                       }

                       //3

                       if (!cur)
                       {
                           dp1[i+1][j][w][(cur+3)%p] = max(dp1[i+1][j][w][(cur+3)%p], dp1[i][j][w][cur] + 1);
                       }
                       else
                       {
                           dp1[i+1][j][w][(cur+3)%p] = max(dp1[i+1][j][w][(cur+3)%p], dp1[i][j][w][cur]);
                       }
                    }
                }
            }
        }

        k1 = 0;
        k2 = 0;
        k3 = 0;
        ans = 0;
        for (int i=0;i<n;i++)
        {
            if (!g[i]) ans++;
            if (g[i]==1) k1++;
            if (g[i]==2) k2++;
            if (g[i]==3) k3++;
        }
        mx = 0;
        if (k1+k2+k3)
        {
            for (int i=0;i<4;i++) mx = max(mx, dp1[k1+k2+k3][k1][k2][i]);
        }
        ans += mx;
    }
    return ans;
}


int main()
{
    ios_base::sync_with_stdio(false);

    #ifdef _FILES
        freopen("A-large.in","r",stdin);
        freopen("out.txt","w",stdout);
    #endif // _FILES
    int T;
    cin>>T;
    for (int test=1;test<=T;test++)
    {
        cout<<"Case #"<<test<<": "<<solve()<<endl;
    }
    return 0;
}
