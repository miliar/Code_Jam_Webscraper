#include <iostream>
#include <cstdio>
using namespace std;

#define ll long long

int main(){
	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++){
		double D;
		ll N;
		cin>>D>>N;
		double t=-1;
		for(int i=0;i<N;i++){
			double k,s;
			cin>>k>>s;
			t=max(t,(D-k)/s);
		}
		double ans=(D*1.0)/t;
		printf("Case #%d: %10f\n",te,ans);
//		cout<<"Case #"<<te<<": "<<ans<<endl;
	}
	return 0;
}