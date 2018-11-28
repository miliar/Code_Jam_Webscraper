#include <iostream>
#include <iomanip>

using namespace std;

int main() {
	int i,j,T,N;
	double S,ans,cur;
	long D,K;
	cout<<fixed;
	cout<<setprecision(7);
	cin>>T;
	for(i=1;i<=T;i++) {
		cin>>D>>N;
		cin>>K>>S;
		ans = (D*S)/(D-K);
		for(j=1;j<N;j++) {
			cin>>K>>S;
			cur = (D*S)/(D-K);
			if(cur<ans) ans = cur;
		}
		cout<<"Case #"<<i<<": "<<ans<<"\n";
	}
	return 0;
}