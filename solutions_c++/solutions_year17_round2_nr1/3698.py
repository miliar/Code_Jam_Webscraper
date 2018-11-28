#include<iostream>
using namespace std;
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tc,j=1;
	cin>>tc;
	while(j<=tc){
		double D,N,time,x;
		
		
		cin>>D>>N;
		double ans=0;
		for(double  i=0;i<N;++i){
			double  K,S;
			cin>>K>>S;
			x = D-K;
			time = x/S;
			ans = max(ans,time);
		}
		double p = D/ans;
		printf("Case #%d: %.6lf\n",j,p);
		j++;
	}
	fclose(stdout);
	return 0;
}
