#include<bits/stdc++.h>
#define F first
#define S second
using namespace std;
bool is_tidy(long long n){
	int curr=9;
	while(n){
		if((n%10)>curr)
			return false;
		curr=n%10;
		n/=10;
	}
	return true;
}
int main(){
	int tt;
	cin>>tt;
	for(int t=1;t<=tt;t++){
		printf("Case #%d: ",t);
		long long n;
		cin>>n;
		while(n){
			if(is_tidy(n)){
				cout<<n<<endl;
				break;
			}
			else
				n--;
		}
	}
	return 0;
}