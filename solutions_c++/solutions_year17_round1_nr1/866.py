#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace std;
using namespace __gnu_pbds;
typedef long long int LL;
typedef pair<int,int> PII;
typedef pair<LL , LL> PLL;
typedef pair< LL , LL > PLL;
typedef vector< int > VI;
typedef vector< LL > VLL;
typedef vector< PII > VPII;
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
///------------------------------------------------------------
#define MAX 30
#define INF 0x3f3f3f3f

char x[MAX][MAX];
int use[MAX][MAX];
int t , n , m;
int main(){
    cin >> t;
    REPNM(times , 1 , t + 1){
    	MEM(use , 0);

    	cin >> n >> m;
    	REP(i , n) REP(j , m) cin >> x[i][j];
    	REP(i , n){
    		REP(j , m){
    			if(x[i][j] != '?'){
    				RREP(k , j , 0){
    					if(use[i][k]) break;
    					use[i][k] = 1;
    					x[i][k] = x[i][j];
    				}
    			}
    		}
    		RREP(j , m - 1 , 0){
    			if(x[i][j] != '?'){
    				REPNM(k , j + 1 , m){
    					if(use[i][k]) break;
    					use[i][k] = 1;
    					x[i][k] = x[i][j];
    				}
    			}
    		}
    	}
    	REP(qq , 100){
    		REPNM(j , 1 , n){
    			if(use[j][0] == 0 && use[j - 1][0] == 1){
    				REPNM(k , 0 , m) x[j][k] = x[j - 1][k] , use[j][k] = 1;
    			}
    		}
    		REPNM(j , 0 , n - 1){
    			if(use[j][0] == 0 && use[j + 1][0] == 1){
    				REPNM(k , 0 , m) x[j][k] = x[j + 1][k] , use[j][k] = 1;
    			}
    		}
    	}
    	cout << "Case #" << times << ":" << endl;
    	REP(i , n){
    		REP(j , m) cout << x[i][j] ;
    		cout << endl;
    	}
    }

    
    return 0;
}