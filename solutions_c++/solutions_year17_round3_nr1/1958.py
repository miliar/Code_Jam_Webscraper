#include <bits/stdc++.h>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;
const double EPS = 1e-50;

int cmp(double a, double b = 0.0){
	if(fabs(a-b) < EPS) return 0;
	return a > b ? 1 : -1;
}

int n, k;
vector < pair < double, double > > vet;
int used[100000], vis = 1;
vector < vector < pair < double, int > > > grafo;

double solve( int at, int qt ){
	if( qt+1 >= k ) return (vet[at].first*vet[at].first*acos(-1)); 

	double ans = -1152921504606846976.;

	for(int i = 0; i < grafo[at].size(); i++){
		if( used[grafo[at][i].second] == vis ) continue;
		used[grafo[at][i].second] = vis;
		ans = max(ans, solve(grafo[at][i].second, qt+1) + (grafo[at][i].first));
		used[grafo[at][i].second] = 0;
	}

	return ans;
}

int main(){
	ios::sync_with_stdio(false);
	int t;

	cin >> t;

	for(int w = 1; w <= t; w++){
		cin >> n >> k;

		vet.clear();
		vet.resize(n);
		vis++;

		vector < pair < double, pair < int, int > > > resp;
		vector < pair < double, int > > us;
		for(int i = 0; i < n; i++){
			cin >> vet[i].first >> vet[i].second;
		}

		sort(vet.begin(), vet.end());
		reverse(vet.begin(), vet.end());
		double ans = 0.;
		if( k == 1 ){
			for(int i = 0; i < n ;i++){
				ans = max(ans, (2.*vet[i].first*acos(-1)*vet[i].second) + (vet[i].first*vet[i].first*acos(-1)) );
			}
		}
		else{
			for(int i = 0; i < n; i++){
				vector < pair < double, int > > opa;
				for(int j = i+1; j < n; j++){
					opa.push_back(make_pair( (2.*vet[j].first*acos(-1)*vet[j].second), j) );
				}
				sort(opa.begin(), opa.end());
				reverse(opa.begin(), opa.end());
				if( opa.size()+1 >= k ){
					double acm = (vet[i].first*vet[i].first*acos(-1));
					acm += (2.*vet[i].first*acos(-1)*vet[i].second);
					for(int j = 0; j < k-1; j++){
						acm += (2.*vet[opa[j].second].first*acos(-1)*vet[opa[j].second].second);
					}
					ans = max(ans, acm);
				}
			}
		}

		cout << "Case #" << w << ": " << fixed << setprecision(8) << ans << endl;
		
	}

	return 0;
}