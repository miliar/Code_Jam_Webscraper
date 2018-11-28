#include<bits/stdc++.h>
using namespace std;
typedef struct did{
	double x,s;
	double t;
}did;
int main(){
	long long T;
	cin >> T;
	for(long long t=1;t<=T;t++){
		long long d,n;
		cin >> d>>n;
		did a[n];
		long long max_ind=0;
		for(long long i=0;i<n;i++){
			cin >> a[i].x;
			cin >> a[i].s;
			a[i].t = (d-a[i].x)/a[i].s;
			if (a[i].t>a[max_ind].t)
				max_ind=i;
		}
		double my_speed = d/a[max_ind].t;
		printf("Case #%lld: %lf\n",t,my_speed);
	}
	return 0;
}
