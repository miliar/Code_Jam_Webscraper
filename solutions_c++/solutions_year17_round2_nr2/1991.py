#include <bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define pii pair<int, int>
#define pll pair<long long, long long>r
#define pb  push_back
#define mp  make_pair
#define pq priority_queue
#define FIN(x) freopen(x,"r",stdin)
#define FOUT(x) freopen(x,"w",stdout)
#define ALL(x) x.begin(),x.end()
#define M(a,x) memset(a,x,sizeof(a))
#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
#define scs(x) scanf("%s",x);
#define SZ(x) (int)x.size()
#define print(x) printf("%d",x);
#define nl printf("\n")
#define fr first
#define se second
#define printl(x) printf("%lld",x)
#define F(i,a,n) for(int i=a;i<n;i++)
#define INF 4000000000000000000LL
#define LL long long

int N,R,O,Y,G,B,V;
vector < char > ans;
int fst = -1;
int cs = 0;
vector < vector < vector < vector < int > > > > dp;
bool solve(int pos,int r,int y,int b,int last){
	if(pos == N){
		if(last != fst){
		  return true;
		}
		return false;
	}
	if(dp[r][y][b][last] != -1) return dp[r][y][b][last];
	if(pos == 0){
		if(r){
			fst = 0;
			ans.push_back('R');
			if(solve(pos+1,r-1,y,b,0)){
				return dp[r][y][b][last] =true;
			}
			ans.pop_back();
		}
		if(y){
			fst = 1;
			ans.push_back('Y');
			if(solve(pos+1,r,y-1,b,1)){
				return dp[r][y][b][last] = true;
			}
			ans.pop_back();
		}
		if(b){
			fst = 2;
			ans.push_back('B');
			if(solve(pos+1,r,y,b-1,2)){
				return dp[r][y][b][last] = true;
			}
			ans.pop_back();
		}
	}
	else {
			if(r && last != 0){
				ans.push_back('R');
				if(solve(pos+1,r-1,y,b,0)){
				return dp[r][y][b][last] = true;
				}
				ans.pop_back();
			}
		if(y && last != 1){
			ans.push_back('Y');
			if(solve(pos+1,r,y-1,b,1)){
				return dp[r][y][b][last]  = true;
			}
			ans.pop_back();
		}
		if(b && last != 2){
			ans.push_back('B');
			if(solve(pos+1,r,y,b-1,2)){
				return dp[r][y][b][last] = true;
			}
			ans.pop_back();
		}
	}
	return dp[r][y][b][last] = false;
}
int main() {
	int t;
	cin >> t;
	while(t--){
		fst = -1;
		ans.clear();
		cin >> N >> R >> O >> Y >> G >> B >> V;
		dp.resize(R+1);
		for(int i = 0 ; i <= R ; i++){
			dp[i].resize(Y+1);
		}
		for(int i = 0 ; i <= R ; i++){
			for(int j = 0 ; j<= Y ; j++){
				dp[i][j].resize(B+1);
			}
		}
		for(int i = 0 ;i<= R ; i++){
			for(int j =0  ;j<= Y ; j++){
				for(int k = 0 ; k<= B ; k++){
					dp[i][j][k].resize(3);
				}
			}
		}
		for(int i = 0 ; i <= R ; i++){
			for(int j = 0 ;j<= Y ; j++){
				for(int k = 0; k<= B ; k++){
					for(int u = 0 ;u < 3 ; u++){
						dp[i][j][k][u] = -1;
					}
				}
			}
		}
		if(solve(0,R,Y,B,0)){
			printf("Case #%d: ",++cs);
			for(auto x : ans){
				cout <<x ;
			}
			cout << endl;
		}
		else {
		  printf("Case #%d: ",++cs);
		  cout <<"IMPOSSIBLE\n";	
		}
	}
}