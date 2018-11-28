/*                                                            */
/*       Lukasz Marecik, lm277561@students.mimuw.edu.pl       */
/*                                                            */
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cmath>
#include <cassert>
#include <cstring>
#include <bitset>
#include <sstream>
#include <ext/numeric>
#include <unordered_set>
#include <unordered_map>
#include <gmpxx.h>				// -lgmpxx -lgmp
//#include <NTL/mat_lzz_p.h> 	// -lntl
using namespace std ;
using namespace __gnu_cxx ;
//using namespace NTL ;
typedef mpz_class BIGNUM ;
typedef long long LL ;
typedef pair<int,int> PII ;
typedef vector<int> VI ;
const int INF = 1e9+100 ;
const LL INFLL = (LL)INF*INF ;
#define REP(i,n) for(int i=0;i<(n);++i)
#define ALL(c) c.begin(),c.end()
#define FOREACH(i,c) for(auto i=(c).begin();i!=(c).end();++i)
#define CLEAR(t) memset(t,0,sizeof(t))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second

template<class T1,class T2> ostream& operator<<(ostream &s, const pair<T1,T2> &x) { return s << "(" << x.FI << "," << x.SE << ")" ;}
template<class T>           ostream& operator<<(ostream &s, const vector<T>   &t) { FOREACH(it, t) s << *it << " " ; return s ; }
template<class T>           ostream& operator<<(ostream &s, const set<T>      &t) { FOREACH(it, t) s << *it << " " ; return s ; }
template<class T1,class T2> ostream& operator<<(ostream &s, const map<T1, T2> &t) { FOREACH(it, t) s << *it << " " ; return s ; }

template<class T1, class T2> T1 conv(const T2 &x) {
	stringstream sss ; sss << x ; T1 y ; sss >> y ; return y ;
}

template<class T> void _debug(bool printName, const char* s, const T &x) { if(printName) cerr << s << "=" ; cerr << x << endl ; }
void _debug(bool, const char* s, const char*) {
	for(;*s;s++) if(*s!='"') { cerr << *s ; } cerr << endl ;
}
template<class T, class... R> void _debug(bool printName, const char* s, const T &x, R... y) {
	bool o=0, str=(*s=='"') ;
	for(; o || *s!=',' ; s++) if(*s=='"') o=!o ; else if(printName||str) cerr<<*s ;
	for(s++;*s && *s==' '; s++) ;
	if(!str) { if(printName) cerr << "=" ; cerr << x ; if(*s!='"' && printName) cerr << "," ; } cerr << " " ;
	_debug(printName, s, y...) ;
}

template<class T>             void _coord(const T &x)         { cerr << "[" << x << "]" ;             }
template<class T, class... R> void _coord(const T &x, R... y) { cerr << "[" << x << "]" ; _coord(y...) ; }

template<class T, class I>             void _val(T &t, const I &i)         { cerr << t[i] ; }
template<class T, class I, class... J> void _val(T &t, const I &i, J... j) { _val(t[i], j...) ; }

#ifndef LOCAL
	#define CERR(...)
	#define DEBUG(...)
	#define DARRAY(...)
#else
	#define CERR(...)     if(DFLAG) _debug(0, #__VA_ARGS__, __VA_ARGS__)
	#define DEBUG(...)    if(DFLAG) _debug(1, #__VA_ARGS__, __VA_ARGS__)	
	#define DARRAY(t,...) if(DFLAG) { cerr << #t ; _coord(__VA_ARGS__) ; cerr << " = " ; _val(t,__VA_ARGS__) ; cerr << endl ; }
#endif

////////////////////////////////////////////////////////////////////////////////
void __init() ;
void __main() ;

int main()
{
	ios_base::sync_with_stdio(0) ;
	cout.setf(ios::fixed) ; cout.precision(10) ;
	cerr.setf(ios::fixed) ; cerr.precision(10) ;
	__init() ;
	int C ;
	cin >> C ; cin.ignore() ;
	for(int tests=1 ; tests<=C ; tests++) {
//		cerr << "Case #" << tests << endl ;
		cout << "Case #" << tests << ": " ;
		__main() ;
	}
}
#define DFLAG 0
////////////////////////////////////////////////////////////////////////////////

void __init() {
	
}
////////////////////////////////////////////////////////////////////////////////

const int MAXN = 100 ;
char t[MAXN][MAXN] ;
int R, C ;
vector<PII> closures[MAXN][MAXN] ;

const int add_x[4] = {1,0,-1,0} ;
const int add_y[4] = {0,1,0,-1} ;

bool inRange(int x, int y) {
	return 0<=x && x<R && 0<=y && y<C ;
}

void move(int &x, int &y, int &dir) {
	x += add_x[dir] ;
	y += add_y[dir] ;
	char field = t[x][y] ;
	if(field=='\\') {
		int tmp[4] = {1,0,3,2} ;
		dir = tmp[dir] ;
	}
	if(field=='/') {
		int tmp[4] = {3,2,1,0} ;
		dir = tmp[dir] ;
	}
}

