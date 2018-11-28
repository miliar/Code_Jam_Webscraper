#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <cstring>
#include <map>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <bitset>
#define f first
#define s second
#define ll long long
#define ull unsigned long long
#define mp make_pair
#define pb push_back
#define vi vector <int>
#define ld long double
#define pii pair<int, int>
using namespace std;    
const int N = 110, mod = int(1e9)  + 7;
int T;

int r[5],p,n;

int d2[N][N][N];
int d3[N][N][N];
int d4[N][N][N];
int sum;

int calc2(int n,int a,int b){
	if(d2[n][a][b] != -1) return d2[n][a][b];
	if(n == 0) return 0;
	int res = 0;
	int cur = (sum - b);
	if(a > 0){
		int ct = 0;
		if(cur % p == 0) ct++;
		res = max(res, calc2(n - 1, a - 1, b) + ct);
	}
	if(b > 0){
		int ct = 0;
		if(cur % p == 0) ct++;
		res = max(res, calc2(n - 1, a,b - 1) + ct);
	}
	return d2[n][a][b] = res;
}

int calc3(int n,int a,int b){
	if(d3[n][a][b] != -1) return d3[n][a][b];
	if(n == 0) return 0;
	int res = 0;
	int cur = (sum - b - 2 * (n - a - b));
	if(a > 0){
		int ct = 0;
		if(cur % p == 0) ct++;
		res = max(res, calc3(n - 1, a - 1, b) + ct);
	}
	if(b > 0){
		int ct = 0;
		if(cur % p == 0) ct++;
		res = max(res, calc3(n - 1, a,b - 1) + ct);
	}
	if(n > a + b){
		int ct = 0;
		if(cur % p == 0) ct++;
		res = max(res, calc3(n - 1, a, b) + ct);
	}
	return d3[n][a][b] = res;
}

int calc4(int n,int a,int b){
	if(d4[n][a][b] != -1) return d4[n][a][b];
	if(n == 0) return 0;
	int res = 0;
	int cur = (sum - a - 2 * b - 3 * (n - a - b));
	int ct = 0;
	if(cur % p == 0) ct++;
	if(a > 0) res = max(res, calc4(n - 1, a - 1,b));
	if(b > 0) res = max(res, calc4(n - 1, a, b - 1));
	if(n > a + b) res = max(res, calc4(n - 1,a,b));
	return d4[n][a][b] = res + ct;
}

void solve(){
	scanf("%d%d",&n,&p);
	for(int i = 0; i < p; i++) r[i] = 0;
	sum = 0;
	if(p == 2) memset(d2,-1, sizeof(d2));
	if(p == 3) memset(d3,-1, sizeof(d3));
	if(p == 4) memset(d4,-1, sizeof(d4));
	for(int i = 1,x; i <= n; i++){
		scanf("%d",&x);
		r[x%p]++;
		sum = sum + x;
	}
	if(p == 2){
		printf("%d\n",calc2(n,r[0],r[1]));
		return;
	}
	if(p == 3){
		printf("%d\n", min(r[0],n) + calc3(n - r[0],0, r[1]));
		return;
	}
	printf("%d\n", r[0] + calc4(n - r[0], r[1],r[2]));
}

int main () {
	freopen("in","r",stdin);
	freopen("ans","w",stdout);
	scanf("%d",&T);
	memset(d2,-1, sizeof(d2));
	memset(d3,-1, sizeof(d3));
	memset(d4,-1, sizeof(d4));
	for(int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}

return 0;
}