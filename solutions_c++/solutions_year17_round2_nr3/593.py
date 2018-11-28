#include <bits/stdc++.h>

#define INF 0x3F3F3F3F
#define DINF 1e+12
#define rep(i, a, b) for (int i = int(a); i < int(b); i++)
#define pb push_back
#define pi 3.1415926535897932384626433832795028841971
#define debug(x) if(1) cout << #x << " = " << x << endl;
#define debug2(x,y) cout << #x << " = " << x << " --- " << #y << " " << y << "\n";
#define all(S) (S).begin(), (S).end()
#define MAXV 1005
#define F first
#define S second
#define EPS 1e-9
#define mp make_pair

using namespace std;

typedef long long ll;
typedef pair < int, int >  ii;

int N;
int dis[105];
int vel[105];
ll g[105][105];
double m[105][105];

void floyd(){
	rep(k,0,N)
	rep(i,0,N)
	rep(j,0,N)
	if(g[i][j] > g[i][k] + g[k][j])
	g[i][j] = g[i][k] + g[k][j];
}

void floyd2(){
	rep(k,0,N)
	rep(i,0,N)
	rep(j,0,N)
	if(m[i][j] > m[i][k] + m[k][j])
	m[i][j] = m[i][k] + m[k][j];
}

int main(){
	
 //freopen("clarge.in", "r", stdin);
 //freopen("outc2.txt", "w", stdout);
	
	int Q;
	int tc, tt=1;
	
	cin >> tc;
	
	while(tc--){
		
		cin >> N >> Q;
		
		rep(k, 0, N){
			cin >> dis[k] >> vel[k];
		}
		
		rep(i, 0, N){
			rep(j, 0, N)
				g[i][j] = DINF;
			g[i][i] = 0;
		}
		
		rep(i, 0, N){
			rep(j, 0, N){
				scanf("%lld", &g[i][j]);
				if(g[i][j] == -1) g[i][j] = DINF;
			}
		}
		
		floyd();
		
//		rep(i, 0, N){
//			rep(j, 0, N){
//				cout << g[i][j] << " ";
//			}
//			cout << endl;
//		}
//		
		rep(i, 0, N){
			rep(j, 0, N)
				m[i][j] = DINF;
			m[i][i] = 0.0;
		}

		rep(k, 0, N){ 
			rep(j, 0, N){
				if(j == k){
					m[j][k] = 0.0;
					continue;
				}
				if(g[k][j] <= dis[k]){ // se o cavalo k chega em j
					double t = (double)g[k][j]/vel[k];
					m[k][j] = t;
				}
			}
		}
		
		floyd2();
		
		int a, b;
		printf("Case #%d:", tt++);
		while(Q--){
			cin >> a >> b;
			--a; --b;
			printf(" %.6lf", m[a][b]);
		}
		printf("\n");
	}
	
	return 0;
}
