#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <cstring>
#include <string>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int i=0; i<n; ++i)
#define FOR(i,a,b) for(int i=a; i<=b; ++i)
#define FORR(i,a,b) for (int i=a; i>=b; --i)
#define ALL(c) (c).begin(), (c).end()

typedef long long ll;
typedef vector<int> VI;
typedef vector<ll> VL;
typedef vector<VI> VVI;
typedef pair<int,int> P;
typedef pair<ll,ll> PL;

int main(void) {
	ifstream ifs("input.txt");
	ofstream ofs("out.txt");
	FILE *fp;
	fp = fopen("out.txt","w");
	int num_of_cases;
	ifs >> num_of_cases;
	REP(cas,num_of_cases){
		fprintf(fp,"Case #%d: ",cas+1);
		printf("Case #%d: ",cas+1);

		ll n, k;
		ifs >> n >> k;
		ll ma = n, mi = 0, x = 1, y = 0;
		while (k > x + y){
			k -= x + y;
			ll ma2 = ma/2, mi2 = ma2-1, x2 = 0, y2;
			if (ma % 2 == 1){
				x2 = 2*x + y;
				y2 = y;
			}else{
				x2 = x;
				y2 = x + 2*y;
			}
			ma = ma2;
			mi = mi2;
			x = x2;
			y = y2;
		}

		ll p;
		if (k <= x) p = ma;
		else p = mi;
		ma = p/2, mi = p-1-ma;

		cout << ma << " " << mi << endl;
		fprintf(fp, "%lld %lld\n", ma, mi);
	}

	return 0;
}