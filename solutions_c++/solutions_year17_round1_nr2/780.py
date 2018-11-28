#include <bits/stdc++.h>
#define endl '\n'
#define forn(i, n) for(int i=0;i<n;i++)
#define fore(i, a, b) for(int i=a;i<=b;i++)
#define lli long long int
#define pb(a) push_back(a)
#define pii pair<int,int>
#define fi first
#define se second
#define DEBUG 0

using namespace std;

const int MAXN = 55;

int aux[MAXN];
int cont[MAXN];
double num[MAXN];
int L[MAXN][MAXN];
int R[MAXN][MAXN];
double mat[MAXN][MAXN];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	if(!DEBUG) {
		freopen("B.in", "r", stdin);
		freopen("B.out", "w", stdout);
	}
	int t,n,p,u=1;
	cin>>t;
	while(t--) {
		cin>>n>>p;
		forn(i, n) cin>>num[i];

		int ans = 0;
		forn(i, n)
		forn(j, p) {
			L[i][j] = R[i][j] = -1;

			cin>>mat[i][j];
			int ini = 1, fin = 1e8;
			while(ini < fin) {
				int med = (ini + fin) / 2;
				double needed = med * num[i] * 1.10;
				if(needed < mat[i][j]) ini = med + 1;
				else fin = med;
			}
			double uno = ini * num[i] * 0.90, dos = ini * num[i] * 1.10;
			if(mat[i][j] < uno || mat[i][j] > dos) continue;
			
			L[i][j] = ini;

			ini = 1, fin = 1e8;
			while(ini < fin) {
				int med = (ini + fin ) / 2;
				double needed = med * num[i] * 0.90;
				if(needed <= mat[i][j]) ini = med + 1;
				else fin = med;
			}
			ini--;
			R[i][j] = ini;
		}

		forn(i, n) cont[i] = aux[i] = 0;

		vector<pii> inicio, fines;
		forn(i, n)
		forn(j, p) {
			if(L[i][j] == -1) continue;
			inicio.pb( pii(L[i][j], i) );
			fines.pb( pii(R[i][j] + 1, i) );
		}

		sort(inicio.begin(), inicio.end());
		sort(fines.begin(), fines.end());
		int i = 0, j = 0, cuantos = 0;
		while(i < inicio.size()) {
			while(j < fines.size() && fines[j].fi <= inicio[i].fi) {
				if(aux[ fines[j].se ]) aux[ fines[j].se ]--;
				else {
					cont[ fines[j].se ]--;
					if(!cont[ fines[j].se ]) cuantos--;
				}
				j++;
			}

			cont[ inicio[i].se ]++;
			if(cont[ inicio[i].se ] == 1) cuantos++;

			while(cuantos == n) {
				forn(h, n) {
					aux[h]++;
					cont[h]--;
					if(!cont[h]) cuantos--;
				}
				ans++;
			}
			i++;
		}

		cout<<"Case #"<<u++<<": "<<ans<<endl;
	}
	return 0;
}
