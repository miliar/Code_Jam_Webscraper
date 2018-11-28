#include <iostream> 
#include <cstdio>
#include <queue>
#include <cmath>
#include <iomanip>


using namespace std;

#define For(i , a , b) for (int i = a , _b = b ; i <= _b ; ++i)
#define Ford(i , a  ,b) for (int i = a , _b = b : i >= _b ; --i)
#define Rep(i , n) for (int i = 0 , _n = n ; i < _n ; ++i)
#define sz(A) ((int)A.size())
#define LL(x) (x << 1)
#define RR(x) ((x << 1) | 1)

typedef pair<int , int> pt;

const int maxn = 100 + 123;
int n, qr;
long long d[maxn][maxn];
int sp[maxn], e[maxn];
const long long INF = 1000LL * 1000 * 1000 * 1000 * 1000 * 1000 + 123;

void ReadData() {
	cin >> n >> qr;
	For(i,1,n) cin >> e[i] >> sp[i];
	For(i,1,n) For(j,1,n) cin >> d[i][j];
	For(i,1,n) For(j,1,n) if (d[i][j] == -1) d[i][j] = INF;
	For(i,1,n) d[i][i] = 0;
	For(k,1,n) For(i,1,n) For(j,1,n) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
	//cout << d[1][2] << endl;
}	

const long double eps = 1e-9;
long double f[maxn];
void Process(int test) {
	cout << "Case #" << test << ": ";
	cout << fixed << setprecision(9);
	For(z,1,qr) {
		int s, t; cin >> s >> t;
		For(i,1,n) f[i] = INF;
		f[s] = 0;
		priority_queue<pair<long double, int> > qu;
		qu.push(make_pair(0,s));
		
		while (sz(qu)) {
			auto cur = qu.top(); qu.pop();
			int u = cur.second; 
			long double z = -cur.first;
			if (abs(f[u] - z) > eps) continue;
			if (f[u] != z) continue;
			For(v,1,n) if (v != u) if (d[u][v] <= e[u] && d[u][v] < INF) {
				long double tmp = f[u] + (long double) d[u][v] / sp[u];

				if (tmp < f[v]) {
					f[v] = tmp;
					qu.push(make_pair(-f[v], v));
				}
			}
		}	


		
		cout << (double) f[t] << " ";
	}
	cout << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
//	freopen("input.inp" , "r" , stdin);
	//freopen("output.out" , "w" , stdout);
	int test; cin >> test;
	For(i,1,test) {
		ReadData();
		Process(i);
	}

	return 0;

}			