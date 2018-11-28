#include <cstdio> 
#include <cstdlib> 
#include <ctime> 
#include <cstring> 
#include <iostream> 
#include <cmath> 
#include <string> 
#include <vector> 
#include <algorithm> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 

using namespace std; 

typedef unsigned int uint; 
typedef long long int64; 
typedef unsigned long long uint64; 
typedef unsigned short ushort; 
typedef unsigned char uchar; 
typedef pair<int,int> ipair; 
typedef vector<int> VI; 
typedef vector<string> VS; 
typedef vector<double> VD; 
#define SIZE(A) ((int)(A.size()))
#define LENGTH(A) ((int)(A.length()))
#define MP(A,B) make_pair(A,B)
const double pi = acos(-1.0); 

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,a) for(int i=0;i<(a);++i)
#define ALL(a) (a).begin(),(a).end()

template<class T> T sqr(const T &x) { return x*x; } 
template<class T> T lowbit(const T &x) { return (x^(x-1))&x; } 
template<class T> int countbit(const T &n) { return (n==0)?0:(1+countbit(n&(n-1))); } 
template<class T> void ckmin(T &a,const T &b) { if (b<a) a=b; } 
template<class T> void ckmax(T &a,const T &b) { if (b>a) a=b; } 




int n, Q;
long long dis[105];
long long speed[105];
double a[105][105];
double f[105][105];
int u[105], v[105];

void parse() {	
	cin >> n >> Q;

	for (int i = 1; i <=n; i++ )
		cin >> dis[i] >> speed[i];

	for (int i = 1; i <=n; i++)
		for (int j = 1; j <= n; j++)
			cin >> a[i][j];
		
	for (int i = 0; i < Q; i++)
		cin >> u[i] >> v[i];
}

void sp(){
	for (int i = 1; i <= n; i++)
		a[i][i] = 0;

	for (int k = 1; k <= n; k++)
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++){
				if (a[i][k] == -1 || a[k][j] == -1) continue; 
				
				if (a[i][j] == -1)
					a[i][j] = a[i][k] + a[k][j];
				else
				if (a[i][k] + a[k][j] < a[i][j])
					a[i][j] = a[i][k] + a[k][j];
			}

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			if (i == j)
				f[i][j] = 0;
			else f[i][j] = -1;

	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++) {
			if (i == j) continue;
			if (a[i][j] == -1) continue;
			if (a[i][j] > dis[i]) continue;
			else f[i][j] = a[i][j] / speed[i];
		}

	
}

void solve() {
	sp();
	
	/*
	for (int i = 1; i <= n; i++)
		for (int j = 1; j <= n; j++)
			f[i][j] = w[i][j];
	*/

	for (int k = 1; k <= n; k++ )
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= n; j++){
				if (f[i][k] == -1 || f[k][j] == -1) continue;
				
				if (f[i][j] == -1) 
					f[i][j] = f[i][k] + f[k][j];
				else
				if (f[i][k] + f[k][j] < f[i][j])
					f[i][j] = f[i][k] + f[k][j];
			}

	//cout << u[0] << " " <<  v[0] << " " << f[u[0]][v[0]] << endl;
	for (int i = 0; i < Q-1; i++)
		printf("%.6f ",f[u[i]][v[i]]);
	printf("%.6f\n", f[u[Q-1]][v[Q-1]]);

}

int main() {
	int T;
	cin >> T;
	for (int kase = 1; kase <= T; kase++) {
		parse();
		printf("Case #%d: ", kase);
		solve();
	}
	return 0;
}