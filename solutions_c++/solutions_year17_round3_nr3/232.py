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

const int N_MAX = 55;
double p[N_MAX];

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1; kase<=t; kase++) {
		printf("Case #%d: ", kase);
		int n, k;
		double u;
		scanf("%d%d%lf", &n, &k, &u);
		for(int i=0; i<n; i++)
			scanf("%lf", p+i);
		sort(p, p+n);
		p[n] = 1;
		for(int i=0; i<n; i++) {
			double tmp = (p[i+1]-p[i])*(i+1);
			if(tmp < u) {
				for(int j=0; j<=i; j++)
					p[j] = p[i+1];
				u -= tmp;
			} else {
				double rate = u/(i+1);
				for(int j=0; j<=i; j++)
					p[j] += rate;
				break;
			}
		}
		double ans=1;
		for(int i=0; i<n; i++)
			ans *= p[i];
		printf("%.10f\n", ans);
	}
	return 0;
}
