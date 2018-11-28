#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <stack>
#include <algorithm>
#define MOD 1000000007
#define forn(a, n) for(int a = 0; a<(int) (n); ++a)
#define dforn(a, n) for(int a = (n)-1; a>=0; --a)
#define forall(a, all) for(__typeof(all.begin()) a = all.begin(); a != all.end(); ++a)
#define EPS 0.000000000001
typedef long long tint;
using namespace std;

vector<int> buscarCaminoDeAumento(vector<vector<pair<int, int> > > &redResidual, int fuente, int sumidero) {
	int n = redResidual.size();
	vector<pair<int, int> > predecesor(n, pair<int, int>(-1, -1));
	
	queue<int> bfs;
	bfs.push(fuente);
	predecesor[fuente] = pair<int, int>(fuente, -1);
	while(!bfs.empty()) {
		int actual = bfs.front();
		bfs.pop();
		
		int cantidadVecinos = redResidual[actual].size();
		forn(i, cantidadVecinos) {
			int siguiente = redResidual[actual][i].first;
			if(redResidual[actual][i].second > 0 && predecesor[siguiente].first == -1) {
				bfs.push(siguiente);
				predecesor[siguiente] = pair<int, int>(actual, i);
			}
		}
	}
	
	vector<int> caminoDeAumento;
	if(predecesor[sumidero].first != -1) {
		int actual = sumidero;
		while(actual != fuente) {
			caminoDeAumento.push_back(predecesor[actual].second);
			actual = predecesor[actual].first;
		}
		reverse(caminoDeAumento.begin(), caminoDeAumento.end());
	}
	
	return caminoDeAumento;
}

int actualizarRedResidual(vector<vector<pair<int, int> > > &redResidual, vector<vector<int> > &backEdges, vector<int> &caminoDeAumento, int fuente) {
	int longitudCamino = caminoDeAumento.size();
	
	int actual = fuente, maximoFlujoCamino = redResidual[fuente][caminoDeAumento[0]].second;
	forn(i, longitudCamino) {
		int eje = caminoDeAumento[i];
		maximoFlujoCamino = min(maximoFlujoCamino, redResidual[actual][eje].second);
		actual = redResidual[actual][eje].first;
	}
	
	actual = fuente;
	forn(i, longitudCamino) {
		int eje = caminoDeAumento[i];
		redResidual[actual][eje].second -= maximoFlujoCamino;
		int siguiente = redResidual[actual][eje].first, backEdge = backEdges[actual][eje];
		redResidual[siguiente][backEdge].second += maximoFlujoCamino;
		actual = siguiente;
	}
	
	return maximoFlujoCamino;
}

vector<vector<int> > armarRedResidual(vector<vector<pair <int, int> > > &grafo, vector<vector<pair <int, int> > > &redResidual) {
	int n = grafo.size();
	vector<vector<int> > backEdges = vector<vector<int> >(n);
	redResidual = vector<vector<pair <int, int> > >(n);
	
	forn(actual, n) {
		forn(i, grafo[actual].size()) {
			int siguiente = grafo[actual][i].first;
			backEdges[siguiente].push_back(redResidual[actual].size());
			redResidual[actual].push_back(grafo[actual][i]);
			backEdges[actual].push_back(redResidual[siguiente].size());
			redResidual[siguiente].push_back(pair<int,int>(actual, 0));
		}
	}
	return backEdges;
}

vector<vector<pair <int, int> > > edmondKarp(vector<vector<pair <int, int> > > &grafo, int fuente, int sumidero){
	vector<vector<pair <int, int> > > redResidual;
	vector<vector<int> > backEdges = armarRedResidual(grafo, redResidual);
	
	int flujoMaximo = 0;
	vector<int> caminoDeAumento = buscarCaminoDeAumento(redResidual, fuente, sumidero);
	
	while(!caminoDeAumento.empty()) {
		flujoMaximo += actualizarRedResidual(redResidual, backEdges, caminoDeAumento, fuente);
		caminoDeAumento = buscarCaminoDeAumento(redResidual, fuente, sumidero);
	}
		
	return redResidual;
}

map<char, int> trad = {{'.', 0}, {'+',1}, {'x',2}, {'o',3}};
vector<char> back = {'.','+','x','o'};

int main()
{
#ifdef ACMTUYO
	freopen("D-large(1).in","r",stdin);
	freopen("D-large(1).out","w",stdout);
#endif
	
	int C;
	cin >> C;
	forn(tc, C) {
		int n, m;
		cin >> n >> m;
		vector<vector<int> > tabini(n, vector<int>(n, 0));
		vector<vector<int> > tabfin(n, vector<int>(n, 0));
		
		forn(i, m) {
			char c;
			int y, x;
			cin >> c >> y >> x;
			y--; x--;
			tabini[y][x] = trad[c];
			tabfin[y][x] = trad[c];
		}
		
		vector<vector<pair<int, int> > > grafox(2*n+2);
		forn(i, n) {
			int filval = 1;
			forn(j, n) {
				if(tabini[i][j]/2){
					filval = 0;
				}
			}
			if(filval) {
				grafox[2*n].push_back(make_pair(i, 1));
			}
			
			int colval = 1;
			forn(j, n) {
				if(tabini[j][i]/2){
					colval = 0;
				}
			}
			if(colval) {
				grafox[n+i].push_back(make_pair(2*n+1, 1));
			}
		}
		
		forn(i, n) {
			forn(j, n) {
				grafox[i].push_back(make_pair(n+j, 1));
			}
		}
		
		grafox = edmondKarp(grafox, 2*n, 2*n+1);
		forn(i, n)  {
			forn(j, grafox[n+i].size()) {
				int a = grafox[n+i][j].first, b = grafox[n+i][j].second;
				if(b && a<n){
					tabfin[j][i]+=2;
				}
			}
		}
		
		vector<vector<pair<int, int> > > grafom(4*n);
		vector<int> diags(2*n-1, 1), diagr(2*n-1, 1);
		forn(i, n){
			forn(j, n){
				grafom[i+j].push_back(make_pair(i-j+n-1+2*n-1, 1));
				if(tabini[i][j]%2) {
					diags[i+j] = 0;
					diagr[i-j+n-1] = 0;
				}
			}
		} 
		forn(i, 2*n-1) {
			if(diags[i]) {
				grafom[4*n-2].push_back(make_pair(i, 1));
			}
			if(diagr[i]){
				grafom[i+2*n-1].push_back(make_pair(4*n-1, 1));
			}
		}
		grafom = edmondKarp(grafom, 4*n-2, 4*n-1);
		forn(i, 2*n-1) {
			forn(j, grafom[i+2*n-1].size()) {
				int a = grafom[i+2*n-1][j].first, b = grafom[i+2*n-1][j].second;
				if(b && a < 2*n-1) {
					int y = ((i-n+1)+a)/2, x = (a-(i-n+1))/2;
					tabfin[y][x]++;
				}
			}
		}
		
		int poi = 0, cha = 0;
		forn(i, n) {
			forn(j, n) {
				if(tabfin[i][j]!=tabini[i][j]) cha++;
				if(tabfin[i][j]%2) poi++;
				if(tabfin[i][j]/2) poi++;
			}
		}
		cout << "Case #" << tc+1 << ": "; 
		cout << poi << " " << cha << endl;
		forn(i, n) {
			forn(j, n) {
				if(tabfin[i][j]!=tabini[i][j]) {
					cout << back[tabfin[i][j]] << " " << i+1 << " " << j+1 << endl;
				}
			}
		}
	}
	
	return 0;
}
