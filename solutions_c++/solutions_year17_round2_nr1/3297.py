#include <cstdio>
#include <algorithm>
#include <cstring>
#include <map>
#include <vector>
#include <cmath>
#include <cstdlib>

using namespace std;

const int maxn = 1111;

double v[maxn];

int d, n;

int main(){
	int t;
	scanf("%d", &t);
	int caso = 1;
	while(t--){
		scanf("%d %d", &d, &n);
		int k, s;
		double ans = 0;
		for(int i = 0 ; i < n; i++){
			scanf("%d %d", &k, &s);
			v[i] = ((double) d - k)/(double) s;
			ans = max(v[i], ans);
		}

		printf("Case #%d: %.6lf\n", caso, ((double ) d)/ans );
		caso++;
	}
	
	return 0;
}