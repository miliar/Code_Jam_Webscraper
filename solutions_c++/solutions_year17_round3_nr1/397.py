/*
ID: ahri1
PROG: A
LANG: C++
*/

#define _USE_MATH_DEFINES

#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <queue>
#include <vector>
#include <cmath>
#include <iomanip>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define sz(X) ((int)(X).size())
#define foreach(i,c) for(__typeof((c).begin()) i=((c).begin());i!=(c).end();++i)
#define EXISTS(x, s) ( (s).find((x)) != (s).end() ) 
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
template<typename T> string v_2_s(vector<T> &a) { stringstream sb; __typeof(a.begin()) i = a.begin(); if (i!=a.end()) { sb << *i; ++i; } for (; i!=a.end();++i) { sb << " " << *i; } return sb.str(); }

struct pancake {
	int64 R, H;
	int64 side;
	int64 top;
	pancake(int64 r, int64 h) : R(r), H(h) {
		side = r * 2 * h;
		top = r * r;
	}
	bool operator<(const pancake& other) const {
		if (R != other.R) return R < other.R;
		return H < other.H;
	}	
};

bool by_side(const pancake& a, const pancake& b) {
	if (a.side != b.side) return a.side > b.side;
	return a < b;
}

template<typename T, typename U> inline void relaxmax(T &res, const U &x) {
  if (x > res) {
    res = x;
  }
}
	
void solve() {
	int N, K;
	cin >> N >> K;
	vector<pancake> P;
	int64 R, H;
	for(int i = 0; i < N; ++i){
		cin >> R >> H;
		P.emplace_back(R, H);
	}
	sort(P.begin(), P.end());
	int64 ret = 0;
	
	// cerr << endl;
	for(int i = K - 1; i < N; ++i) {
		// cerr << i << endl;
		int64 temp = P[i].top + P[i].side;
		if (i > 1)
			sort(P.begin(), P.begin() + i, by_side);
		for(int j = 0; j < K - 1; ++j){
			temp += P[j].side;
		}
		relaxmax(ret, temp);
	}
	cout.precision(9);
	cout << std::fixed << ret * M_PI << endl;
	
}

int main() {

  cin.sync_with_stdio(0);
  int T;
  cin >> T;
  for (int i=0;i<T;i++) {
    cout << "Case #" << i+1 << ": ";
    solve();
  }
  
  return 0;
}
