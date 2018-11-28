#include <bits/stdc++.h>
#define LL long long
#define FOR(i,c) for(__typeof(c.begin()) i = c.begin(); i != c.end(); i++)
#define F first
#define S second
using namespace std;

const LL mod = 1e9 + 7;

template<typename T> T gcd(T a, T b) { return b == 0?a: gcd(b, a % b); }
template<typename T> T LCM(T a, T b) { return a*(b/gcd(a, b)); }
template<typename T> T expo(T base, T e, T mod) { T res = 1;
  while(e > 0) { if(e&1) res = res * base % mod; base = base * base % mod; e >>= 1; }
  return res;
}
template<typename T, typename S> T expo(T b, S e){if(e <= 1)return e == 0?1: b;\
	return (e&1) == 0?expo((b*b), e>>1): (b*expo((b*b), e>>1));}
template<typename T, typename S> T modinv(T a, S mod) { return expo(a, mod-2, mod); }
template<class T, class S> std::ostream& operator<<(std::ostream &os, const std::pair<T, S> &t) {
	os<<"("<<t.first<<", "<<t.second<<")";
	return os;
}
template<class T> std::ostream& operator<<(std::ostream &os, const std::vector<T> &t) {
	os<<"["; FOR(it,t) { if(it != t.begin()) os<<", "; os<<*it; } os<<"]";
	return os;
}

const int MAXN = 53;
const double EPS = 1e-9;
double P[MAXN];
LL pp[MAXN];
int n, k;

struct dsu {
  vector<int> Rank, P;
	vector<double> vals;
  int V;
  dsu(int v = 0) : V(v) {
    Rank = vector<int>(v + 1, 0);
		vals = vector<double>(v + 1, 0);
    P = vector<int>(v + 1, 0);
    for(int i = 0; i < P.size(); i++) {
      P[i] = i, Rank[i] = 1;
			vals[i] = ::P[i];
    }
  }
  int find_root(int x) { return x == P[x] ? x : P[x] = find_root(P[x]); }
  void merge(int x, int y) {
    int xr = find_root(P[x]), yr = find_root(P[y]);
    if(xr == yr) {
			assert(false);
		}
    if(vals[xr] < vals[yr]) swap(xr, yr), swap(x, y);
    Rank[xr] += Rank[yr];
    P[yr] = xr;
  }
};

int main() {
  ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int tc = 1; tc <= t; tc++) {
		double U;
		cin >> n >> k;
		cin >> U;
		for(int i = 1; i <= n; i++) {
			cin >> P[i];
		}
		dsu tester(n);
		for(int i = 1; i <= n; i++) {
			for(int j = i; j <= n; j++) {
				if(fabs(P[i] - P[j]) < EPS && tester.find_root(i) != tester.find_root(j)) {
					tester.merge(i, j);
				}
			}
		}
		while(U > EPS) {
			int cnt = 0;
			vector<pair<double, int> > arr;
			for(int i = 1; i <= n; i++) {
				if(tester.find_root(i) == i) {
					arr.push_back({tester.vals[i], i});
				}
			}
			if(arr.size() == 1) {
				int idx = arr[0].S;
				tester.vals[idx] += U/(double)n;
				break;
			}
			sort(arr.begin(), arr.end());
			double minim = arr[0].F, s_minim = arr[1].F;
			if((s_minim - minim) * tester.Rank[arr[0].S] > U) {
				int idx = arr[0].S;
				tester.vals[idx] += U/(double)tester.Rank[idx];
				break;
			}
			U -= tester.Rank[arr[0].S] * (s_minim - minim);
			tester.merge(arr[0].S, arr[1].S);
		}
		double res = 1.0l;
		for(int i = 1; i <= n; i++) {
			if(tester.find_root(i) == i) {
				res *= expo(tester.vals[i], tester.Rank[i]);
			}
		}
		cout << fixed << setprecision(10) << "Case #" << tc << ": " << res << '\n';
	}
  return 0;
}
