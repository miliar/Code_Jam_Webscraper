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
#ifdef LOCAL
    #define D(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
    #define D(...) ;
    #define cerr if(0)cout
#endif
using namespace std;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T, U> &_p) { return os << "(" << _p.X << "," << _p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& _V) { bool f = true; os << "["; for(auto v: _V) { os << (f ? "" : ",") << v; f = false; } return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& _S) { bool f = true; os << "("; for(auto s: _S) { os << (f ? "" : ",") << s; f = false; } return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& _M) { return os << set<pair<T, U>>(ALL(_M)); }
template<class TH> void _dbg(const char *sdbg, TH h){ cerr<<sdbg<<'='<<h<<endl; }template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) { while(*sdbg!=','){cerr<<*sdbg++;}cerr<<'='<<h<<", "; _dbg(sdbg+1, a...); }

typedef signed long long slong;
typedef long double ldouble;
const slong INF = 1000000100;
const ldouble EPS = 1e-9;

typedef vector<int> state;

 bitset<1010> O[3][3][1010][1010];

void dfs(vector<int> st, int g, int f) {
	O[f][g][st[0]][st[1]][st[2]] = 1;
	if(st[0]+st[1]+st[2] == 1001) return;

	FOR(i,0,2) if(i != g) {
		st[i]++;
		if(O[f][i][st[0]][st[1]][st[2]] == 0)
		dfs(st,i,f);
		st[i]--;
	}

}

#define IMP {printf("Case #%d: IMPOSSIBLE\n", t); return;}

string base[] = {"R","Y","B"};

string get(state st, int f, int l) {
	if(st[0]+st[1]+st[2] == 1){
		if(st[f] == 1) return base[f];
		assert(false);
	}
	st[l]--;
	FOR(pop, 0, 2) if(pop != l) {
		if(O[f][pop][st[0]][st[1]][st[2]]) return get(st,f,pop) + base[l];
	}
	assert(false);
}

void solve(int t) {
	int n,r,o,y,g,b,v;
		scanf("%d%d%d%d%d%d%d", &n,&r,&o,&y,&g,&b,&v);
		if(n == 1) {
			if(r == 1) printf("Case #%d: R\n",t);
			if(o == 1) printf("Case #%d: O\n",t);
			if(y == 1) printf("Case #%d: Y\n",t);
			if(g == 1) printf("Case #%d: G\n",t);
			if(b == 1) printf("Case #%d: B\n",t);
			if(v == 1) printf("Case #%d: V\n",t);
			return;
		}

		if(n == b+o and b == o) {
			printf("Case #%d: ", t);
			FOR(i,1,b) printf("BO"); printf("\n");
			return;
		}
		if(n == y+v and y==v) {
			printf("Case #%d: ", t);
			FOR(i,1,v) printf("YV"); printf("\n");
			return;
		}
		if(n == r+g and r==g) {
			printf("Case #%d: ", t);
			FOR(i,1,r) printf("RG"); printf("\n");
			return;
		}

		if(v != 0) {
			y -= v;
			if(y <= 0) IMP;
		}
		if(o != 0) {
			b -= o;
			if(b <= 0) IMP;
		}
		if(g != 0) {
			r -= g;
			if(r <= 0) IMP;
		}
		int stp = -1;
		state st = {r,y,b};
		FOR(i,0,2) {
			st[i]++;
			if(O[i][i][st[0]][st[1]][st[2]]) stp=i;
			st[i]--;
		}
		if(stp == -1) IMP;
		st[stp]++;
		auto s = get(st, stp, stp);
		string res;

		for(auto c : s) {
			while(c == 'B' and o > 0) {
				o--;
				res += "BO";
			}
			while(c == 'Y' and v > 0) {
				v--;
				res += "YV";
			}
			while(c == 'R' and g > 0) {
				g--;
				res += "RG";
			}
			res += c;
		}
		
		res = res.substr(0,SIZE(res)-1);

		cout << "Case #" << t << ": " << res << endl;

}

int main() {
	dfs({1,0,0},0,0);
	dfs({0,1,0},1,1);
	dfs({0,0,1},2,2);

	int t;
	scanf("%d",&t);
	FOR(T,1,t) {
		solve(T);
	}
}
