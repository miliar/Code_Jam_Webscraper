#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<queue>
#include<utility>
#include<bitset>
#include<complex>
#include<map>
#include<set>
#include<unordered_map>
#include<unordered_set>

using namespace std;

#define mem(a,b) memset(a,b,sizeof(a))
#define REP(i,a,b) for(int i=a; i<=b; ++i)
#define FOR(i,a,b) for(int i=a; i<b; ++i)
#define MP make_pair
typedef long long LL;
typedef pair<int,int> pii;

const int maxn = 1000;
const double PI = acos(-1.0);

int n, kk;
int arr[maxn+5], Ri[maxn+5], Hi[maxn+5];
double f[maxn+5];

bool cmp(const int &a, const int &b) {
	return Ri[a] > Ri[b];
}

inline double SideArea(int x) {
	return double(Ri[x]) * 2.0 * PI * Hi[x];
}

inline double TopArea(int x) {
	return double(Ri[x]) * Ri[x] * PI;
}

int main() {
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t) {
		scanf("%d%d", &n, &kk);
		REP(i,1,n) {
			scanf("%d%d", Ri+i, Hi+i);
			arr[i] = i;
		}
		sort(arr+1, arr+1+n, cmp);
		mem(f, 0);
		for(int i = 1; i <= n; ++i) {
			double area = SideArea(arr[i]);
			for(int k = kk; k >= 2; --k)
				f[k] = max(f[k], f[k-1] + area);
			f[1] = max(f[1], area + TopArea(arr[i]));
		}
		printf("Case #%d: %.9f\n", t, f[kk]);
	}
	return 0;
}
