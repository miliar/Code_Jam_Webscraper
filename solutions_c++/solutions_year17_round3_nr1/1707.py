#include <cstdio>
#include <cstring>
#include <cmath>
#include <limits>
#include <cassert>

#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <algorithm>
#include <iomanip> 
using namespace std;

#define dout(x) cerr << #x << " = " << x << endl;
template<typename T>
ostream& operator<< (ostream& out, const vector<T>& v) {
	out << "[";
	for (auto vi : v)
		out << vi << ", ";
	out << "]";
	return out;
}

#define ALL(x) (x).begin(), (x).end()
#define FOR(i, n) for(int i=0;i<(n);++i)
#define pb push_back
#define fr first
#define sc second
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector <int> vi;
int DX[] = {  0, +1,  0, -1,  0};
int DY[] = {  +1, 0, -1,  0,  0};

int ri() {
	int temp;
	scanf("%d", &temp);
	return temp;
}



void solve(int t) {
	vector <pii> v;
	int n = ri(),k = ri();
	FOR(i,n) {
		int r = ri();
		int h = ri();
		v.pb(pii(r,h));
	}
	sort(ALL(v));

	double max_answer = 0;
	for (int i = k-1; i < n; i++) {
		double answer = (double)v[i].fr*v[i].fr*M_PI;
		answer += 2.0 * M_PI * v[i].fr * v[i].sc;
		vector<double> h;
		for (int j = 0; j < i; j++) {
			h.pb( 2.0 * M_PI * v[j].fr * v[j].sc );
		}
		sort(ALL(h));
		reverse(ALL(h));
		for (int j = 0; j < k-1; j++) {
			answer += h[j];
		}
		max_answer = max(max_answer, answer);
	}

	cout << setprecision(10) << fixed;
	cout << "Case #" << t << ": " << max_answer << "\n";
}

void readData() {
	int nt = ri();
	FOR(t,nt) {
		solve(t+1);
	}
}

int main() {
#ifdef LOCAL_TEST
	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	readData();
	//solve();
	return 0;
}
