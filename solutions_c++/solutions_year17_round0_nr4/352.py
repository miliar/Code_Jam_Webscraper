#include <bits/stdc++.h>

using namespace std;
#define PB push_back
#define MP make_pair
#define LL long long
#define int LL
#define FOR(i,a,b) for (int i = (a); i <= (b); i++)
#define REP(i,n) FOR(i,0,(int)(n)-1)
#define RE(i,n) FOR(i,1,n)
#define R(i,n) REP(i,n)
#define FI first
#define SE second
#define st FI
#define nd SE
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define VI vector<int>
#define PII pair<int,int>
#define LD long double

template<class C> void mini(C& a4, C b4) { a4 = min(a4, b4); }
template<class C> void maxi(C& a4, C b4) { a4 = max(a4, b4); }

template<class TH> void _dbg(const char *sdbg, TH h){cerr<<sdbg<<"="<<h<<"\n";}
template<class TH, class... TA> void _dbg(const char *sdbg, TH h, TA... a) {
  while(*sdbg!=',')cerr<<*sdbg++;cerr<<"="<<h<<","; _dbg(sdbg+1, a...);
}

template<class T> ostream &operator<<(ostream &os, vector<T> V){
  os<<"[";for(auto vv:V)os<<vv<<",";return os<<"]";
} 

template<class L, class R> ostream &operator<<(ostream &os, pair<L,R> P) {
  return os << "(" << P.st << "," << P.nd << ")";
}


#ifdef LOCAL
#define debug(...) _dbg(#__VA_ARGS__, __VA_ARGS__)
#else
#define debug(...) (__VA_ARGS__)
#define cerr if(0)cout
#endif

const int inf = 1e9;

struct Sol{
	int n,m;
	vector<int> row, col;
	map<int,int> d1,d2;
	vector<vector<char>> grid;
	set<PII> res;
	vector<vector<int>> d;
	map<int,int> s;
	vector<int> sa;
	vector<int> cz;
	bool nima(int i){
		auto xxx = s.find(i);
		return xxx == s.end();
	}
	bool dfs(int v){
		if(cz[v])return 0;
		cz[v] = 1;
		for(int ak:d[v]){
			if(nima(ak) || dfs(s[ak])){
				s[ak] = v;
				sa[v] = ak;
				return 1;
			}
		}
		return 0;
	}
	
  	void run(int cas){
		cin >> n >> m;
		row.resize(n);
		col.resize(n);
		grid.resize(n,vector<char>(n,'.'));
		d.resize(n*2);
		int earn = 0;
		R(i,m){
			char z;
			int a,b;
			cin >> z >> a >> b;
			a--;b--;
			grid[a][b] = z;
			if(z == 'x' || z == 'o'){
				row[a] = 1;
				col[b] = 1;
			}
			if(z == '+' || z == 'o'){
				d1[a+b] = 1;
				d2[a-b] = 1;
			}
			earn++;
			if(z == 'o'){
				earn++;
			}
		}
		R(i,n)R(j,n){
			if(row[i] == 0 && col[j] == 0){
				debug(i,j);
				if(grid[i][j] == '.'){
					grid[i][j] = 'x';
				}else
					grid[i][j] = 'o';
				earn ++;	
				res.insert({i,j});
				row[i] = col[j] = 1;
			}
			if(d1[i + j] == 0 && d2[i - j] == 0){
				d[i + j].PB(i - j);
			}
		}
		bool x = 1;
		cz.resize(2*n);
		sa.resize(2*n, inf);
		while(x){
			x = 0;
			R(i,n*2) cz[i] = 0;
			R(i,n*2) if(sa[i] == inf) {
				if(dfs(i)) x = 1;
			}
		}
		
		R(i,n)R(j,n){
		 	if(sa[i+j] == i-j){
				if(grid[i][j] == '.'){
					grid[i][j] = '+';
				}else
					grid[i][j] = 'o';
				earn ++;	
				res.insert({i,j});
			}
		}
		
		cout << "Case #" << cas << ": " << earn << " " << SZ(res) << "\n";
		for(PII ak : res){
			cout << grid[ak.FI][ak.SE] << " " << ak.FI + 1 << " " << ak.SE + 1 << "\n"; 
		}
		cerr << "\n";
		R(i,n){
			int ilx = 0,ily = 0;
			R(j,n){
				if(grid[i][j] == 'x' || grid[i][j] == 'o')ilx++;
				if(grid[j][i] == 'x' || grid[j][i] == 'o')ily++;
			}
			assert(ilx <= 1);
			assert(ily <= 1);
		}
		map<int,int> prze1, prze2;
		R(i,n)R(j,n){
			if(grid[i][j] == '+' || grid[i][j] == 'o'){
				prze1[i+j]++;
				prze2[i-j]++;
				assert(prze1[i+j] < 2);
				assert(prze2[i-j] < 2);
			}
		}
    
	}
};

int32_t main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout << fixed << setprecision(11);
	cerr << fixed << setprecision(6);
	int t;
	cin >> t;
	R(i,t){
		Sol sol;
		sol.run(i+1);
	}
}
