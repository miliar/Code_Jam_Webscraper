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
///------------------------------------------------------------
typedef long long int LL;
typedef pair<int,int> PII;
typedef pair<LL , LL> PLL;
typedef pair< LL , LL > PLL;
typedef vector< int > VI;
typedef vector< LL > VLL;
typedef vector< PII > VPII;
#define MAX 30000
#define INF 0x3f3f3f3f

int t;
char qq[] = {'R' , 'Y' , 'B'};
int main(){
	cin >> t;
	REPNM(times , 1 , t + 1){
		int q , a[3] , ok = 1;
		PII b[3];
		cin >> q >> a[0] >> q >> a[1] >> q >> a[2] >> q;
		REP(i , 3) b[i].A = a[i] , b[i].B = i;
		sort(a , a + 3 , greater<int>());
		sort(b , b + 3 , greater<PII>());
		VI sol;
		if(a[0] == 1){
			REP(i , a[0]) sol.pb(0);
			REP(i , a[1]) sol.pb(1);
			REP(i , a[2]) sol.pb(2);
		}
		else {
			REP(i , a[0]) sol.pb(0);
			REP(i , a[1]){
				if(sol[0] == sol.back()){
					sol.insert(sol.begin() , 1);
					continue;
				}
				REP(j , sol.size() - 1){
					if(sol[j] == 0 && sol[j + 1] == 0){
						sol.insert(sol.begin() + j + 1 , 1);
						break;
					}
				}
			}
			REP(i , a[2]){
				int qok = 1;
				REP(j , sol.size() - 1){
					if(sol[j] == sol[j + 1]){
						sol.insert(sol.begin() + j + 1 , 2);
						qok = 0;
						break;
					}
				}
				if(qok == 0) continue;
				REP(j , sol.size() - 1){
					if(sol[j] != 2 && sol[j + 1] != 2){
						sol.insert(sol.begin() + j + 1 , 2);
						break;
					}
				}
			}
		}
		REP(i , sol.size() - 1) if(sol[i] == sol[i + 1]) ok = 0;
		if(sol.size() > 1 && sol[0] == sol.back()) ok = 0;
		
		if(ok == 0) printf("Case #%d: IMPOSSIBLE\n" , times);
		else {
			printf("Case #%d: " , times);
			for(auto i : sol) printf("%c", qq[b[i].B]);puts("");
		}
	}    
    return 0;
}