#include <bits/stdc++.h>

#define REP(i, n) for(int i = 0; i < n; i++)

#define SIZE 123
#define INF 1.0e+30
#define EPS 1.0e-6

using namespace std;

typedef long double ld;
typedef long long ll;


// Only easy dataset

int d[SIZE][SIZE];
double dist[SIZE][SIZE];
int e[SIZE], s[SIZE];
int n;


void fw(){
	REP(i, n)REP(j, n){
		if(d[i][j] == -1) dist[i][j] = i==j ? 0 : INF;
		else dist[i][j] = d[i][j];
	}

	REP(k, n)REP(i, n)REP(j, n){
		dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
	}
}

void edit_dist(){
	REP(i, n){
		double endurance = e[i], speed = s[i];
		REP(j, n){
			if(dist[i][j] <= endurance+EPS)dist[i][j]/=speed;
			else dist[i][j] = INF;
		}
	}
}

void fw2(){
	REP(k, n)REP(i, n)REP(j, n){
		dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
	}
}


void testcase(int tcn){
	
	int u, v, q;
	cin >> n >> q;

	REP(i, n){
		cin >> e[i] >> s[i];
	}

	REP(i, n)REP(j, n){
		cin >> d[i][j];
	}

	fw();
	edit_dist();
	fw2();


	cout << "Case #"<<tcn<<":";
	REP(i, q){
		cin >> u >> v;
		--u;--v;
		cout << " " << setprecision(9) << dist[u][v];
	}





	cout << endl;

}

int main(){
	int T;
	cin >> T;
	REP(i, T){
		testcase(i+1);
	}
	return 0;

}