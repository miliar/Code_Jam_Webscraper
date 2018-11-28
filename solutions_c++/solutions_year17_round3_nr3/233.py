#include <bits/stdc++.h>

using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		cout << "Case #" << t << ": ";
		int N, K;
		cin >> N >> K;
		double niza[N];
		double units;
		cin >> units;
		priority_queue<double, vector<double>, greater<double>> q;
		for(int i=0; i<N; i++){
			cin >> niza[i];
			q.push(niza[i]);
		}

		while(units > 0.00001){
			double tmp = q.top();
			q.pop();
			tmp += 0.0001;
			q.push(tmp);
			units -= 0.0001;
		}
		double prod = 1.00000000000;
		while(!q.empty()){
			prod *= q.top();
			q.pop();
		}
		cout << setprecision(9) << fixed << prod << endl;
	}


	return 0;
}

