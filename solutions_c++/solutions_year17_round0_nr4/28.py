#line 1 "D.cpp"
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <cassert>
#include <cmath>
#include <cstring>
#include <functional>
#include <random>
using namespace std;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef long long ll;
#define REP(i,a,n) for (int i = (a); i < (n); i++)

template<class T> T& setmin(T &a, const T &b) {return a = min(a, b);}
template<class T> T& setmax(T &a, const T &b) {return a = max(a, b);}
template<class T> T MODD(const T &a, const T &b) {T r = a%b; if (r < 0) r += b; return r;}




///////////////////////////////// BEGIN util.h /////////////////////////////////


#line 1 "util.h"
template <class T, class U>
ostream& operator<<(ostream &o, const pair<T,U> &p) {
	return o << "(" << p.first << ", " << p.second << ")";
}

template <class T>
ostream& print_list(ostream &o, const T &v) {
	o << "[";
	bool first = true;
	for (const auto &t : v) {
		if (first)
			first = false;
		else
			o << ", ";
		o << t;
	}
	return o << "]";
}

template <class T>
ostream& print_map(ostream &o, const T &v) {
	o << "{";
	bool first = true;
	for (const auto &t : v) {
		if (first)
			first = false;
		else
			o << ", ";
		o << t.first << " => " << t.second;
	}
	return o << "}";
}

template <class T>
ostream& operator<<(ostream &o, const vector<T> &v) {
	return print_list(o, v);
}

template <class T>
ostream& operator<<(ostream &o, const set<T> &v) {
	return print_list(o, v);
}

template <class T,size_t N>
ostream& operator<<(ostream &o, const array<T,N> &v) {
	return print_list(o, v);
}

template <class T,class U>
ostream& operator<<(ostream &o, const map<T,U> &v) {
	return print_map(o, v);
}

template <class T, size_t N>
struct TuplePrintHelper {
	static ostream& print(ostream& o, const T &t) {
		TuplePrintHelper<T,N-1>::print(o, t);
		o << ", ";
		return o << get<N-1>(t);
	}
};

template <class T>
struct TuplePrintHelper<T,1> {
	static ostream& print(ostream& o, const T &t) {
		return o << get<0>(t);
	}
};

template <class T>
struct TuplePrintHelper<T,0> {
	static ostream& print(ostream& o, const T &) {
		return o;
	}
};

template <class... Args>
ostream& operator<<(ostream &o, const tuple<Args...> &t) {
	o << "(";
	TuplePrintHelper<tuple<Args...>, sizeof...(Args)>::print(o, t);
	return o << ")";
}


template <class T>
T fastpow(const T &a, ll n) {
	T r = 1, e = a;
	for (int i = 0; (1ll<<i) <= n; i++, e *= e) {
		if (n&(1ll<<i))
			r *= e;
	}
	return r;
}



///////////////////////////////// END util.h /////////////////////////////////


#line 30 "D.cpp"

int testcasenr;

struct bigraph {
	int N1, N2; // Number of nodes in $M_1$ and $M_2$
	vector<VI> ad1; // ad1[a]: Nodes in $M_2$ that are connected to $a\in M_1$
	vector<bool> bad1, bad2;
	VI ni1; // The node in $M_2$ that is matched to $a\in M_1$; -1 if unmatched
	VI ni2; // The node in $M_1$ that is matched to $a\in M_2$; -1 if unmatched
	vector<bool> vis;
	bigraph(int n1, int n2) {
		N1 = n1; N2 = n2;
		ad1.resize(n1);
		bad1.assign(n1,false);
		bad2.assign(n1,false);
	}
	bool visit(int i) {
		if (vis[i])
			return false;
		vis[i] = true;
		for (int k : ad1[i]) {
			if (k != ni1[i] && (ni2[k] == -1 || visit(ni2[k]))) {
				ni1[i] = k;
				ni2[k] = i;
				return true;
			}
		}
		return false;
	}
	// Returns the size of the maximum bipartite matching / minimum vertex cover
	int solve() {
		ni1.assign(N1, -1);
		ni2.assign(N2, -1);
		int numpairs = 0, pv;
		do {
			pv = numpairs;
			vis.assign(N1, false);
			REP(i,0,N1)
			if (ni1[i] == -1)
				numpairs += visit(i);
		} while(numpairs != pv);
		return numpairs;
	}
};

int N;

int index(int x, int y, int t, int d) {
	if (t == 0) {
		if (d == 0)
			return x;
		else
			return y;
	} else {
		if (d == 0)
			return x+y;
		else
			return x-y+N;
	}
}

char cmap[2][2] = {{'.','+'},{'x','o'}};

void docase() {
	int M;
	scanf("%d %d ", &N, &M);
	vector<bigraph> graphs(2, bigraph(5*N, 5*N));
	vector<vector<vector<bool> > > input(2, vector<vector<bool> >(N, vector<bool>(N, false)));
	vector<vector<vector<bool> > > output(2, vector<vector<bool> >(N, vector<bool>(N, false)));
	int res = 0;
	REP(m,0,M) {
		char c; int x, y;
		scanf("%c %d %d ", &c, &x, &y);
		x--; y--;
		if (c == 'x' || c == 'o') {
			input[0][x][y] = true;
			graphs[0].bad1[index(x,y,0,0)] = true;
			graphs[0].bad2[index(x,y,0,1)] = true;
			res++;
		}
		if (c == '+' || c == 'o') {
			input[1][x][y] = true;
			graphs[1].bad1[index(x,y,1,0)] = true;
			graphs[1].bad2[index(x,y,1,1)] = true;
			res++;
		}
	}
	REP(t,0,2) {
		REP(x,0,N) REP(y,0,N) {
			int a = index(x,y,t,0), b = index(x,y,t,1);
			if (!graphs[t].bad1[a] && !graphs[t].bad2[b])
				graphs[t].ad1[a].push_back(b);
		}
		int size = graphs[t].solve();
		res += size;
		REP(x,0,N) REP(y,0,N) {
			int a = index(x,y,t,0), b = index(x,y,t,1);
			output[t][x][y] = input[t][x][y] || graphs[t].ni1[a] == b;
		}
	}
	vector<pair<char,PII> > changes;
	REP(x,0,N) REP(y,0,N) {
		if (input[0][x][y] != output[0][x][y] || input[1][x][y] != output[1][x][y])
			changes.push_back(make_pair(cmap[output[0][x][y]][output[1][x][y]], PII(x,y)));
	}
	printf("%d %d\n", res, (int)changes.size());
	for (auto &f : changes)
		printf("%c %d %d\n", f.first, f.second.first+1, f.second.second+1);
}

int main() {
	int T;
	scanf("%d ", &T);
	for (testcasenr = 1; testcasenr <= T; testcasenr++) {
		fprintf(stderr, "Test %d/%d\n", testcasenr, T);
		printf("Case #%d: ", testcasenr);
		docase();
		fflush(stdout);
		fflush(stderr);
	}
	return 0;
}
