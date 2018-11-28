#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

vector < vector < int > > grafo;
int n;

pair < int, double > cavalo[1000];
int dist[1001][1001];
//double custo[101][1001][101];
map < pair < int, pair < int, int > >, double > custo;

double solve( int de, int para ){
	/*for(int i = 0; i < n; i++){
		for(int j = 0; j < 1001; j++){
			for(int w = 0; w < 101; w++){
				custo[i][j][w] = 1152921504606846976.;
			}
		}
	}*/
	custo.clear();

	priority_queue < pair < double, pair < int, pair < int, int > > > > fila;

	fila.push(make_pair(0, make_pair(de, make_pair ( -cavalo[de].first, de))));
	pair < int, pair < int, int > > m = (make_pair(de, make_pair(cavalo[de].first, de)));
	custo[m] = 0;

	while(!fila.empty()){
		pair < double, pair < int, pair < int, int > > > f = fila.top();
		fila.pop();

		double c = -f.first;
		int at = f.second.first;
		int tanto = -f.second.second.first;
		int at_c = f.second.second.second;

		if( at == para ) return c;

		for(int i = 0; i < grafo[at].size(); i++){
			int px = grafo[at][i];
			double tot = double(dist[at][px])/cavalo[at_c].second;
			if( dist[at][px] <= tanto ){
				int qt = tanto - dist[at][px];
				m = (make_pair(at, make_pair(qt, at_c)));
				if( !custo.count(m) || !(custo[m] < (c + tot)) ){
					custo[m] = (c + tot);
					fila.push(make_pair(-(c + tot), make_pair(px, make_pair(-qt, at_c))));
				}
				m = (make_pair(at, make_pair(cavalo[px].first, px)));
				if( !custo.count(m) || custo[m] > (c + tot) ){
					custo[m] = (c + tot);
					fila.push(make_pair(-(c + tot), make_pair(px, make_pair(-cavalo[px].first, px))));
				}
			}
		}
	}

	return 0.;
}


int main(){
	ios::sync_with_stdio(false);
	int t, q, de, para, val;
	
	cin >> t;

	for(int w = 1; w <= t; w++){
		grafo.clear();
		cin >> n >> q;

		for(int i = 0; i < n; i++) cin >> cavalo[i].first >> cavalo[i].second;

		grafo.resize(n+10);

		for(int i = 0; i < n; i++){
			for(int j = 0; j < n; j++){
				cin >> val;
				dist[i][j] = val;
				if( val != -1 ){
					grafo[i].push_back(j);
				}
			}
		}
		cout << "Case #" << w << ":";
		while( q-- ){
			cin >> de >> para;
			de--; para--;
			cout << " " << fixed << setprecision(6) << solve(de, para);
		}
		cout << endl;
	}

	return 0;
}