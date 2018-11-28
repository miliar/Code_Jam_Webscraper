#include <iostream>
#include <cstdio>

using namespace std;

int main(){
	double d;
	double k[1000], s[1000];

	int i, j, t, n;

	double min, mink, mins;

	double treq, velo, time, maxtime;

	cin>>t;

	for(i = 0; i < t; i++){

		for(j = 0; j < 1000; j++){
			k[j] = 0.0;
			s[j] = 0.0;
		}

		cin>>d>>n;
		for(j = 0; j < n; j++){
			cin>>k[j]>>s[j];
		}

		maxtime = 0.0;
		time = 0.0;
		for(j = 0; j < n; j++){
			
			time =(double) ((d -k[j]) / s[j]);
			
			if(time >= maxtime){
				maxtime = time;
			}
		}

		velo = d / maxtime;

		printf("Case #%d: %f\n", i + 1, velo);
	}

	return 0;
}