#include <bits/stdc++.h>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define INF 0x3F3F3F3F
#define MP(X,Y) make_pair(X,Y)
#define PB(X) push_back(X)
#define REP(X,N) for(int X=0;X<N;X++)
#define REP2(X,L,R) for(int X=L;X<=R;X++)
#define DEP(X,R,L) for(int X=R;X>=L;X--)
#define CLR(A,X) memset(A,X,sizeof(A))
#define IT iterator
#define RIT reverse_iterator
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> PII;
typedef vector<PII> VII;
typedef vector<int> VI;
typedef tree<int, null_type, greater<int>, rb_tree_tag, tree_order_statistics_node_update > rb_tree_set;
typedef tree<int, int, greater<int>, rb_tree_tag, tree_order_statistics_node_update > rb_tree;
#define PQ std::priority_queue
#define HEAP __gnu_pbds::priority_queue
#define X first
#define Y second
#define lson(X) ((X)<<1)
#define rson(X) ((X)<<1|1)

#define FILE_NAME "C-large"

int e[110];
int s[110];
ll d[110][110];
double dp[110][110];

int main()
{
#ifdef LOCAL
    freopen(FILE_NAME ".in","r",stdin);
    freopen(FILE_NAME ".out","w",stdout);
#endif // LOCAL
    ios::sync_with_stdio(false);
    int t,cs=1;
    cin>>t;
    while(t--) {
        int n,q;
        cin>>n>>q;
        REP(i,n) cin>>e[i]>>s[i];
        REP(i,n)
        REP(j,n) {
            cin>>d[i][j];
            if(d[i][j] == -1) d[i][j] = LINF;
        }
        REP(k,n)
        REP(i,n)
        REP(j,n) {
            d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
        }
        REP(i,n)
        REP(j,n) {
            if(d[i][j] <= e[i]) {
                dp[i][j] = 1.0 * d[i][j] / s[i];
            }else{
                dp[i][j] = 1e100;
            }
        }
        REP(k,n)
        REP(i,n)
        REP(j,n) {
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
        }
        
        cout<<"Case #"<<cs++<<":";
        REP(i,q) {
            int u, v;
            cin>>u>>v;
            u--; v--;
            cout<<' '<<fixed<<setprecision(6)<<dp[u][v];
        }
        cout<<endl;
    }
    return 0;
}

