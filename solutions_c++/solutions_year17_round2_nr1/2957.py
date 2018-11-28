#include "bits/stdc++.h"
using namespace std;

int main() {
	int t;
	cin>>t;
	int e=1;
	while(t--){
		double d,n;
		cin>>d>>n;
		double max_time=-1;
		for(int i=0;i<n;i++){
			double k,si;
			cin>>k>>si;
			if(((d-k)/si)>=max_time) max_time=(d-k)/si;
		}
		printf("Case #%d: %.6lf\n",e++,d/max_time);
	}
	// your code goes here
	return 0;
}
