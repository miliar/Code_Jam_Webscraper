#include<bits/stdc++.h>
using namespace std;
#define lli long long int

int main(){	
	lli i,t;
	cin>>t;
	for(i=1;i<=t;i++){
		lli n,j;
		long double k,m,ans=(LLONG_MAX),s,d;
		cin>>d>>n;
		for(j=1;j<=n;j++){
			cin>>k>>s;
			long double a=d-k;
			long double time=a/s;
			m=d/time;
			if(m<ans){
				ans=m;
			}
		}
		printf("Case #%lld: %.6Lf\n",i,ans);
	}
	return 0;
}