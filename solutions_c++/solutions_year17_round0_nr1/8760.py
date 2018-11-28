#include<bits/stdc++.h>
#define ALL(X)        X.begin(),X.end()
#define FOR(I,A,B)    for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)   for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)   for(int (I) = (A); (I) >= (B); (I)--)
#define CLEAR(X)      memset(X,0,sizeof(X))
#define SIZE(X)       int(X.size())
#define CONTAINS(A,X) (A.find(X) != A.end())
#define PB            push_back
#define MP            make_pair
#define X             first
#define Y             second
using namespace std;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U> &_p) { return os << "(" << _p.X << "," << _p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& _V) { bool f = true; os << "["; for(auto v: _V) { os << (f ? "" : ",") << v; f = false; } return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& _S) { bool f = true; os << "("; for(auto s: _S) { os << (f ? "" : ",") << s; f = false; } return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& _M) { return os << set<pair<T, U> >(ALL(_M)); }

template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
	  while(*sdbg!=',')cerr<<*sdbg++;cerr<<'='<<h<<','; _dbg(sdbg+1, a...);
}

#ifdef LOCAL
  #define DBG(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
  #define DBG(...) ;
  #define cerr if(0)cout
#endif

int T, k;
int cou; 
string S; 

void solve() 
{ 
	cin >> S >> k; 
	int res = 0; 
	FORD(i,SIZE(S)-1,k-1) 
	{ 
		if(S[i] == '-')
		{ 
			res++; 
			FORW(j,0,k) 
			{ 
				int pos = i-j; 
				if(S[pos] == '-') 
					S[pos] = '+'; 
				else 
					S[pos] = '-';
			} 
		} 
	} 
	cout << "Case #" << ++cou << ": "; 
	FORW(i,0,SIZE(S))
		if(S[i] == '-') 
		{ 
			puts("IMPOSSIBLE"); 
			return; 
		}
	cout << res << endl; 
} 

int main() 
{
	cin >> T; 
	while(T--) 
		solve(); 
} 
