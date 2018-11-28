#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int,int> pii;

#define fi first
#define se second
#define mp make_pair
#define pb push_back

int t;
const int MAXN = 1000;
pii ar[MAXN + 4];
int main(){
	scanf("%d", &t);
	for(int tc = 1; tc <= t; ++tc){
		double maxtime = 0;
		int n, d;
		scanf("%d%d", &d, &n);
		for(int i = 0;i < n; ++i){
			scanf("%d%d", &ar[i].fi, &ar[i].se);
			int dist = d - ar[i].fi;
			maxtime = max(maxtime, dist / (double) ar[i].se);
		}

		printf("Case #%d: %lf\n", tc, d / maxtime);

	}
	return 0;
}