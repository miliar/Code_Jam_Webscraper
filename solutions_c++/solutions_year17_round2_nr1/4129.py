#include <iostream>

using namespace std;

int T;
double D;
int N;
double *K;
double *S;
double *time_;
double max_time;
double mySpeed;

int main() {
	cin>> T;
	
	for(int i=0 ; i<T ; i++){
		cin >> D;
		cin >> N;
		K = new double[N];
		S = new double[N];
		time_ = new double[N];
		max_time = -1;
		for(int j=0;j<N;j++){
			cin>> K[i];
			cin>> S[i];
			time_[j] = (D - K[i]) / S[i];
			if(max_time<time_[j])
				max_time = time_[j];
		}
		mySpeed = D / max_time;
		printf("Case #%d : %.6lf\n", i+1, mySpeed);
	}

	return 0;
}