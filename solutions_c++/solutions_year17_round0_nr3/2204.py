#include <bits/stdc++.h>
using namespace std;
typedef long long int LL;
typedef pair<LL , LL> PLL;
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
#define int unsigned long long
#define MAX 
#define INF 0x3f3f3f3f
map<int , int> cc;
set<int> use;
PLL F(int now){
	if(now & 1LL) return mp(now / 2 , now / 2);
	else return mp(now / 2 , now / 2 - 1);
}
PLL solve(int n , int m){
	priority_queue<int> pq;
	pq.push(n) , cc[n] = 1;
	int cnt = 0;
	while(pq.size()){
		int now = pq.top() ; pq.pop();
		if(cc[now] + cnt >= m) return F(now);
		else {
			cnt += cc[now];
			if(now & 1){
				cc[now / 2] += cc[now] + cc[now];
				if(use.find(now / 2) == use.end()) use.insert(now / 2) , pq.push(now / 2);
			}
			else {
				cc[now / 2] += cc[now];
				cc[now / 2 - 1] += cc[now];
				if(use.find(now / 2) == use.end()) use.insert(now / 2) , pq.push(now / 2);
				if(use.find(now / 2 - 1) == use.end()) use.insert(now / 2 - 1) , pq.push(now / 2 - 1);
				
			}
		}
	}
	return mp(-1 , -1);
}
int t , n , m;
int32_t main(){
    cin >> t;
    REPNM(times , 1 , t + 1){
    	cc.clear();
    	use.clear();
    	cin >> n >> m;
    	PLL ans = solve(n , m);
    	assert(ans.A != -1);
    	cout << "Case #" << times << ": " << ans.A << " " << ans.B << endl;
    }
    return 0;
}