#include <bits/stdc++.h>
using namespace std;
int main(){
	//ios::sync_with_stdio(false);
	int t;cin>>t;
	for(int i2=0;i2<t;i2++){
		 double d,n;cin>>d>>n;
		 double mi_time=1000000000;
		 double mi_rat=0;
		for(int i=0;i<n;i++){
			 double x,y;cin>>x>>y;
			 double tim=(d-x)/y;
			 double rat=x*tim;
			if(rat>mi_rat){
				mi_time=tim;
				mi_rat=rat;
			}
		}
		printf("Case #%ld\n: ",d/mi_time);
		//cout<<"Case #"<<i2+1<<": "<< d/mi_time<<endl;
	}
	return 0;
}