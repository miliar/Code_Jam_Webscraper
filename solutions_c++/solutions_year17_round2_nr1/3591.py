#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <climits>
#include <complex>
#include <numeric>
using namespace std;

#define REP(i,n) for(int i=0; i<(int)(n); i++)
#define RREP(i,n) for(int i=(int)n-1; i>=0; i--)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define RFOR(i,c) for(__typeof((c).rbegin())i=(c).rbegin();i!=(c).rend();++i)
#define ALL(c) (c).begin(), (c).end()

typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<int, pair<int, int> > pipii;
typedef vector<int> vi;

const int INF = 1e9;
const int MOD = 1e9+7;
const long double EPS = 1e-7;

bool isAttack(long double d, long double s0, long double d1, long double s1) {
	//printf("d1 : %.12Lf", d1);
	long double dd = d1 * s0 / (s0 - s1);
	//cout << d << " " << s0 << " " << d1 << " " << s1 << endl;
	//printf("dd : %.12Lf\n", dd);
	if(dd > d + EPS) return false;
	if(dd < 0) return false;
	return true;
}

int main(void){
	int t; cin >> t;
	for(int tt = 1; tt <= t; tt++){
		int d, n;
		cin >> d >> n;
		vector<ll> ki(n), si(n);
		REP(i, n) cin >> ki[i] >> si[i];

		long double left = EPS, right = 1e15 + EPS;
		for(int i = 0; i <= 200; i++){
			long double mid = (left + right) / 2;
			int attack = 0;
			REP(i, n){
				if(isAttack(d, mid, ki[i], si[i])) attack = 1;
			}
			if(attack) right = mid;
			else left = mid;
		}

		cout << "Case #" << tt << ": ";
		printf("%.10Lf\n", left);
	}

	return 0;
}