bool go(int x, int y, int dir, vector<PII> &s) {
//	DEBUG("go", x, y, dir) ;
	while(1) {
		move(x,y,dir) ;
//		DEBUG(x,y,dir) ;
		if(!inRange(x,y) || t[x][y]=='#')	// wylecielismy
			return true ; 
		if(t[x][y]=='-' || t[x][y]=='|')
			return false ;
		if(t[x][y]=='.')
			s.PB(MP(x,y)) ;
	}
}

//////////////////////////////////////////////
VI implies[2*MAXN*MAXN] ;		// wymuszenia
bool used[2*MAXN*MAXN], w[2*MAXN*MAXN] ;

VI post ;

// DFS na grafie odwróconym
void dfs_rev(int x) {
	used[x] = true ;
	FOREACH(q, implies[x^1])
		if(!used[*q^1]) dfs_rev(*q^1) ;
	post.PB(x) ;
}

void dfs_mark(int x) {
	used[x] = used[x^1] = w[x] = 1 ;
	FOREACH(q, implies[x])
		if(!used[*q]) dfs_mark(*q) ;
}

// ustawienie klauzuli (a or b)
void sat_or(int a, int b) {
	implies[a^1].PB(b) ;
	implies[b^1].PB(a) ;
}

// n - liczba zmiennych 0,..,n-1
// kazdej zmiennej i odpowiada literal 2*i oraz 2*i+1 (zaprzeczenie)
// w[2*i]   = true  <=> zmienna i ustawiona na 1
// w[2*i+1] = true  <=> zmienna i ustawiona na 0
bool sat2(int n) {
	CLEAR(used) ;
	CLEAR(w) ;
	post.clear() ;
	
	int i ;
	REP(i, 2*n)
		if(!used[i]) dfs_rev(i) ;
	reverse(ALL(post)) ;	// malejaca kolejnosc postorder w grafie transp.
	
	CLEAR(used) ;
	FOREACH(q, post)
		if(!used[*q]) dfs_mark(*q) ;
	
	REP(i, 2*n)
		FOREACH(q, implies[i])
			if(w[i] && !w[*q]) return 0 ;
	return 1 ;
}
////////////////////////////////

void __main() {
	DEBUG("") ;
	cin >> R >> C ;
	vector<PII> guns ;
	REP(i, R)
		REP(j, C) {
			closures[i][j].clear() ;		
			cin >> t[i][j] ;
			if(t[i][j]=='-' || t[i][j]=='|')
				guns.PB(MP(i,j)) ;
		}
	/*REP(i, R) {
		REP(j, C) {
			cout << t[i][j] ;
		}
		cout << endl ;
	}*/
	
	REP(k, 2*guns.size())
		implies[k].clear() ;
	
	REP(i, guns.size()) {
		vector<PII> s ;
		bool ok1 = go(guns[i].FI, guns[i].SE, 0, s) ;
		bool ok2 = go(guns[i].FI, guns[i].SE, 2, s) ;
		
		if(ok1 && ok2) {
//			DEBUG(guns[i], "|", s) ;
			FOREACH(it, s)
				closures[it->FI][it->SE].PB(MP(i,0)) ;
		}
		else
			sat_or(2*i+1, 2*i+1) ;
		
		s.clear() ;
		ok1 = go(guns[i].FI, guns[i].SE, 1, s) ;
		ok2 = go(guns[i].FI, guns[i].SE, 3, s) ;
		
		if(ok1 && ok2) {
//			DEBUG(guns[i], "-", s) ;
			FOREACH(it, s)
				closures[it->FI][it->SE].PB(MP(i,1)) ;
		}
		else
			sat_or(2*i, 2*i) ;
	}
	
	//DEBUG(guns.size()) ;
	//DEBUG(closures) ;
	
	REP(i, R)
		REP(j, C) {
			if(t[i][j]!='.') continue ;
			auto &tmp = closures[i][j] ;
			if(tmp.empty()) {
				cout << "IMPOSSIBLE" << endl ;
				return ;
			}
			auto a = tmp[0] ;
			auto b = tmp.back() ;
			DEBUG(a,b) ;
			sat_or(2*a.FI+a.SE, 2*b.FI+b.SE) ;
		}
	
	bool ok = sat2(guns.size()) ;
	if(!ok) {
		cout << "IMPOSSIBLE" << endl ;
		return ;
	}
	else {
		cout << "POSSIBLE" << endl ;
		REP(i, guns.size())
			t[guns[i].FI][guns[i].SE] = w[2*i] ? '|' : '-' ;
		REP(i, R) {
			REP(j, C)
				cout << t[i][j] ;
			cout << endl ;
		}
	}
}

