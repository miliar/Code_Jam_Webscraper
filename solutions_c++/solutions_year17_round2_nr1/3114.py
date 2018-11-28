#include<iostream>
using namespace std;
int main(){
	int tcs; cin>>tcs;
	for(int tc = 1; tc <= tcs; tc++){
		double d,n; cin>>d>>n;
		double max = 0;
		for(int i = 0; i <n; i++){
			double di,s;
			cin>>di>>s;
			double t = (d-di)/s;
			if(max < t) max = t;
		}
		cout<<"Case #"<<tc<<": ";
		printf("%0.6lf\n",(double)d/max);	}
}
