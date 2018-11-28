#include <algorithm>
#include <bitset>
#include <cassert>
#include <deque>
#include <fstream>
#include <iostream>
#include <map>
#include <math.h>
#include <memory>
#include <queue>
#include <sstream>
#include <stdio.h>
#include <string>
#include <vector>

#define FOR(i, a, b) for (int i = (a); i < (b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define POW(n) ((n) * (n))
#define ALL(a) (a).begin(), (a).end()
#define dump(v) (cerr << #v << ": " << v << endl)
#define cerr                                                                   \
  if (true)                                                                    \
  cerr

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<string> vs;
typedef vector<long long> vll;
typedef pair<int,int> pii;

int T;
ll N,K;
// std::vector<pii> V;
vll R,H;

double PI = 3.141592653589793d;

// ll n = to_T<ll>("114514")
template <class T> T to_T(const string &s) {
	istringstream is(s);
	T res;
	is >> res;
	return res;
}
template <class T> string to_s(const T &a) {
	ostringstream os;
	os << a;
	return os.str();
}

double calc(double r,double h){
  // return POW((double)r) + 2.d*PI*r*h;
  return POW((double)r)*PI + 2*r*PI*h;
}

double rcalc(double r){
  return POW((double)r)*PI;
}

double hcalc(double r, double h){
  // cout << r << " " << h << " " << (calc(r,h) - rcalc(r)) << endl;
  return 2*r*PI*h;
}


double solve() {
  // sort(ALL(V));
  // reverse(ALL(V));

  double ans = 0;

  for(int i = 0;i<1 << N;++i){
    int c = 0;
    int maxr = 0;
    double sum = 0;

    REP(j,N){
      if( i & (1 << j)){
        c++;
        maxr = max(maxr,(int)R[j]);
        sum += hcalc(R[j],H[j]);
      }
    }

    if(c > K)continue;
    sum += rcalc((double)maxr);

    // cout << i << " " << c << " " << sum << endl;
    ans = max(ans,sum);
  }

  return ans;
}


int main() {
	ios::sync_with_stdio(false);
	cin >> T;

	REP(t, T){
    cin >> N >> K;
    // V.clear();
    R.clear();
    H.clear();
    R.resize(N);
    H.resize(N);
    REP(i,N){
      cin >> R[i] >> H[i];
      // cout << R[i]  << " "<< H[i] << endl;
      // int r,h;
      // cin >> r >> h;
      // V.push_back(pii(r,h));
    }
		double ans = solve();
		// cout << "Case #" << t + 1 << ": ";
    printf("Case #%d: %.9f\n",t+1,ans);
    // cout << endl;
	}

	return 0;
}
