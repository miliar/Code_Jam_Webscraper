#include "stdafx.h"
#include <math.h> 
#include <iostream>
#include <fstream>
#include <sstream> 
#include <set> 
#include <map> 
#include <vector> 
#include <list> 
#include <string>
#include <algorithm>
#include <cassert>
#include <bitset>
#include <experimental/filesystem>
namespace fs = std::experimental::filesystem;
using namespace std;

//BEG parts From mkal13n
typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int uint;
typedef unsigned char uchar;
typedef double ld;
typedef pair<int, int> pii;
typedef pair<short, short> pss;
typedef pair<LL, LL> pll;
typedef pair<ULL, ULL> puu;
typedef pair<ld, ld> pdd;
template<class T> inline T sqr(T x) { return x * x; }
template<class T> inline string tostr(const T & x) { stringstream ss; ss << x; return ss.str(); }
inline LL parse(const string & s) { stringstream ss(s); LL x; ss >> x; return x; }

#define mp make_pair
#define MT make_tuple
#define pb push_back
#define sz(x) ((int)(x).size())
#define all(x) (x).begin(), (x).end()
#define clr(ar,val) memset(ar, val, sizeof(ar))
#define istr stringstream
#define forn(i,n) for(int i=0;i<(n);++i)
#define forv(i,v) forn(i,sz(v))
#define X first
#define Y second
const ld EPS = 1e-12;
const int INF = 1000 * 1000 * 1000;
const LL LINF = INF * 1ll * INF;
const ld DINF = 1e200;
const ld PI = 3.1415926535897932384626433832795l;
template<class T> ostream& operator<<(ostream &s, const vector<T> &v);
template<class A, class B> ostream& operator<<(ostream &s, const pair<A, B> &p);
template<class K, class V> ostream& operator<<(ostream &s, const map<K, V> &m);
template<class T, size_t N> ostream& operator<<(ostream &s, const array<T, N> &a);
template<class T> ostream& operator<<(ostream &s, const vector<T> &v) { s << '[';forv(i, v) { if (i)s << ',';s << v[i]; }s << ']';return s; }
template<class A, class B> ostream& operator<<(ostream &s, const pair<A, B> &p) { s << "(" << p.X << "," << p.Y << ")";return s; }
template<class K, class V> ostream& operator<<(ostream &s, const map<K, V> &m) { s << "{";bool f = false;for (const auto &it : m) { if (f)s << ",";f = true;s << it.X << ": " << it.Y; }s << "}";return s; }
template<class T> ostream& operator<<(ostream &s, const set<T> &m) { s << "{";bool f = false;for (const auto &it : m) { if (f)s << ",";f = true;s << it; }s << "}";return s; }
template<class T> ostream& operator<<(ostream &s, const multiset<T> &m) { s << "{";bool f = false;for (const auto &it : m) { if (f)s << ",";f = true;s << it; }s << "}";return s; }
template<class T, size_t N> ostream& operator<<(ostream &s, const array<T, N> &a) { s << '[';forv(i, a) { if (i)s << ',';s << a[i]; }s << ']';return s; }
template<size_t n, class... T> struct put1 { static ostream& put(ostream &s, const tuple<T...> &t) { s << get<sizeof...(T)-n>(t);if (n>1)s << ',';return put1<n - 1, T...>::put(s, t); } };
template<class... T> struct put1<0, T...> { static ostream& put(ostream &s, const tuple<T...> &t) { return s; } };
template<class... T> ostream& operator<<(ostream &s, const tuple<T...> &t) { s << "(";put1<sizeof...(T), T...>::put(s, t);s << ")";return s; }
ostream& put2(ostream &s, const tuple<> &t) { return s; }
template<class U> ostream& put2(ostream &s, const tuple<U> &t) { return s << get<0>(t); }
template<class U, class V, class... T> ostream& put2(ostream &s, const tuple<U, V, T...> &t) { return s << t; }
#ifdef DEB
#define dbg(...) do { cerr << #__VA_ARGS__ << " = "; put2(cerr, make_tuple(__VA_ARGS__)); cerr << endl; }while(false)
#else
#define dbg(...) do{}while(false)
#endif
//END
#define forb(i,n) for(int i=(n);i>=1;--i)
#define fornx(i,x,n) for(int i=(x);i<(n);++i)
#define forbx(i,n,b) for(int i=(n);i>=(x);--i)
#define fora(i, a) for (auto& i: a)
using pSS = pair<string, string>;

const string prob = "A";
const string infilesCheck[] = { prob + "-large",
prob + "-large-practice",
prob + "-small-attempt9",
prob + "-small-attempt8",
prob + "-small-attempt7",
prob + "-small-attempt6",
prob + "-small-attempt5",
prob + "-small-attempt4",
prob + "-small-attempt3",
prob + "-small-attempt2",
prob + "-small-attempt1",
prob + "-small-attempt0",
prob + "-small-practice",
"testmy",
"test" };
string insuff = ".in";
string outsuff = ".out";
string logsuff = ".log";

int T, N, S;
int A, B;

void
PrintResult(int i, const vector<string>& res)
{
	cout << "Case #" << i << ":" << endl;
	fora(i, res) cout << i << endl;
}

void
Solve(vector<string>& s)
{
	//fill empty rows
	string lr;
	forn(i, A) {
		auto& r = s[i];
		forn(j, B) {
			if (r[j] != '?') {
				lr = r;
				goto start;
			}
		}
	}
	start:
	forn(i, A) {
		auto& r = s[i];
		int lq = 0;
		char lc = '?';
		forn(j, B) {
			char c = r[j];
			if (c != '?') {
				if (j == 0) {
					while (r[j + 1] == '?') {
						++j;
						r[j] = c;
					}
				}
				else {
					fornx(k, lq, j) {
						r[k] = c;
					}
				}
				lq = j + 1;
				lc = c;
			}
		}
		if (!lq) {
			r = lr;
			--i;
		}
		else {
			fornx(k, lq, B) {
				r[k] = lc;
			}
			lr = r;
		}
	}
}

int
main()
{
	string f = "def";
	for (auto& file : infilesCheck) {
		if (fs::exists(file + insuff)) {
			f = file;
			break;
		}
	}
	ifstream in(f + insuff);
	cin.rdbuf(in.rdbuf());

	ofstream out(f + outsuff);
	cout.rdbuf(out.rdbuf());

	ofstream err(f + logsuff);
	cerr.rdbuf(err.rdbuf());

	cin >> T;

	fornx(i, 1, T + 1) {
		vector<string> s;
		cin >> A >> B;
		forn(j, A) {
			string r;
			cin >> r;
			s.emplace_back(r);
		}
		Solve(s);
		PrintResult(i, s);
	}

	return 0;
}
