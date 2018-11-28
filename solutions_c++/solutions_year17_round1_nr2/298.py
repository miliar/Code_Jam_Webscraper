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

const int MAXN = 50 + 10;
const int MAXX = 1000000+10;

int r[MAXN], ptr[MAXN];
int q[MAXN][MAXN];

int main() {
	int T;
	scanf("%d", &T);
	for(int kase=1; kase<=T; kase++) {
		int n, p;
		scanf("%d%d", &n, &p);
		for(int i=0; i<n; i++)	scanf("%d", r+i);
		for(int i=0; i<n; i++) {
			for(int j=0; j<p; j++)	scanf("%d", q[i]+j);
			sort(q[i], q[i]+p);
		}

		fill(ptr, ptr+n, 0);
		int ans = 0;
		bool GG = false;
		while(1) {
			bool flag = false;
			int mx = 0;
			for(int i=0; i<n; i++) {
				if((10*q[i][ptr[i]])/(9*r[i]) < mx) {
					ptr[i]++;
					if(ptr[i] == p)	GG = true;
					flag = true;
					break;
				}
				mx = max(mx, (10*q[i][ptr[i]]-1)/(11*r[i])+1);
			}
			if(GG)	break;
			for(int i=n-1; i>=0 && !flag; i--) {
				if((10*q[i][ptr[i]])/(9*r[i]) < mx) {
					ptr[i]++;
					if(ptr[i] == p)	GG = true;
					flag = true;
					break;
				}
				mx = max(mx, (10*q[i][ptr[i]]-1)/(11*r[i])+1);
			}
			if(GG)	break;
			if(!flag) {
				ans++;
				for(int i=0; i<n; i++) {
					ptr[i]++;
					if(ptr[i] == p)	GG = true;
				}
			}
			if(GG)	break;
			//for(int k2=(10*Q-1)/(11*R)+1; k2<=(10*Q)/(9*R); k2++) {
		}

		printf("Case #%d: %d\n", kase, ans);
	}
    
    return 0;
}
