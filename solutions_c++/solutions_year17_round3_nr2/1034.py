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
const int N = 2405;
int vis[2][N];

struct interval
{
    int l, r, id;
}p[N];

bool cmp( interval a, interval b )
{
    return a.l < b.l;
}

int main()
{
    int n, m, i, j, T, cas = 1, k;
    freopen("B-small-attempt0 (1).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while(T--){
        printf("Case #%d: ", cas++);
        scanf("%d%d", &m, &k);
        n = m+k;
        int ans = 0;
        for( i = 1; i <= n; i ++ ){
            scanf("%d%d", &p[i].l, &p[i].r);
            if( i <= m ) p[i].id = 0;
            else p[i].id = 1;
        }
        sort( p+1, p+1+n, cmp );
        int s[2]={0,0}, sum = 0, c[2]={0,0};// s must  c choose
        memset( vis, 0, sizeof(vis) );
        p[n+1] = p[1]; p[n+1].l += 1440, p[n+1].r += 1440;
        for( i = 1; i <= n+1; i ++ ){
            if( i != 1 ){
                if( p[i].id != p[i-1].id ){
                    ans ++;
                    sum += p[i].l-p[i-1].r;
                }
                else{
                    s[p[i].id] += p[i].r-p[i].l;
                    c[p[i].id] += p[i].l-p[i-1].r;
                    vis[p[i].id][p[i].l-p[i-1].r] ++;
                }
            }
        }
        if( s[0]+c[0] <= 720 && s[1]+c[1] <= 720 ){
            printf("%d\n", ans);
            continue;
        }
        int fl = 0;
        if( s[0]+c[0]+sum < s[1]+c[1] ) fl = 1;
        sum += s[fl] + c[fl];
        for( int i = 2000; i >= 0; i -- ){
            while( vis[fl][i] ){
                ans += 2;
                sum -= i;
                vis[fl][i] --;
                if( sum <= 720 ){
                    break;
                }
            }
            if( sum <= 720 ) break;
        }
        printf("%d\n", ans);
    }
}
