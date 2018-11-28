
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define INF 1000000000
#define F first
#define S second
#define forn(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,b) for(int i = 0; i < (b); i++)

#define PI 3.14159265358979323846264
using namespace std;


bool cmp(ii a, ii b){
	return a.F > b.F;
}
bool cmp2(ii a, ii b){
	return a.S*a.F > b.S*b.F;
}


int main(){
	int testc;
	scanf("%d", &testc);
	for(int tc = 1; tc <= testc; tc++){
		int n,k;
		ii p[1234];
		scanf("%d %d", &n, &k);
		rep(i,n) scanf("%lld %lld", &p[i].F, &p[i].S);
		double mx = -1;
		for(int i = 0; i <= n-k; i++){
			double area = 0;
			sort(p,p+n,cmp);
			ii x = p[i];
			area += 2*PI*x.F*x.S + PI*x.F*x.F;
			sort(p+i+1,p+n,cmp2);
			for(int j = 0; j < k-1; j++){
				area += 2*PI*p[j+i+1].F*p[j+i+1].S;
			}
			mx = max(mx,area);
		}
		printf("Case #%d: %0.12lf\n", tc, mx);
	}
	

	return 0;
}
