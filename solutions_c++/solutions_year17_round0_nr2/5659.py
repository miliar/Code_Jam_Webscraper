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

struct Solver {
	bool isGood(string& s, int low, int high) {
		for (int i = low; i + 1 <= high; ++i) {
			if (s[i] > s[i + 1]) {
				return false;
			}
		}
		
		return true;
	}
	
	long long toLongLong(string& s, int low, int high) {
		long long x = 0;
		for (int i = low; i <= high; ++i) {
			x = (x * 10LL) + (s[i] - '0');
		}
		return x;
	}
	
	long long solve(string& s) {
		if (isGood(s, 0, size(s) - 1)) {
			return toLongLong(s, 0, size(s) - 1);
		}
		
		for (int i = size(s) - 1; i >= 0; --i) {
			string p = s;
			if (p[i] != '0') {
				p[i] = p[i] - 1;
				for (int j = i + 1; j < size(s); ++j) {
					p[j] = '9';
				}
				
				if (isGood(p, 0, size(p) - 1)) {
					return toLongLong(p, 0, size(p) - 1);
				}
			}
		}
		
		return -1;
	}
};

int main()
{
	int nTest = readInt();
	Solver solver;
	for (int test = 1; test <= nTest; ++test) {
		string s = readString();
		long long x = solver.solve(s);
		cout << "Case #" << test << ": " << x << endl;
	}
	return 0;
}

// Powered by PhoenixAI