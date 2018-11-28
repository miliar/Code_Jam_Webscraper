#include<cstdio>
#include<iostream>

using namespace std;

double D;
int T,N;
double K;
double S;
double maxx,x;

int main() {
	cin >> T;
	for(int ncase=1; ncase<=T; ncase++) {
		maxx=0;
		cin >> D >> N;
		for(int i=0; i<N; i++) {
			cin >> K >> S;
			x=(D-K)/S;
			if(maxx<x) maxx=x;
		}
		cout << "Case #" << ncase << ": ";
		printf("%.6f\n", D/maxx);
	}
	
	return 0;
}
