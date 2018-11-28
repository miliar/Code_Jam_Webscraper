#include <bits/stdc++.h>
using namespace std;
#define int long long
const double INF = 1e13;
main (){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout << fixed;
	cout << std::setprecision(6);
	int z;
	cin >> z;
	for (int casess = 1; casess <= z; ++casess){
		int n;
		cin >> n;
		int q;
		cin >> q;
		vector <vector <int > > dst(n, vector <int> (n, -1));
		vector <vector <double > > ndst(n, vector <double> (n, INF)); 
		vector <int> spedh(n,0), dish(n,0);
		for (int i = 0; i < n; ++i){
			cin >> dish[i] >> spedh[i];
		}
		for (int i = 0; i < n; ++i){
			for (int  j = 0; j < n; ++j){
				cin >> dst[i][j];
				if(dst[i][j] == -1)dst[i][j] = (int)1e9 + 10;
			}
		}
		
		for (int k = 0; k < n; ++k){
			for (int i = 0; i < n; ++i){
				for (int j = 0; j < n; ++j){
					if(dst[i][j] > dst[i][k] + dst[k][j])
						dst[i][j] = dst[i][k] + dst[k][j];
				}
			}
		}
		
		for (int i = 0; i < n; ++i){
			for (int j =0; j < n; ++j){
				if(dst[i][j] <= dish[i]){
					ndst[i][j] =  (((double)dst[i][j])/ ((double)spedh[i]));
				}
				else ndst[i][j] = INF;
			}
		}
		
		for (int k = 0; k < n; ++k){
			for (int i = 0; i < n; ++i){
				for (int j = 0; j < n; ++j){
					if(ndst[i][j] > ndst[i][k] + ndst[k][j])
						ndst[i][j] = ndst[i][k] + ndst[k][j];
				}
			}
		} 
		cout <<"Case #" << casess <<": ";
		for (int i = 0; i < q; ++i){
			int a,b;
			cin >> a >> b;
			--a;
			--b;
			assert(ndst[a][b] <= INF);
			cout << ndst[a][b] << ' '; 
		}
		cout <<'\n';
		 
	}
}
