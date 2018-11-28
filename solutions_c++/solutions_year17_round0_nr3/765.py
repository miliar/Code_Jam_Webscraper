#include <iostream>
using namespace std;
int T;long long n,k,l,r,t,z,dd;
int main(){
	int ca=0;
	for(cin>>T;T;T--){
		cin>>n>>k;
		for(l=1,r=n;l<r;){
			t=(l+r+1)/2;
			for(z=1;n/t >= z;z*=2);z/=2;
			dd = z + min(n - t * z , z - 1);
			if(dd>=k)l=t;else r=t-1;
		}
		cout<<"Case #"<< ++ca << ": " << r/2 << ' ' << (r-1)/2 << endl;		
	}
}