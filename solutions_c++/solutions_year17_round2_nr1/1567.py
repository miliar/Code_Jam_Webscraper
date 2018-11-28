#include <iostream>
#include <cmath>
using namespace std;
int main(){
	int t = 0;
	cin>>t;
	for(int l = 1; l <= t; l++){
		int n = 0, d = 0;
		cin>>d>>n;
		double time = 0;
		for(int i = 0; i < n; i++){
			double x, s;
			cin>>x>>s;
			double t1 = (d-x)/s;
			if(time < t1){
				time = t1;
			}
		}
		cout<<"Case #"<<l<<": ";
		printf("%.6f\n", (float)d/time);
	}
	return 0;
}