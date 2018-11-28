#include <iostream>

using namespace std;



int main(){
	int t;
	long long n,k;
	cin>>t;
	for(int i =1; i <= t; i++) {
		cin>>n>>k;
		while(k != 1){
			if(k & 1) {
				n = n - 1 -n/2;
			}
			else {
				n = n/2;
			}
			k=k/2;
		}
		long long ans1 = max(n/2, n-1-n/2);
		long long ans2 = min(n/2, n-1-n/2);
		cout<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<endl;
	}
}