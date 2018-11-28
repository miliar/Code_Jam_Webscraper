#include <bits/stdc++.h>
using namespace std;
#define all(v) (v).begin(),(v).end()
#define pb push_back
#define sqr(x) ((x)*(x))
#define mp make_pair
#define ones(x) __builtin_popcount(x)
#define fast_io() ios_base::sync_with_stdio(0);cin.tie(0);
#define debug(x) cout << #x << ": " << x << endl;
#define REP(i,x,y) for(int (i)=(x);(i)<(y);(i)++)
#define REPIT(it,A) for(auto it = (A.begin()); it!=A.end();it++)
#define fst first
#define snd second
#define itm1 fst.fst
#define itm2 fst.snd
#define itm3 snd
#define mt(a,b,c) mp(mp(a,b),c)
#define sz(v) int(v.size())
		
typedef pair<int,int> ii;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair< ii, int > tri;
typedef unsigned int uint;

const double PI = acos(-1);
const int  INF = 2e9;
const ll LINF = 1e18 + 5;
const ll MOD = 1e9 + 7;
const int MAXN =  1e5 + 5;
const int MN = 1e6 + 2;

char grid[30][30];
int r, c;
vector< tri > v;

bool algun(int f){
	for(int i = 0; i < c; ++i){
		if(grid[f][i] != '?') return 1;
	}
	return 0;
}

void fill(int cle, int cri, int fle, int fri, char x){
	if(fri < fle) return;
	if(cri < cle) return;
//	cout << "To fill" << endl; 
//	debug(fle);
//	debug(fri);
//	debug(cle);
//	debug(cri);
//	cout << x << endl;
	
	for(int i = fle; i <= fri; ++i){
		for(int j = cle; j <= cri; ++j){
			grid[i][j] = x;
		}
	}

}

int main(){
	fast_io();
	int tc; cin >> tc;
	for(int tt = 1; tt <= tc; ++tt){
		cin >> r >> c;
		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j){
				cin >> grid[i][j];
			}
		}	
		v.clear(); 
		int last = -1;
		for(int i = 0; i < r; ++i){
			if(algun(i)){
				int ext = r - 1; 
				for(int j = i + 1; j < r; ++j){
					if(algun(j)){
						ext = j - 1;
						break; 
					}
				}
				v.pb(mt(last + 1, ext, i));
				last = i;			
			}
		}	
		
		for(int i = 0; i < sz(v); ++i){
			int ini = v[i].itm1;
			int fin = v[i].itm2;
			int ch = v[i].itm3;
//			debug(ini);
//			debug(fin);
//			debug(ch); 
//			cout << "-----------" << endl; 
			int prev = -1;
			for(int j = 0; j < c; ++j){
				if(grid[ch][j] != '?'){
//					cout << "Not ? " << "(" << ch << ", " << j << ")"<< endl; 
					fill(prev + 1, j, ini, fin, grid[ch][j]);
					prev = j;
				}
			}
			fill(prev + 1, c - 1, ini, fin, grid[ch][prev]);
		}
		cout << "Case #" << tt << ":" << endl;
		for(int i = 0; i < r; ++i){
			for(int j = 0; j < c; ++j){
				cout << grid[i][j];
			}
			cout << endl;
		}		


	}
	

	return 0;
}






















