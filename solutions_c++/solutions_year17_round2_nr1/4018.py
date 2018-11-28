#include <iostream>
#include <cstdlib>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <cmath>
#include <iomanip>
using namespace std;

#define MAX_HORSES 1500

double S[MAX_HORSES];
double K[MAX_HORSES];
double T[MAX_HORSES];


int main() {
	ios_base::sync_with_stdio(0);

	int T;
	cin>>T;

	for(int tt=1; tt<=T; tt++) {

		int D, N;
		cin>>D>>N;

		S[N] = 0;
		K[N] = D;

		for(int i=0; i<N; i++) {
			cin>>K[i]>>S[i];
		}

		double time = 0;
		if(N == 1) {
			time = (K[N] - K[N-1])/(S[N-1]);
		} else {
			int i = 0;

			//cout<<" "<<K[i+1]<<" "<<K[i]<<endl;
			if(K[i+1] < K[i]) {
				swap(K[i+1], K[i]);
				swap(S[i+1], S[i]);
				//cout<<" "<<K[i+1]<<" "<<K[i]<<endl;
			}

			double t = fabs(K[i] - K[i+1])/(S[i] - S[i+1]);
			//czy pierwszy dogoni 2
			if(t > 0) {
				double d = K[i] + S[i]*t;
				if(d <= D) {
					time += t;
					K[i+1] += S[i+1]*t;
					time += (K[i+2]-K[i+1])/S[i+1]; 
				} else {
					//cout<<"HI"<<endl;
					time += abs(K[i+2] - K[i])/(S[i]);
				}	
			} else {
				time += abs(K[i+2] - K[i])/(S[i]);
			}
		}


		double res = (double) D / time;

		// for(int i=0; i<N; i++) {
		// 	double t = abs(K[i] - K[i+1])/(S[i] - S[i+1]);
		// 	T[i] = t;
		// }

		// double time = 0;
		// int m = 0;

		// for(int i=0; i<N; i++) {
		// 	if(T[i] < T[m])
		// 		m = i;
		// }

		;
		cout<<"Case #"<<tt<<": "<< setprecision (6) << fixed <<res<<endl;

	}
	return 0;
}