#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace std;
using namespace __gnu_pbds;
#define REP(i,j)       for(int i = 0 ; i < j ; i++)
#define REPNM(i,j,k)   for(int i = j ; i < k ; i++)
#define RREP(i,j,k)    for(int i = j ; i >=k ; i--)
#define LREP(i,j)      for(LL  i = 0 ; i < j ; i++)
#define LREPNM(i,j,k)  for(LL  i = j ; i < k ; i++)
#define LRREP(i,j,k)   for(LL  i = j ; i >=k ; i--)
#define pb   push_back
#define mp   make_pair
#define A    first
#define B    second
#define MEM(i,j)   memset(i,j,sizeof i)
#define ALL(i)     i.begin(),i.end()
#define DBGG(i,j)     cout << i << " " << j << endl
#define DB4(i,j,k,l)  cout << i << " " << j << " " << k << " " << l << endl
#define RI(i)       scanf("%d" , &i)
#define RII(i,j)    scanf("%d%d" , &i , &j)
#define RIII(i,j,k) scanf("%d%d%d" , &i , &j , &k)
#define RL(i)       scanf("%lld" , &i)
#define RLL(i,j)    scanf("%lld%lld" , &i , &j)
#define RLLL(i,j,k) scanf("%lld%lld%lld" , &i , &j , &k)
#define AS assert
#define IOS cin.tie() , cout.sync_with_stdio(0)
typedef long long int LL;
typedef pair<int,int> PII;
typedef pair<LL , LL> PLL;
typedef pair< LL , LL > PLL;
typedef vector< int > VI;
typedef vector< LL > VLL;
typedef vector< PII > VPII;
///------------------------------------------------------------
#define int long long
#define MAX 100
#define INF 0x3f3f3f3f
/*
100
1 8
10
1 7 5 8 4 2 3 6
*/
int t , n , m , x[MAX] , a[MAX][MAX];
PLL b[MAX][MAX];
VLL g;
int32_t main(){
    cin >> t;
    REPNM(times , 1 , t + 1){
    	// if(t == 42) assert(0);
    	MEM(x , 0) , MEM(a , 0) , MEM(b , 0) , g.clear();

    	cin >> n >> m;
    	REP(i , n) cin >> x[i];
    	// cout << "here" << endl;
    	REP(i , n){
    		REP(j , m) cin >> a[j][i];
    	}
    	REP(i , m){
    		// int u = INF , d = 0;
    		REP(j , n){
    			int now = 0 , qu , qd;
    			RREP(k , 25 , 0){
    				int tmp = now + (1 << k);
    				double q = tmp * x[j];
    				if(q * 9 <= a[i][j] * 10) now = tmp;
    			}
    			qu = now , now = 3000000;
    			RREP(k , 25 , 0){
    				int tmp = now - (1 << k);
    				double q = tmp * x[j];
    				if(q * 11 >= a[i][j] * 10) now = tmp;
    			}
    			qd = now , now = 0;
    			if(qu >= qd) b[j][i] = mp(qu , qd) , g.pb(qu) , g.pb(qd);
    			else b[j][i] = mp(-1 , -1);
    			// DBGG(qu , qd);
    			// u = min(u , qu);
    			// d = max(d , qd);
    		}
    		// if(u >= d) ans ++;
    	}
    	REP(i , n) sort(b[i] , b[i] + m);
    	int ans = 0;
    	sort(ALL(g));
    	for(auto i : g){
    		VI sol;
    		REP(j , n){
    			REP(k , m) if(b[j][k].A != -1 && b[j][k].B <= i && i <= b[j][k].A){
    				sol.pb(k);
    				break;
    			}
    		}
    		if(sol.size() == n){
    			REP(w , sol.size()) b[w][sol[w]] = mp(-1 , -1);
    			ans ++;
    		}

    	}
    	cout << "Case #" << times << ": " << ans << endl;
    }

    
    return 0;
}