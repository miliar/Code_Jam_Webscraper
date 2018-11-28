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
const int N = int(3e5), mod = int(1e9)  + 7;
int T;

int d,n, k[N], s[N];

void solve(){
	scanf("%d%d",&d,&n);
	double ans = 0.0;
	for(int i = 1; i <= n; i++){
		scanf("%d%d",&k[i],&s[i]);
		ans = min(ans, (1ll * d * s[i] + 0.0) / (d - k[i]));
		if(i == 1) ans = (1ll * d * s[i] + 0.0) / (d - k[i]);
	}
	printf("%.12lf\n", ans);
}

int main () {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++){
		printf("Case #%d: ",tt);
		solve();
	}

return 0;
}