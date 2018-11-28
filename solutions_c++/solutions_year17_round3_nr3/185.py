#include <algorithm>
#include <iostream>
#include <iomanip>
#include <utility>
#include <string>
#include <vector>

using namespace std;

int main(){
	int cases;
	cin>>cases;

	for (int cas=1; cas<=cases; ++cas){
		cout << "Case #"<<cas << ": ";

		int N,K;
		cin>>N>>K;

		vector <double> P;

		double U;
		cin>>U;

		for (int i=0;i<N;++i){
			double tmp;
			cin>>tmp;
			P.push_back(tmp);
		}

		P.push_back(1.0);


		sort(P.begin(), P.end());

		for (int i=0; i<N;++i) {
			if ((P[i+1]-P[i])*(double)(i+1)<=U){
				U-=(P[i+1]-P[i])*(double)(i+1);
				for(int j=0;j<=i;++j){
					P[j]=P[i+1];
				}
			}else{
				for(int j=0;j<=i;++j){
					P[j]+=U/(double)(i+1);
				}
				U=0;
				break;
			}
		}

		double ret = 1.0;

		for(int i=0;i<N;++i) {
			ret *= P[i];
		}

		cout << setprecision(12) << (double)ret << endl;



	}
}

