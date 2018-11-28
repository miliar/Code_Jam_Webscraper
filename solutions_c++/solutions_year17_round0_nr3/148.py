#include <bits/stdc++.h>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace std;
using namespace __gnu_cxx;
using namespace __gnu_pbds;
#define XINF INT_MAX
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

int main()
{
#ifdef LOCAL
	   freopen("C-large.in","r",stdin);
	   freopen("C-large.out","w",stdout);
#endif
	ios::sync_with_stdio(false);
	int t,cs=1;
	cin>>t;
	while(t--) {
        ll n,m;
        cin>>n>>m;
        ll a = n, c1 = 1, c2 = 0;
        ll ans = 0;
        while(1) {
            if(m <= c1) {ans = a; break;}
            m -= c1;
            if(m <= c2) {ans = a-1; break;}
            m -= c2;
            if((a-1)%2==0) {
                c1 = c1*2 + c2;
                c2 = c2;
            }else{
                c2 = c1 + c2*2;
                c1 = c1;
            }
            a = a-1 - (a-1)/2;
        }
        cout<<"Case #"<<cs++<<": ";
        cout<<ans-1-(ans-1)/2<<' '<<(ans-1)/2<<endl;
	}
	return 0;
}
