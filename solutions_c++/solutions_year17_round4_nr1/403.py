
#include<bits/stdc++.h>
using namespace std;
#define D(x)        cout<<#x " = "<<(x)<<endl
#define un(x)       x.erase(unique(x.begin(),x.end()), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define pb          push_back
#define mp          make_pair
#define xx          first
#define yy          second
#define hp          (LL) 999983
#define MAX         100
#define eps         1e-9
#define pi          acos(-1.00)
typedef long long int LL;
typedef pair<int,int> pii;

int arr[MAX+5];
int cnt[7];
int n, p;
int dp[MAX+5][MAX+5][MAX+5][7];

int F(int m1, int m2, int m3, int prv)
{
    int ret = 0;
    if(dp[m1][m2][m3][prv] != -1) return dp[m1][m2][m3][prv];
    if(m1 != 0)
    {
        int new_mod = (prv + 1) % p;

        if(prv == 0) ret = max(ret, 1 + F(m1 - 1, m2, m3, new_mod));
        else ret = max(ret, F(m1 - 1, m2, m3, new_mod));
    }

    if(m2 != 0)
    {
        int new_mod = (prv + 2) % p;
        if(prv == 0) ret = max(ret, 1 + F(m1, m2 - 1, m3, new_mod));
        else ret = max(ret, F(m1, m2 - 1, m3, new_mod));
    }

    if(m3 != 0)
    {
        int new_mod = (prv + 3) % p;
        if(prv == 0) ret = max(ret, 1 + F(m1, m2, m3 - 1, new_mod));
        else ret = max(ret, F(m1, m2, m3 - 1, new_mod));
    }

    return dp[m1][m2][m3][prv] =ret;
}

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int i, j, k;
    int t, cs;

    sf(t);
    for(cs = 1; cs <= t; cs++)
    {
        memset(cnt, 0, sizeof(cnt));
        memset(dp, -1, sizeof(dp));

        sff(n, p);
        for(i = 1; i <= n; i++)
        {
            scanf("%d", &arr[i]);
            cnt[arr[i] % p]++;
        }

        for(i = 0; i <= cnt[1]; i++)
            for(j = 0; j <= cnt[2]; j++)
                for(k = 0; k <= cnt[3]; k++)
                    for(int prv = 0; prv < p; prv++)
                        F(i, j, k, prv);
        printf("Case #%d: %d\n", cs, cnt[0] + F(cnt[1], cnt[2], cnt[3], 0));
    }
    return 0;
}





