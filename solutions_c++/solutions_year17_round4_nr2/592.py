#include <vector>
#include <iostream>
#include <math.h>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <map>

#define FOR(i, n) for(int i = 0; i < n; i++)
#define MP(a, b) make_pair(a, b)
#define INF 2000000000

using namespace std;

typedef long long LL;
typedef pair<int, int> PII;

int n, c, m;
int minprom;
int r[1001][1001];
int sum[1001];
int sbps[1001];

bool can(int nr) {
	//cout << "CAN " << nr << endl;
	minprom = 0;
	int left = 0;
	for (int pos = 1; pos <= n; pos++) {
		int posleft = nr;
		//cout << "DEBUG " << posleft << ' ' << sbps[pos] << endl;
		if (sbps[pos] <= posleft) {
			posleft -= sbps[pos];
		} else {
			FOR(i, n) {
				if (r[pos][i] <= posleft) {
					posleft -= r[pos][i];
				} else {
					// promote
					//cout << "prom r[pos][i] " << r[pos][i] << endl;
					//r[pos][i] -= posleft;
					if (r[pos][i] - posleft > left) {
						return false;
					}
					//cout << "PROM " << r[pos][i] << endl;
					minprom += (r[pos][i] - posleft);
					left -= (r[pos][i] - posleft);
					posleft = 0;
				}
			}
		}
		//cout << "PL " << posleft << endl;
		left += posleft;
	}
	return true;
}

void solve(int casenum) {
  cout << "Case #" << casenum << ": ";
  cin >> n >> c >> m;
  memset(r, 0, sizeof(r));
  memset(sum, 0, sizeof(sum));
  memset(sbps, 0, sizeof(sbps));
  FOR(i, m) {
  	int bi, pi;
  	cin >> pi >> bi;
  	sbps[pi]++;
  	sum[bi - 1]++;
  	r[pi][bi - 1]++;
  }

  int mx = 0, mmx = 0;
  FOR(i, n) {
  	mx = max(mx, sum[i]);
  	mmx += sum[i];
  }

  int ll = mx;
  int rr = mmx;
  //cout << "BOUNDS " << ll << ' ' << rr << endl;
  while (rr - ll > 1) {
  	int mid = (ll + rr) / 2;
  	if (can(mid)) {
  		rr = mid;
  	} else {
  		ll = mid;
  	}
  }

  if (can(ll)) {
  	cout << ll << ' ' << minprom << endl;
  } else {
  	can(rr);
  	cout << rr << ' ' << minprom << endl;
  }
}

int main() {
  ios_base::sync_with_stdio(0);
  int t;
  cin >> t;
  FOR(tt,t) {
    solve(tt+1);
  }
  return 0;
}


