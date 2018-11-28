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
#include <vector>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
#define sz(X) ((int)(X).size())
#define foreach(i,c) for(__typeof((c).begin()) i=((c).begin());i!=(c).end();++i)
#define EXISTS(x, s) ( (s).find((x)) != (s).end() ) 
template<class T> vector<T> tokenize_to(const string &str) { vector<T> r; T x; istringstream is(str); while (is >> x) r.push_back(x); return r; }
template<typename T> string v_2_s(vector<T> &a) { stringstream sb; __typeof(a.begin()) i = a.begin(); if (i!=a.end()) { sb << *i; ++i; } for (; i!=a.end();++i) { sb << " " << *i; } return sb.str(); }

struct pos{
	uint64 i, mini, maxi;
	pos(uint64 _i, uint64 _mini, uint64 _maxi) : i(_i), mini(_mini), maxi(_maxi) {}
	const bool operator<(const pos& other) const {
		if (mini != other.mini)
			return mini < other.mini;
		if (maxi != other.maxi)
			return maxi < other.maxi;
		return i > other.i;
	}
};

// pos solve_bruteforce(int N, int K) {
	// vector<int> S(N + 2, 0);
	// S[0] = S[N + 1] = 1;
	
	// pos next(-1, -1, -1);
	// cerr << "N: " << N << endl;
	// for (int i = 0; i < K; ++i) {
		// next = pos(N + 1, -1, -1);		
		// int L, R;
		// for (int j = 1; j <= N; ++j) {
			// if (S[j] == 1)
				// continue;
			// L = R = j;
			// for (;S[L] == 0; L--);
			// for (;S[R] == 0; R++);
			// pos x(j, min(j - L - 1, R - j - 1), max(j - L - 1, R - j - 1));
			// if (next < x)
				// next = x;
		// }
		// cerr << next.i << endl;
		// S[next.i] = 1;
	// }
	// cerr << "---" << endl;
	// cerr << v_2_s(S) << endl;
	// return next;
// }


// pos solve_smarter(uint64 N, int K) {
	// std::priority_queue<uint64> Q;
	// Q.push(N);
	// uint64 X;
	// cerr << endl;
	// for (int i = 0; i < K; ++i) {
		// X = Q.top();
		// Q.pop();
		// cerr << X << endl;
		// uint64 L = X / 2 - ((X + 1) % 2);
		// uint64 R = X / 2;
		// if (i == K - 1)
			// return pos(-1, L, R);		
		// Q.push(L);
		// Q.push(R);
	// }
	// return pos(-1, -1, -1);	
// }

pos solve_supersmart(uint64 N, uint64 K) {
	uint64 count = 0;
	uint64 div = 1;
	while (count + div < K) {
		count += div;
		div *= 2;
	}
	uint64 X = (N - count) / div;
	uint64 R = (N - count) % div;
	if (K - count <= R) 
		X++;
	return pos(-1, X / 2 - ((X + 1) % 2), X / 2);
}

void solve() {
	uint64 N, K;
	cin >> N >> K;
	// auto ret = solve_bruteforce(N, K);
	// auto ret = solve_smarter(N, K);
	auto ret = solve_supersmart(N, K);
	// if (ret.maxi != ret2.maxi || ret.mini != ret2.mini)
		// cerr << "WTF: " << ret.mini << " " << ret.maxi << " vs " << ret2.mini << " " << ret2.maxi << endl;
		
	cout << ret.maxi << " " << ret.mini << '\n';
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
