#include <bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define SZ(x) ((int)(x).size())
#define ALL(x) (x).begin(),(x).end()
#ifdef _DEBUG_
	#define debug(...) printf(__VA_ARGS__)
#else
	#define debug(...) (void)0
#endif
using namespace std;
typedef long long ll;
typedef pair<int,int> PII;
typedef vector<int> VI;

const int N_MAX = 1010;
int tic[N_MAX];
int cnt[N_MAX];

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1;kase<=t;kase++) {
		printf("Case #%d: ", kase);
		int n, m, c;
		scanf("%d%d%d", &n, &c, &m);
		memset(tic, 0, sizeof(tic));
		memset(cnt, 0, sizeof(cnt));
		for(int i=0; i<m; i++) {
			int p, b;
			scanf("%d%d", &p, &b);
			tic[p]++;
			cnt[b]++;
		}
		int rds=0, sum=0;
		for(int i=1; i<=c; i++)
			rds = max(rds, cnt[i]);
		for(int i=1; i<=n; i++) {
			sum += tic[i];
			rds = max(rds, (sum-1)/i+1);
		}
		int pmt=0, ptr=1;
		for(int i=n; i>=1; i--) {
			int x = tic[i] - rds;
			if(x>0)
				pmt+=x;
			while(x>0) {
				if(tic[ptr]>=rds)
					ptr++;
				else {
					x -= min(rds-tic[ptr], x);
				}
			}
		}
		printf("%d %d\n", rds, pmt);
	}
	return 0;
}
