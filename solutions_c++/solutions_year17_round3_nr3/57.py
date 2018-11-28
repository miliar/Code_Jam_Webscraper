#include<bits/stdc++.h>
using namespace std;


bool canmake(double goal, double U, vector<double> P){
	for(int i = 0; i < P.size(); i++){
		if(P[i] < goal){
			U -= goal - P[i];
		}
	}
	return U >= 0;
}


void solve(){
	long long N, K;
	double U;
	vector<double> P;
	cin >> N >> K;
	cin >> U;

	for(int i = 0; i < N; i++){
		double tmp;
		cin >> tmp;
		P.push_back(tmp);
	}
	sort(P.begin(), P.end());

	double start = 0;
	double end = 1;

	while(start + 0.000000001 < end){
		double mid = (start + end)/2;
		if(canmake(mid, U, P)){
			start = mid;
		}else{
			end = mid;
		}
	}

	double ans = 1;
	for(int i = 0; i < P.size(); i++){
		ans *= max(start, P[i]);
	}
	printf("%.10f\n", ans);
}


int main(){
	long long T;
	cin >> T;
	for(int i = 0; i < T; i++){
		cout << "Case #" << i + 1 << ":" << " ";
		solve();
	}
}

