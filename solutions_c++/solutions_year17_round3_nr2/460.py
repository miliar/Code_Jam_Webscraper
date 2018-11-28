#include <bits/stdc++.h>

#ifdef PIT
#define debug(...) fprintf(stderr, __VA_ARGS__)
#else
#define debug(...)
#endif

#define rep(i, j, k) for(int i = (int) j; i < (int) k; ++i)
#define sz(x) ((int) (x).size())
#define ll long long
#define mp make_pair
#define pii pair<int, int >
#define fi first
#define se second
#define pb push_back
#define inf 0x3f3f3f3f
#define INF 0x3f3f3f3f3f3f3f3f
#define zero(x) memset((x), (0), sizeof (x))
#define zerox(x, y) memset((x), (y), sizeof (x))

using namespace std;
const int mx = 24 * 60;

int a[mx+10];
int f[mx+10][mx/2+10][5][5];

int main()
{
#ifdef PIT
freopen("B-large.in", "r", stdin);
freopen("B-large.out", "w", stdout);
int _time_zlp = clock();
#endif // PIT

    int ic = 1, T;
    for(scanf("%d", &T); ic <= T; ++ic){
        printf("Case #%d: ", ic);
        //printf("Case #%d:\n", ic);
        int n,m;
        scanf("%d%d", &n,&m);
        zerox(a,-1);
        
        rep(i,1,1+n){
            int x,y;
            scanf("%d%d", &x,&y);
            rep(j,x,y) a[j%mx]=1;
        }

        rep(i,1,1+m){
            int x,y;
            scanf("%d%d", &x,&y);
            for(int j=x;j<y;j++)
                a[j%mx]=0;
        }
        rep(i,0,mx)
            for(int j=0;j<=mx/2;j++)
                rep(k,0,4)
                    f[i][j][k/2][k%2]=2*mx;
        f[0][0][0][0]=0;
        f[0][1][1][1]=0;
        rep(i,1,mx)
            for(int j=0;j<=mx/2;j++)
                rep(k,0,2)
                {
                    rep(l,0,2)
                    {
                        if(a[i]==-1||a[i]==0)
                            f[i][j][0][k]=min(f[i][j][0][k],f[i-1][j][l][k]+(l!=0));
                        if(j!=0)
                            if(a[i]==-1||a[i]==1)
                                f[i][j][1][k]=min(f[i][j][1][k],f[i-1][j-1][l][k]+(l!=1));
                    }
                }
        int ans=2*mx;
        rep(i,0,2)
            rep(j,0,2)
                ans=min(ans,f[mx-1][mx/2][i][j]+(i!=j));
        printf("%d\n",ans);
    }
#ifdef PIT
debug("Time: %f s\n", double(clock()-_time_zlp)/CLOCKS_PER_SEC);
#endif //PIT
    return 0;
}





