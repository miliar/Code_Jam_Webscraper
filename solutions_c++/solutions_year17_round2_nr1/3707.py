#include<iostream>
#include<cstdio>
using namespace std;

int main(){
	
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int d,n;
		cin>>d>>n;
		long a[n][2];
		for(int j=0;j<n;j++){
			cin>>a[j][0]>>a[j][1];
		}
		long temp;
		for(int j=0;j<n;j++){
			for(int k=0;k<n-j-1;j++){
				if(a[k][0]<a[k+1][0]){
					temp = a[k][0];
					a[k][0] = a[k+1][0];
					a[k+1][0]=temp;
					temp = a[k][1];
					a[k][1] = a[k+1][1];
					a[k+1][1]=temp;
				}
			}
		}
		long double maxt=(long double)(d-a[0][0])/a[0][1],newt;
		
		for(int j=1;j<n;j++){
			if(a[j][1]*maxt+a[j][0]<d){
				maxt = (long double)(d-a[j][0])/a[j][1];
			}
		}
		//cout<<maxt<<" "<<d<<"\n";
		long double ans = d/maxt;
		printf("Case #%d: %.6Lf\n",i,ans);
		//cout<<"Case #"<<i<<": "<<(double)(d/maxt)<<"\n";
	}
	return 0;
}
