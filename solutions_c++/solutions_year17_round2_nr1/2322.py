
#include <stdio.h>
#include <algorithm>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define INF 1000000000
#define F first
#define S second
#define forn(i,a,b) for(int i = (a); i < (b); i++)
#define rep(i,b) for(int i = 0; i < (b); i++)

using namespace std;

int main(){
	int tcas;
	int d, n;
	scanf("%d", &tcas);
	for(int tc = 1; tc <= tcas; tc++){
		scanf("%d %d", &d, &n);
		double arrives = -1;
		rep(i,n){
			int k,s;
			scanf("%d %d", &k, &s);
			arrives = max(arrives, ((double)d-(double)k)/(double)s);
		}
		printf("Case #%d: %lf\n", tc, (double)d/(double)arrives);
	}

	return 0;
}
