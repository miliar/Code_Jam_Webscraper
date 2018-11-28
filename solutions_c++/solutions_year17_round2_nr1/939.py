#include "stdafx.h"
ll K[1000000],S[1000000];
int main() {
	ios_base::sync_with_stdio(0); cout.tie(NULL);
	int _cases; cin >> _cases;
	for (int _case = 1; _case <= _cases; _case++) {
		ll D, N; 
		cin >> D >> N;
		for (int i = 0; i < N; i++)
			cin >> K[i] >> S[i];

		double ans= 0;

		for (int i = 0; i < N; i++) {
			double arrival_time=double(D-K[i])/(double)S[i];//FIXME
			ans = max(ans, arrival_time);
		}


	
		cout << "Case #" << _case << ": " <<fixed<<setprecision(10)<< D/ans << endl;
	}

}

