/*
ID: ahri1
PROG: A
LANG: C++
*/
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
#include <iomanip>
#include <vector>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define sz(X) ((int)(X).size())
#define foreach(i,c) for(__typeof((c).begin()) i=((c).begin());i!=(c).end();++i)
#define EXISTS(x, s) ( (s).find((x)) != (s).end() ) 
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
template<typename T> string v_2_s(vector<T> &a) { stringstream sb; __typeof(a.begin()) i = a.begin(); if (i!=a.end()) { sb << *i; ++i; } for (; i!=a.end();++i) { sb << " " << *i; } return sb.str(); }

struct horse {
	int K, S;
	const bool operator<(const horse& o) const {
		return K == o.K ? S > o.S : K > o.K;
	}
};

template<typename T, typename U> inline void relaxmax(T &res, const U &x) {
  if (x > res) {
    res = x;
  }
}

void solve() {
	int D, N;
	cin >> D >> N;
	vector<horse> H(N);
	for(int i = 0; i < N; ++i) {
		cin >> H[i].K >> H[i].S;
	}
	sort(H.begin(), H.end());
	
	double T = 0;
	
	for(int i = 0; i < N; ++i){
		relaxmax(T, (D - H[i].K) / (double)H[i].S);
	}
	
	cout << std::setprecision(7) << std::fixed << D / T << '\n';
	
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
