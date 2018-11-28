#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <string.h>

#include <vector>
#include <limits>
#include <queue>
#include <cstdlib>
#include <map>
#include <math.h>
#include <limits>
#include <time.h>
#include <bitset>
#include <set>
#include <stack>
#include <iomanip>
#include <complex>
#include <ctime>
using namespace std;
#define ll long long

#define endl '\n'

#define MAXN 105

int n, q;
int Ei[MAXN], Si[MAXN];

double oo = 1e16;

struct edge {
	int v, d;
	edge(){}
	edge(int vv,int dd) {
		v = vv;
		d = dd;
	}
};

struct arco {
	int v;
	double t, vel;
	int km;

	arco(){}
	arco(int vv,double tt, int kmm, double velv) {
		v = vv;
		t = tt;
		km = kmm;
		vel = velv;
	}

	bool operator<(const arco b) const {
		if (t != b.t) return t > b.t;
		if (km != b.km) return km < b.km;
		return vel > b.vel;
	}
};

vector<edge> ady[MAXN];

priority_queue<arco> cola;

double T[MAXN][MAXN];
int KM[MAXN][MAXN];


void solve() {
	cin >> n >> q;

	for(int i=0;i<n;i++) {
		ady[i].clear();

	}

	for(int i=0;i<n;i++) {
		cin >> Ei[i] >> Si[i];
	}
	for(int i=0;i<n;i++)
		for(int j=0;j<n;j++) {
			int d;
			cin >> d;
			if (d == -1) continue;
			ady[i].push_back(edge(j, d));
		}

	for(int start=0;start<n;start++) {

		for(int i=0;i<n;i++) {
			T[start][i] = oo;
			KM[start][i] = -1;
		}
		T[start][start] = 0;

		cola.push(arco(start, 0, Ei[start], Si[start]));

		//cout << "START " << start +1<< endl << endl << endl;

		while (!cola.empty()) {
			arco aux = cola.top(); cola.pop();
			int v = aux.v;

			//printf("%d %.2lf %d %.2lf\n", v + 1, aux.t, aux.km, aux.vel);

			if (T[start][v] > aux.t)
				T[start][v] = aux.t;

			if (KM[start][v] >= aux.km) continue;

			KM[start][v] = aux.km;

			for(int i=ady[v].size()-1;i>=0;i--) {
				int u = ady[v][i].v;
				int d = ady[v][i].d;
				if (d <= aux.km) {
					// continuando
					double t1 = (double)d / aux.vel;
					//cout << "   continuando a " << u+1 << " quedando " << aux.km - d << endl;
					cola.push(arco(u, aux.t + t1, aux.km - d , aux.vel));

				}

				if (d <= Ei[v]) {
					// empezando
					double t1 = (double)d / (double)Si[v];
					//cout << "   empezando a " << u+1 << " quedando " << Ei[v] - d << endl;
					cola.push(arco(u, aux.t + t1, Ei[v] - d , Si[v]));
				}
			}
		}

		if (start == 0) {
			for(int i=0;i<3;i++) {
				for(int j=0;j<3;j++) {
		//			cout << setprecision(7) << fixed << T[i][j] << "  ";
				}
		//		cout << endl;
			}
		}
	}

	int a,b;
	bool first = false;
	while (q--) {
		cin >> a >> b;
		a--, b--;

		if (first) cout << " "; else first = true;
		cout << setprecision(7) << fixed << T[a][b];
	}
	cout << endl;
}

int main(){
	//freopen("/Users/jcfernandez/Downloads/CodeJam/input.txt", "r", stdin);
	//freopen("/Users/jcfernandez/Downloads/CodeJam/output.txt", "w", stdout);


	int cas, caso = 1;
	cin >> cas;
	while(cas--) {
		cout << "Case #" << caso++ << ": ";
		solve();
	}
	return 0;
}
