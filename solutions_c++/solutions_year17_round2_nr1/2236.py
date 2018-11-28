
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


int main(){
	int T;
	cin >> T;

	for(int tsc=0; tsc<T; tsc++){
		int N,D;
		cin >> D >> N;
		vector<int> K,S;
		for(int i=0; i<N; i++){
			int k,s;
			cin >> k >> s;
			K.push_back(k);
			S.push_back(s);
		}

		double T = (double)(D - K.back()) / S.back();
		K.pop_back();
		S.pop_back();

		while(!K.empty()){
			T = max(T,(double)(D - K.back()) / S.back());
			K.pop_back();
			S.pop_back();
		}

		cout.precision(17);

		cout << fixed <<  "Case #"<<tsc+1<<": "<< D / T << endl;
	}
}
