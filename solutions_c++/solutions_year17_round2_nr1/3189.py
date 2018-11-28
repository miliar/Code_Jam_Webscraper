#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<math.h>
#include<stdlib.h>
#include<stdio.h>
using namespace std;

double end_time(double K, double S, double D){
	return (D-K)/S;
}

int main(){
	long t,T,N;
	double K,S,Ki,Si;
	cin >> T;
	double D;
	
	
	for(t=1;t<=T;++t){
		cin >> D;
		cin >> N;
		double max_t=-1;
		for(long i=0;i<N;++i){
			cin >> K;
			cin >> S;
			double t = D*S/(D-K);
			if(max_t<-1E-6 || t-max_t < -1E-6){
				max_t = t;
			}
		}
		cout << "Case #"<<t<<": ";
		printf("%.6lf\n",max_t);
	}
}
