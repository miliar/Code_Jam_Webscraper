#include <iostream>
#include <iosfwd>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <cassert>
#include <cctype>
#include <climits>
#include <vector>
#include <bitset>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <deque>
#include <string>
#include <list>
#include <iterator>
#include <sstream>
#include <complex>
#include <fstream>
#include <functional>
#include <numeric>
#include <utility>
#include <algorithm>

using namespace std;

// MACROS_BEGIN
#define CLEAR() cerr << endl;
#define LET(x, a) __typeof(a) x = a
#define FOREACH(it, v) for (LET(it, (v).begin()); it != (v).end(); ++it)
#define REPEAT(i, n) for (int i = 0; i < (n); ++i)
// MACROS_END

// GENERIC_UTILITIES_BEGIN
template <class T> inline int size(const T& c) {return (int) c.size();}
inline long long two(int x) {return (1LL << (x));}
vector<string> split(string s, string delim) {
	s += delim[0];
	string tmp;
	vector<string> result;
	for (int i = 0; i < size(s); ++i) {
		if (delim.find(s[i]) == string::npos) { tmp.push_back(s[i]);}
		else {if (tmp != "") result.push_back(tmp); tmp.clear();}
	}
	return result;
}
template <class A, class B>
void setMin(A& a, const B& b) {
	a = min(a, b);
}
template <class A, class B>
void setMax(A& a, const B& b) {
	a = max(a, b);
}
// GENERIC_UTILITIES_END

// FAST_IO_BEGIN
// FAST_IO_END

// STANDARD_IO_BEGIN
#ifndef USING_FAST_IO
int readInt() {int N = -1; scanf("%d", &N); return N;}
double readDouble() {double D; scanf("%lf", &D); return D;}
string readString() {char buffer[1 << 20]; scanf("%s", buffer); return buffer;}
#endif // NOT DEFINED USING_FAST_IO
// STANDARD_IO_END


// OUTPUT_UTILITIES_BEGIN
template <class A, class B> ostream& operator << (ostream& o, const pair<A, B>& p);
template <class T> ostream& operator << (ostream& o, const vector<T>& v);
template <class A, class B> ostream& operator << (ostream& o, const map<A, B>& m);
template <class T> ostream& operator << (ostream& o, const set<T>& s);
template <class T> ostream& operator << (ostream& o, const queue<T>& q);
template <class T> ostream& operator << (ostream& o, const stack<T>& s);

template <class A, class B> ostream& operator << (ostream& o, const pair<A, B>& p) {
	o << "(" << p.first << "," << p.second << ")";
	return o;
}
template <class T> ostream& operator << (ostream& o, const vector<T>& v) {
	o << "{";
	bool first = true;
	FOREACH(it, v) {
		if (!first) o << ","; first = false; o << *it;
	}
	return o << "}";
}
template <class A, class B> ostream& operator << (ostream& o, const map<A, B>& m) {
	o << "{";
	bool first = true;
	FOREACH(it, m) {
		if (!first) o << ","; first = false; o << *it;
	}
	return o << "}";
}
template <class T> ostream& operator << (ostream& o, const set<T>& s) {
	o << "{";
	bool first = true;
	FOREACH(it, s) {
		if (!first) o << ","; first = false; o << *it;
	}
	return o << "}";
}
template <class T> ostream& operator << (ostream& o, const queue<T>& q) {
	o << "{";
	bool first = true;
	queue<T> p = q;
	while (!p.empty()) {
		if (!first) o << ","; first = false; o << p.front(); p.pop();
	}
	return o << "}";
}
template <class T> ostream& operator << (ostream& o, const stack<T>& s) {
	o << "{";
	bool first = true;
	stack<T> r = s;
	while (!r.empty()) {
		if (!first) o << ","; first = false; o << r.top(); r.pop();
	}
	return o << "}";
}
// OUTPUT_UTILITIES_END

// DEBUGGING_UTILITIES_BEGIN
#define PHOENIX_DEBUG

#ifdef PHOENIX_DEBUG
#define BUG(...) __f(__LINE__, #__VA_ARGS__, __VA_ARGS__)
template<typename Arg>
void __print(int line, const string& name, Arg&& arg) {
	cerr << line << ": " << name << " = " << arg << std::endl;
}
template<typename Arg>
void __g(int line, vector<string>& names, int idx, Arg&& arg) {
  __print(line, names[idx], arg);
}
template<typename Arg, typename... Args>
void __g(int line, vector<string>& names, int idx, Arg&& arg, Args&&... args) {
	__g(line, names, idx, arg);
	__g(line, names, idx + 1, args...);
}
template <typename Arg>
void __f(int line, const string& name, Arg&& arg) {
	__print(line, name, arg);
	CLEAR();
}
template <typename Arg, typename... Args>
void __f(int line, const string& _names, Arg&& arg, Args&&... args) {
	vector<string> names = split(_names, ", ");
	__g(line, names, 0, arg, args...);
	CLEAR();
}
#else
#define BUG(...)
#endif
// DEBUGGING_UTILITIES_END

const double epsilon = 1e-8;
const int infinite  = 1000000000;
const long long infiniteLL = 1000000000000000000LL;
const long long modulo = 1000000007;

vector<bool> seen;
vector<double> memo;

double calculate(int idx, int last, vector<int>& E, vector<int>& S,
					vector<vector <int> >& D) {
	if (idx == last) {
		return 0;
	} else if (seen[idx]) {
		return memo[idx];
	} else {
		seen[idx] = true;
		memo[idx] = infinite + 1;
		memo[idx] *= 10000;
		//memo[idx] ;
		double dist = 0;
		
		for (int i = idx + 1; i <= last; ++i) {
			dist += D[i - 1][i];
			
			if (E[idx] >= dist) {
				memo[idx] = min(memo[idx], (dist / S[idx]) + calculate(i, last, E, S, D));
			}
		}
		
		return memo[idx];
	}
}

int main()
{
	int nTest = readInt();
	for (int test = 1; test <= nTest; ++test) {
		seen.clear();
		memo.clear();
		int N = readInt(), Q = readInt();
		seen.resize(N, false);
		memo.resize(N, 0);
		vector<int> E, S;
		for (int i = 0; i < N; ++i) {
			E.push_back(readInt());
			S.push_back(readInt());
		}
		
		vector< vector<int> > D(N + 1, vector<int> (N + 1, 0));
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < N; ++j) {
				D[i][j] = readInt();
			}
		}
		int u = readInt() - 1, v = readInt() - 1;
		
		double result = calculate(0, N - 1, E, S, D);
		cout << std::setprecision(6) << std::fixed;
		cout << "Case #" << test << ": " << result << endl;
	}
	return 0;
}

// Powered by PhoenixAI