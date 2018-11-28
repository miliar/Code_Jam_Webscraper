#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<map>
#include<cassert>
#include<deque>

using namespace std;

#define sz(x) (int)(x.size())
#define rep(i,a,b) for(int i=a;i<b;++i)
#define per(i,a,b) for(int i=a-1;i>=b;--i)
#define pb push_back
#define mp make_pair
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
////////////////////////

int const N = 1e3 + 41;
int const INF = 1e9 + 41;

int cntP[N], cntC[N], c, m, n, a[N];

void printTest(int test){
	printf("Case #%d: ",test);
}

int can(int maxi){
	int ret = 0;
	rep(i, 0, n) a[i] = cntP[i];
	for(int i=n-1;i>0;--i){
		if(a[i] <= maxi) continue;
		int add = a[i] - maxi;
		for(int j=i-1;j>=0 && add > 0;--j){
			if(a[j] >= maxi) continue;
			int mini = min(maxi - a[j], add);
			add -= mini;
			ret += mini;
		}
		if(add > 0){
			return INF;
		}
		a[i] -= add;
	}
	if(a[0] > maxi) ret = INF;
	return ret;
}

void clear(){
	rep(i, 0, N) cntP[i] = cntC[i] = a[i] = 0;
}

void solve(int test){
	printTest(test);
	clear();
	cin >> n >> c >> m;
	rep(i, 0, m){
		int pi, ci;
		cin >> pi >> ci;
		--pi;--ci;
		++cntP[pi];
		++cntC[ci];
	}
	int ans = 0;
	rep(i, 0, c) ans = max(ans, cntC[i]);
	rep(i, ans, N){
		int ans2 = can(i);
		if(ans2 != INF){
			printf("%d %d\n", i,ans2);
			return;
		}
	}

}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int testCnt;
	cin >> testCnt;
	rep(test,1,testCnt+1){
		solve(test);
	}

	return 0;
}


