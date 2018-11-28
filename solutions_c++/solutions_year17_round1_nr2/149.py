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

bool check(int x, int y){
	return 10*x >= 9*y && 10*x <= 11*y;
}

int solve(int n, int p, VI r, VVI q){
	if (n == 1){
		int ans = 0;
		REP(j,p){
			int x = q[0][j]/r[0]*r[0];
			if (check(q[0][j], x) || check(q[0][j], x+r[0])) ans++;
		}
		return ans;
	}
	int ans = 0;
	VI s(n);
	FOR(a,1,1000000){
		bool make = true, no_more = false;
		while (make){
			make = true;
			REP(i,n){
				int x = r[i] * a;
				while (s[i] < p && 10*q[i][s[i]] < 9*x) s[i]++;
				if (s[i] == p) no_more = true, make = false;
				else if (10*q[i][s[i]] > 11*x) make = false;
			}
			if (make){
				ans++;
				REP(i,n) s[i]++;
			}
		}
		// cout << a << endl;
		// REP(i,n) cout << s[i] << " ";
		// cout << endl;
		if (no_more) break;
	}
	return ans;
}

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

		int n, p;
		ifs >> n >> p;
		VI r(n);
		REP(i,n) ifs >> r[i];
		VVI q(n,VI(p));
		REP(i,n) REP(j,p) ifs >> q[i][j];
		REP(i,n) sort(ALL(q[i]));

		int ans = solve(n, p, r, q);
		cout << ans << endl;
		fprintf(fp, "%d\n", ans);
	}

	return 0;
}