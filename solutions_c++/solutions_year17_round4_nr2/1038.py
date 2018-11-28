#include <bits/stdc++.h>
#define maxx 100005
#define inf 2000000000
#define mod 1000000007
#define pii pair<int,int>
#define piii pair<pii,pii>
#define pli pair<long long,int>
#define pll pair<long long,long long>
#define f first
#define s second
#define in(x) scanf("%d",&x)
#define IN(x) scanf("%lld",&x)
#define inch(x) scanf("%s",x)
#define indo(x) scanf("%lf",&x)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;

using namespace std;

int t, n, c, m, p, b;
int C[3][1234], cnt[3];
int main()
{
    freopen("input.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    in(t);
    for(int cases = 1; cases <= t; cases ++){
        in(n); in(c); in(m);
        memset(C, 0, sizeof(C));
        memset(cnt, 0, sizeof(cnt));
        for(int i = 1; i <= m; i++){
            in(p); in(b);
            C[b][p]++;
            cnt[b]++;
        }
        int y = max(cnt[1], cnt[2]);
        int z = 0;
        y = max(y, C[1][1] + C[2][1]);
        for(int i = n; i >= 2; i--){
            if(C[1][i] + C[2][i] > y){
                z += (C[1][i] + C[2][i] - y);
            }
        }
        printf("Case #%d: ",cases);
        printf("%d %d\n", y, z);
    }
    return 0;
}
