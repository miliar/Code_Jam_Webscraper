#include<iostream>
#include<algorithm>
#include<cctype>
#include<cstdio>
#include<cstring>
#include<string>
#include<map>
#include<vector>
#include<set>
#include<cmath>
#include<queue>
#include<ctime>
typedef long long ll;
#define pii pair<int,int>
#define xx first
#define yy second
#define mp make_pair
using namespace std;
const double INF = 1e18;
const double pi = acos(-1.0);
const int N = 1005;
double dp[N][N];

struct node
{
    double a, b;
}p[N];

bool cmp( node aa, node bb )
{
    if( aa.b > bb.b ) return 1;
    else return 0;
}

int main()
{
    double R, H;
    int n, m, i, j, T, cas = 1;
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while( T -- ){
        printf("Case #%d: ", cas++);
        scanf("%d%d", &n, &m);
        for( int i = 1; i <= n; i ++ ){
            scanf("%lf%lf", &R, &H);
            p[i].a = 2.0*pi*R*H;
            p[i].b = pi*R*R;
        }
        sort( p+1, p+1+n, cmp );
        dp[0][0] = 0.0;
        for( int i = 1; i <= m; i ++ ) dp[0][i] = 0.0;
        for( i = 1; i <= n; i ++ ){
            for( j = 0; j <= m; j ++ ){
                dp[i][j] = dp[i-1][j];
                if( j >= 2 ) dp[i][j] = max( dp[i][j], dp[i-1][j-1]+p[i].a );
                if( j == 1 ) dp[i][j] = max( dp[i][j], dp[i-1][j-1]+p[i].a+p[i].b );
            }
        }
        printf("%.10f\n", dp[n][m]);
    }
}
