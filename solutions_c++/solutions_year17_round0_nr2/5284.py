#include<iostream>
#include<cmath>

typedef long long ll;

using namespace std;

int getIthDigit(ll N,int i){
	if(N/(pow(10,i-1))==0) return -1;
	return (ll)(fmodl(N,(pow(10,i)))/pow(10,i-1));
}

ll setIthDigit(ll N,int i, int newVal) {
	return (N + (ll)((newVal-getIthDigit(N,i))*pow(10,i-1)));
}

int main() {

	int T;
	cin>>T;

	ll N;
	for(int i=1;i<=T;i++) {
		cin>>N;

		int d=1;

		while(1) {
			if(getIthDigit(N,d+1)==-1)
				break;
			if(getIthDigit(N,d) < getIthDigit(N,d+1)) {
				for(int j=d;j>=1;j--) {
					N=setIthDigit(N,j,9);
				}
				N=setIthDigit(N,d+1,getIthDigit(N,d+1)-1);	
			}	
			d++;
		}
		cout<<"Case #"<<i<<": "<<N<<endl;
	}

}