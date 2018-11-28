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

		int n, c, m;
		ifs >> n >> c >> m;

		VVI a(n, VI(c));
		VI num(c), pos(n);
		int sm = 0, la = m;
		REP(i,m){
			int p, b;
			ifs >> p >> b;
			p--;
			b--;
			a[p][b]++;
			num[b]++;
			pos[p]++;
			sm = max(sm, num[b]);
		}

		sm--;
		while (la - sm > 1){
			int mi = (sm + la) / 2;
			int move = 0;
			bool possible = true;
			int yo = 0;
			REP(i,n){
				if (pos[i] <= mi){
					yo += mi - pos[i];
				}else{
					move += pos[i] - mi;
					yo -= pos[i] - mi;
					if (yo < 0) possible = false;
				}
			}
			if (possible) la = mi;
			else sm = mi;
		}

		int ans = la;
		int move = 0;
		int yo = 0;
		REP(i,n){
			if (pos[i] <= ans){
				yo += ans - pos[i];
			}else{
				move += pos[i] - ans;
				yo -= pos[i] - ans;
			}
		}

		cout << ans << " " << move << endl;
		fprintf(fp, "%d %d\n", ans, move);
	}

	return 0;
}