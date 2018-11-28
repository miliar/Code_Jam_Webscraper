#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i=(a); i<(b); i++)
#define pb push_back
#define mk make_pair
#define debug(x) cout<<__LINE__<<": "<<#x<<" = "<<x<<endl;
#define all(c) (c).begin(), (c).end()
#define F first
#define S second
#define UNIQUE(c) sort(all(c)); (c).resize(unique(all(c))-c.begin());
#define pi 3.1415926535897932384626433832795028841971

typedef long long ll;
typedef pair<int, int> ii;
const int INF = 0x3f3f3f3f;
const double LINF = (1LL<<60);
const double EPS = 1e-9;

inline int cmp(double x, double y = 0, double tol = EPS){
	return ((x <= y+tol) ? (x+tol < y) ? -1:0:1); }


string int2str(int x){ stringstream ss; string str; ss << x; ss >> str;  return str; }
int str2int(string str){ stringstream ss; int x; ss << str; ss >> x;  return x; }

int N, Q;
double E[110]; 
double S[110];

double D[110][110];
double T[110][110];

int main(){
	int tn; cin >> tn;
	rep(t,0,tn) {
		
		cin >> N >> Q;
		rep(i,0,N){
			cin >> E[i] >> S[i];
		}
		rep(i,0,N){
			rep(j,0,N){
				cin >> D[i][j];
				if (D[i][j] < 0) D[i][j] = LINF;
				if (i == j) D[i][j] = 0;
			}
		}
		
		// floyd -> Distancia
		rep(k,0,N)
			rep(i,0,N)
				rep(j,0,N)
					D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
	
		rep(i,0,N)
			rep(j,0,N){
				T[i][j] = LINF;
				if (i == j) T[i][j] = 0;
			}
		
		
		// creating edges
		rep(x,0,N){
			rep(y,0,N){
				if (x == y) continue;
				double dist = D[x][y];
				if (dist > E[x]) continue;
				T[x][y] = D[x][y] / S[x];				
			}
		}
		
		// floyd -> tempo
		rep(k,0,N)
			rep(i,0,N)
				rep(j,0,N)
					T[i][j] = min(T[i][j], T[i][k] + T[k][j]);
					
		
		vector<double> ans;
		while (Q--){
			int x, y;
			cin >> x >> y;
			x--, y--;
			ans.pb(T[x][y]);
		}
		
		printf("Case #%d:", (t+1));
		rep(i,0,ans.size())  printf(" %.8lf", ans[i]);
		printf("\n");
				
	}
	return 0;
}









