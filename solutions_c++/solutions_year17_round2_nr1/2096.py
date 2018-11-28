#include<iostream>
using namespace std;

int main(){
	long T;
	cin>>T;
	for (int i=0;i<T;i++){
		long d,n;
		cin>>d>>n;
		double t=0;
		for(int j=0;j<n;j++){
			long k;
			double s;
			cin>>k>>s;
			double ti = ((d-k)/s);
			
			if (ti>t) t = ti;
		}
		double speed = d/t;
		cout<<std::fixed<<"Case #"<<i+1<<": "<<speed<<endl;
	}
}