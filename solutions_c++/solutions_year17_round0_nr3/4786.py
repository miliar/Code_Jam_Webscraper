#include <iostream>
#include <math.h>
#include <string>
using namespace std;
struct Res{
	int y,z;
};
int main(){
	int t;
	cin>>t;
	int iter=t;
	Res* res= new Res[t];
	while(t--){
		long int n;
		cin>>n;
		long int k;
		cin>>k;
		if(k==n){
			res[t].y=0;
			res[t].z=0;
		}

		//else if(k>n/2) {
		//	res[t].z=0;
		//	res[t].y=0;
		//}
		else {
			long int i=log(k)/log(2);
			double temp= (n- pow(2,i)+1.0)/pow(2,i);
			long int min=temp;
			long int max;
			if(min==temp){
				max=min;
			}
			else {
				max=min+1;
			}
			float f= temp-min;
			long int rem=k-pow(2,i) +1;
			if(rem<=f*pow(2,i)){
				res[t].z=(max-1)/2;
				res[t].y=max-1-res[t].z;
			}
			else{
				res[t].z=(min-1)/2;
				res[t].y=min-1-res[t].z;	
			}
			
		}
		
	}
	int i=1;
	while (iter--){
		cout<<"Case #"<<i<<": "<<res[iter].y<<" "<<res[iter].z<<endl;
		i++;
	}
	delete[] res;
	return 0;
}

