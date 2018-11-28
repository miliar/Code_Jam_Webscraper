#include<bits/stdc++.h> 
#define ALL(X) X.begin(),X.end()
#define FOR(I,A,B) for(int (I) = (A); (I) <= (B); ++(I))
#define FORW(I,A,B) for(int (I) = (A); (I) < (B); ++(I)) 
#define FORD(I,A,B) for(int (I) = (A); (I) >= (B); --(I))
#define CLEAR(X) memset(X,o,sizeof(X))
#define SIZE(X) int(X.size())
#define PB push_back 
#define MP make_pair
#define X first 
#define Y second 
using namespace std;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U> &_p) { return os << "(" << _p.X << "," << _p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& _V) { bool f = true; os << "["; for(auto v: _V) { os << (f ? "" : ",") << v; f = false; } return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& _S) { bool f = true; os << "("; for(auto s: _S) { os << (f ? "" : ",") << s; f = false; } return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& _M) { return os << set<pair<T, U>>(ALL(_M)); }

template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
	  while(*sdbg!=',')cerr<<*sdbg++;
	    cerr<<'='<<h<<", "; _dbg(sdbg+1, a...);
}

#ifdef LOCAL
  #define DBG(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
  #define DBG(...) ;
  #define cerr if(0)cout
#endif

typedef pair<int, int> PII; 

int T, n, k, cou; 
bool t[1005]; 
PII w[1005]; 

int policz() 
{ 
	FOR(i,1,n) 
	{ 
		w[i].X = 1e9; w[i].Y = 1e9; 
	} 
	FOR(i,1,n) 
	{ 
		if(t[i]) continue; 
		FOR(j,0,i-1) 
		{ 
			if(t[j]) 
			{ 
				int dist = i-j; 
				dist--; 
				w[i].X=min(w[i].X,dist);
			} 
		} 
		FOR(j,i+1,n+1) 
		{ 
			if(t[j]) 
			{ 
				int dist = j-i; 
				dist--; ; 
				w[i].Y=min(w[i].Y,dist); 
			} 
		} 
	}
	int res = 0; PII cur(0,0); 
	FOR(i,1,n) 
	{ 
		if(t[i]) continue; 
		if(min(cur.X,cur.Y) < min(w[i].X,w[i].Y))
		{ 
			cur = w[i]; 
			res = i; 
		} 
		else if(min(cur.X,cur.Y) == min(w[i].X,w[i].Y ))
		{ 
			if(max(cur.X,cur.Y) < max(w[i].X,w[i].Y))
			{ 
				cur = w[i]; 
				res = i; 
			} 
		} 
	}
	FOR(i,1,n) 
	{ 
		w[i].X = 1e9; w[i].Y = 1e9;  
	} 
	return res; 
}

void solve() 
{ 
	scanf("%d%d",&n,&k);
	FOR(i,0,n+1) t[i] = false; 
	t[0] = true; t[n+1] = true; 
	FOR(i,1,k-1) 
	{ 
		int pos = policz();
		t[pos] = true; 
	} 
	PII result(0,0);
	FOR(i,1,n) 
	{ 
		if(t[i]) continue; 
		FOR(j,0,i-1) 
		{ 
			if(t[j]) 
			{ 
				int dist = i-j; 
				dist--; 
				w[i].X = min(w[i].X,dist); 
			} 
		}
		FOR(j,i+1,n+1) 
		{ 
			if(t[j]) 
			{ 
				int dist = j-i; 
				dist--; 
				w[i].Y=min(w[i].Y,dist); 
			} 
		} 
	}
	FOR(i,1,n) 
	{ 
		if(t[i]) continue;
		if(min(result.X,result.Y) < min(w[i].X,w[i].Y)) 
		{ 
			result = w[i]; 
		} 
		else if(min(result.X,result.Y) == min(w[i].X,w[i].Y))
		{ 
			if(max(result.X,result.Y) < max(w[i].X,w[i].Y))
				result = w[i]; 
		} 
	}
	printf("Case #%d: %d %d\n",++cou,max(result.X,result.Y),min(result.X,result.Y)); 

} 

int main()
{
	scanf("%d",&T); 
	while(T--) 
		solve(); 
} 
