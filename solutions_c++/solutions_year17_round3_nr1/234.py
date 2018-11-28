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

const double PI = acos(-1);

const int N_MAX = 1010;
PII p[N_MAX];

double side(PII x) {
	return PI*2*x.F*x.S;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int kase=1; kase<=t; kase++) {
		printf("Case #%d: ", kase);
		int n, k;
		scanf("%d%d", &n, &k);
		for(int i=0; i<n; i++)
			scanf("%d%d", &p[i].F, &p[i].S);
		sort(p, p+n);
		double ans=0;
		for(int i=k-1; i<n; i++) {
			double s = side(p[i]) + PI*p[i].F*p[i].F;
			priority_queue<double, vector<double>, greater<double> > heap;
			for(int j=0; j<i; j++) {
				heap.push(side(p[j]));
				if(SZ(heap) >= k)
					heap.pop();
			}
			assert(SZ(heap) == k-1);
			while(!heap.empty()) {
				debug("%f ", heap.top());
				s += heap.top();
				heap.pop();
			}
			debug("|||%d %f\n", i, s);
			ans = max(ans, s);
		}
		printf("%.10f\n", ans);
	}
	return 0;
}
