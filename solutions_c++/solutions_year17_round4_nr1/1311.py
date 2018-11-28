#include <bits/stdc++.h>
using namespace std;

int dp[101][101][101];
int solve(int m1, int m2, int m3)
{
    if (dp[m1][m2][m3]==-1)
    {
        int x = 999,t=0;
        if (m2>=2) {t=1;x = min(x,solve(m1,m2-2,m3)+1);}
        if (m1&&m3) {t=1;x = min(x,solve(m1-1,m2,m3-1)+1);}
        if (m2&&m1>=2) {t=1;x = min(x,solve(m1-2,m2-1,m3)+2);}
        if (m2&&m3>=2) {t=1;x = min(x,solve(m1,m2-1,m3-2)+2);}
        if (m1 >= 4) {t=1;x = min(x,solve(m1-4,m2,m3)+3);}
        if (m3 >= 4) {t=1;x = min(x,solve(m1,m2,m3-4)+3);}
        dp[m1][m2][m3] = x;
        if (!t)
        {
            return max(0,(m1+m2+m3)-1);
        }
    }
    return dp[m1][m2][m3];
}
int main()
{
    int T; cin >> T;
    for (int t = 1; t <= T; t++)
    {
        map<int,int> modulo;
        int N, P, X;
        cin >> N >> P;
        for (int i = 0; i < N; i++)
        {
            cin >> X;
            modulo[X%P]++;
        }
        int ans=0;
        if (P==2) ans = modulo[1]/2;
        else if (P==3)
        {
            while (modulo[1]&&modulo[2])
            {
                modulo[1]--;
                modulo[2]--;
                ans++;
            }
            ans += (modulo[1]/3)*2 + max(0, modulo[1]%3 - 1);
            ans += (modulo[2]/3)*2 + max(0, modulo[2]%3 - 1);
        }
        else if (P==4)
        {
            memset(dp,-1,sizeof(dp));
            ans = solve(modulo[1],modulo[2],modulo[3]);
        }
        cout << "Case #" << t << ": " << N-ans << endl;
    }
}
