#include <bits/stdc++.h>

using namespace std;

int distanciaTotal;

// double masLento(vector<long long> &k, vector<long long> &s){
// 	int sz = k.size();

// 	for(int i=0 ; i<sz; i++){

// 	}
// }

double masLento(long long k, long long s){
	long long d = distanciaTotal - k;
	double tiempo = (double)d / (double)s;
	return tiempo;
}

int main(){

	int tc;
	scanf("%d",&tc);
	int ci = 1;
	while(tc--){
		long long d, n;
		cin >> d >> n;
		distanciaTotal = d;
		// vector<long long> k;
		// vector<long long> s;
		int kk, ss;
		double masTarde = 0;
		for(int i=0 ; i<n; i++){
			cin >> kk >> ss;
			// k.push_back(kk);
			// s.push_back(ss);
			// cout << kk << " " << ss <<endl;
			// cout << "Tiampo: " << masLento(kk,ss) << endl;
			masTarde = max(masTarde,masLento(kk,ss));
		}
		double res = (double)d / masTarde;
		// cout << "Res: " << res << endl;
		printf("Case #%d: %.6lf\n", ci++,res);
	}
}