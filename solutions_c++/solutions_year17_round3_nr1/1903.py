#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

#define IT(a,it) for(auto it=a.begin(); it != a.end(); it++)
#define REV_IT(a,it) for(auto it=a.rbegin(); it != a.rend(); it++)
#define LL long long
#define LD long double
#define MP make_pair
#define FF first
#define SS second
#define PB push_back
#define INF (int)(1e9)
#define EPS (double)(1e-9)
#define PI 3.141592653589793

#ifndef ONLINE_JUDGE
#  define LOG(x) cerr << #x << " = " << (x) << endl
#else
#  define LOG(x) 0
#endif

#define MAXX 2005

using namespace std;

typedef pair <LL, LL> pi_i;
typedef pair<int, pi_i> pi_ii;

bool cmp(int a, int b){ return a>b; }
template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> T lcm(T a, T b) { return a * (b / gcd(a, b)); }

LL n, k, r[MAXX], h[MAXX], dp[MAXX][MAXX];
LD dpp[MAXX][MAXX];
vector< pi_i > vv;

/*LL solve(int idx, int kk){
	if(idx == n){
		//LOG(kk);
		if(kk != k) return -1000000000000LL;
		return 0;
	}
	if(dp[idx][kk] != -1) return dp[idx][kk];
	LL ans = solve(idx + 1, kk+1) + (2LL * vv[idx].FF * vv[idx].SS);
	if(kk > 0) ans = max(ans, solve(idx + 1, kk));
	return dp[idx][kk] = ans;
}*/
LD solve(int idx, int kk, int st){
	if(idx == n){
		if(kk != k) return -100000000000000000.00;
		return 0;
	}
	LD ans = 0;
	if(dp[idx][kk] != -1) return dpp[idx][kk];
	if(st == 0){
		ans = solve(idx+1, kk+1, 1) + (((2LL * vv[idx].FF * vv[idx].SS) + ( vv[idx].FF*vv[idx].FF )) * PI);
		ans = max(ans, solve(idx+1, kk, 0) );
	}else{
		ans = solve(idx+1, kk+1, 1) + ((2LL * vv[idx].FF * vv[idx].SS) * PI);
		ans = max(ans, solve(idx+1, kk, 1) );
	}
	dp[idx][kk] = 1;
	return dpp[idx][kk] = ans;
}

int main(){
	ios_base::sync_with_stdio(false);
	
	freopen("in.txt","r",stdin);
	freopen("out3.txt","w",stdout);
	
	int T, casee = 1;
	cin >> T;
	for(casee=1;casee<=T;casee++){
		cout << "Case #" << casee << ": " ;
		vv.clear();
		cin >> n >> k;
		memset(dp, -1LL, sizeof dp);
		for(int i = 0;i < n;i++){
			cin >> r[i] >> h[i];
			vv.PB(MP(r[i], h[i]));
		}
		sort(vv.begin(), vv.end());
		reverse(vv.begin(), vv.end());
		LD ans = solve(0, 0, 0);
		//LOG(ans);
		cout << fixed << setprecision(9) << ans<< endl;
	}
	
	//fclose(stdin);
	//fclose(stdout);
return 0;	
}

