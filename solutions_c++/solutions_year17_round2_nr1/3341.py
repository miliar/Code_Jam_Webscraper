	#include <iostream>
#include <cstdio>
#include <iomanip>
#include <algorithm>
using namespace std;
double work() {
	double d;
	int n;
	cin>>d>>n;
	double start, speed;
	double  mat=-1;
	for(int i = 0; i <n; i++) {
		cin>>start>>speed;
		double t = (d-start)/speed;
		if(t > mat ) mat = t;
	}
	return d/mat;
}

int main() {
	int t;
	cin>>t;
	int i = 1;
	while(t--){ 
		printf("Case #%d: %.6lf\n", i, work());
		i++;
	}
}