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


VI G[400];
int match[400];
bool used[400];

bool h(int u) {
	used[u] = 1;
	REP(i,G[u].size()) {
		int v = G[u][i], w = match[v];
		if(w < 0 || ! used[w] && h(w)) {
			match[v] = u;
			match[u] = v;
			return 1;
		}
	}
	return 0;
}

int hungary(int n) {
	int res = 0;
	CLR(match, -1);
	REP(v, n) {
		if(match[v] < 0) {
			CLR(used, 0);
			if(h(v)) res ++;
		}
	}
	return res;
}


char ch[4] = {'.','+','x','o'};
int a[200][200];
int b[200][200];
int v[4][400];
int main()
{
#ifdef LOCAL
	   freopen("D-large.in","r",stdin);
	   freopen("D-large.out","w",stdout);
#endif
	ios::sync_with_stdio(false);
	int t,cs=1;
	cin>>t;
	while(t--) {
        int n,m;
        cin>>n>>m;
        REP(i,n)
        REP(j,n)
            a[i][j] = b[i][j] = 0;
        memset(v,0,sizeof(v));
        REP(i,m) {
            char c;
            int x,y;
            cin>>c>>x>>y;
            x--; y--;
            if(c == 'o') {
                a[x][y] = 3;
            }else if(c == '+') {
                a[x][y] = 1;
            }else if(c == 'x') {
                a[x][y] = 2;
            }
        }
        REP(i,n)
        REP(j,n) {
            b[i][j] = a[i][j];
            if(a[i][j] & 1) {
                v[2][i+j]=1;
                v[3][i-j+n-1]=1;
            }
            if(a[i][j] & 2) {
                v[0][i]=1;
                v[1][j]=1;
            }
        }
        vector<int> not_vis[4];
        REP(i,n) if(!v[0][i]) not_vis[0].PB(i);
        REP(i,n) if(!v[1][i]) not_vis[1].PB(i);
        REP(i,n*2-1) if(!v[2][i]) not_vis[2].PB(i);
        REP(i,n*2-1) if(!v[3][i]) not_vis[3].PB(i);
        assert(not_vis[0].size() == not_vis[1].size());
        assert(not_vis[2].size() == not_vis[3].size());
        REP(i,not_vis[0].size()) {
            int x=not_vis[0][i];
            int y=not_vis[1][i];
            b[x][y] |= 2;
        }
        REP(i,400) G[i].clear();
        int ans = n;
        ans += n*2-1 - (int)not_vis[2].size();
        REP(i,not_vis[2].size()) {
            REP(j,not_vis[3].size()) {
                int A=not_vis[2][i];
                int B=not_vis[3][j];
                int x=((A+B)-n+1)/2;
                int y=A-x;
                if(x >= 0 && y >= 0 && x < n && y < n && x-y+n-1 == B) {
                    G[A].PB(B+200);
                    G[B+200].PB(A);
                }
            }
        }
        ans += hungary(400);
        
        REP(i,not_vis[2].size()) {
            int A=not_vis[2][i];
            int B=match[A] - 200;
            int x=((A+B)-n+1)/2;
            int y=A-x;
            if(B >= 0) {
                b[x][y] |= 1;
            }
        }
        vector<pair<int,int> > vec;
        REP(i,n)
        REP(j,n)
            if(a[i][j] != b[i][j])
                vec.PB(MP(i,j));
        
        cout<<"Case #"<<cs++<<": "<<ans<<' '<<vec.size()<<endl;
        REP(i,vec.size()) {
            auto p = vec[i];
            cout<<ch[b[p.X][p.Y]]<<' '<<p.X+1<<' '<<p.Y+1<<endl;
        }
	}
	return 0;
}
