#include <iostream>
#include <queue>
using namespace std;
typedef long long ll;

int n, q;
ll e[200];
ll s[200];
ll dist[200][200];
int partenza, arrivo;
double ans[200];

struct elem{
	double ans;
	int city;
	elem(int c, double a){
		ans = a;
		city = c;
	}
};
bool operator <(elem x, elem y){
	if(x.ans > y.ans) return true;
	if(x.ans < y.ans) return false;
	return (x.city > y.city);
}
priority_queue<elem> coda;

void test_case(){
	cin >> n >> q;
	for(int i=0; i<n; i++) cin >> e[i] >> s[i];
	for(int i=0; i<n; i++) for(int j=0; j<n; j++) cin >> dist[i][j];
	
	for(int i=0; i<n; i++) dist[i][i] = 0;
	for(int k=0; k<n; k++){
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if(dist[i][k]>=0 && dist[k][j]>=0 && (dist[i][j]<0 || dist[i][j] > dist[i][k] + dist[k][j]))
					dist[i][j] = dist[i][k] + dist[k][j];
			}
		}
	}
	//~ for(int i=0; i<n; i++) {for(int j=0; j<n; j++) cerr << dist[i][j] << ' '; cerr << endl;}

	
	for(int ask=0; ask<q; ask++){
		cin >> partenza >> arrivo;
		partenza--;
		arrivo--;
		for(int i=0; i<n; i++) ans[i] = 1e15;
		ans[arrivo] = 0;
		coda.emplace(arrivo, 0);
		while(!coda.empty()){
			int citta = coda.top().city;
			double arr = coda.top().ans;
			coda.pop();
			if(ans[citta]!=arr) continue;
			//~ cerr << "ans(" << citta << ") = " << arr << endl;
			//~ for(int i=0; i<n; i++) {for(int j=0; j<n; j++) cerr << d[i][j] << ' '; cerr << endl;}
			for(int i=0; i<n; i++) if(i!=citta && dist[i][citta]>=0 && dist[i][citta]<=e[i]){
				//~ cerr << dist[i][citta] << endl;
				double na = arr + (double)dist[i][citta]/s[i];
				if(na < ans[i]){
					//~ cerr << "NUOVA " << i << ' ' << na << endl;
					ans[i] = na;
					coda.emplace(i,na);
				}
			}
		}
		cout << fixed << ans[partenza] << ' ';
	}
	cout << endl;
	//~ cerr << "fine" << endl << endl;
}

int main(){
	cout.precision(10);
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		cout << "Case #" << i << ": ";
		test_case();
	}
	return 0;
}
