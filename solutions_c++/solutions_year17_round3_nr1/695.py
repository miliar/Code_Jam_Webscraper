#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long llu;

double solve(){
	llu N,K;
	scanf("%llu %llu\n",&N,&K);
	vector<pair<double,double>> R(N);
	for(llu i=0;i<N;i++){
		float r,h;
		scanf("%f %f\n",&r,&h);
		//cout<< "R: "<<r<< " H: "<<h<<endl;
		R[i].second  = r;
		R[i].first = h*r*2.0*M_PI;
	}
sort(R.begin(),R.end());
	double max_area = 0;
double area=0;
	for(llu i=0;i<N;i++){
		// pick ith as base
		area = R[i].second * R[i].second * M_PI + R[i].first;
		//cout << "Picking with radius: "<< R[i].second<<endl;
		int k = 1;
		for(int j=N-1;j>=0 && k<K;j--){
			//cout << "At :" <<j<< "With :"<<R[j].first<<endl;
			if(i != j && R[j].second <= R[i].second){
				area += R[j].first;
				//cout << "Adding with radius: "<< R[j].second<<endl;
				k++;
			}
		}
		//cout << "Area: "<<area<<endl;
		if(area > max_area)max_area = area;
	}
	return max_area;
}

int main() {
    int T;
    scanf("%d\n",&T);
    for(int i=1;i<=T;i++){
        printf("Case #%d: %.10f\n",i,solve());
    }
    return 0;
}
