#include <iostream>
using namespace std;

#define ll long long

bool check(ll n){
	int arr[100];
	int i=0;
	while(n>0){
		arr[i]=n%10;
		n/=10;
		i++;
	}
	for(int j=0;j<i-1;j++){
		if(arr[j]<arr[j+1]){
			return false;
		}
	}
	return true;
}

int main(){
	int Te;
	cin>>Te;
	for(int te=1;te<=Te;te++){
		ll N;
		cin>>N;

		// int res=1;
		// for(int n=1;n<=N;n++){
		// 	if(check(n)){
		// 		res=n;
		// 	}
		// }
		// cout<<"Case #"<<te<<": "<<res<<endl;
		// continue;

		int arr[100];
		int n=0;
		ll tmp=N;
		while(tmp>0){
			arr[n]=tmp%10;
			n++;
			tmp/=10;
		}

		for(int i=n-1;i>=0;i--){
			int fl=1;
			for(int j=i;j>=0;j--){
				if(arr[j]>arr[i]){
					break;
				}
				if(arr[j]<arr[i]){
					fl=0;
					break;
				}
			}
			if(fl==0){
				arr[i]--;
				for(int j=i-1;j>=0;j--){
					arr[j]=9;
				}
				break;
			}
		}
		ll ans=arr[0];
		ll f=1;
		for(int i=1;i<n;i++){
			f*=10;
			ans+=arr[i]*f;
			
		}
		cout<<"Case #"<<te<<": "<<ans<<endl;
	}
	return 0;
}