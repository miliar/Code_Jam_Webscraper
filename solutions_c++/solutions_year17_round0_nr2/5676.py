#include<iostream>
#include<cstring>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		long long n;
		cin>>n;
		int len=0;
		long long x=n;
		while(x){
			x/=10;
			len++;
		}
		short a[len+1];
		x=n;
		int j=0;
		while(x){
			a[j]=x%10;
			x/=10;
			j++;
		}
		j=0;
		for(int k=0;k<len;k++){
			for(j=len-1;j>0;j--){
				if(a[j]>a[j-1]){
					a[j]--;
					j--;
					for(;j>=0;j--){
						a[j]=9;
					}
					break;
				}
			}
			j=len;
		}
		long long ans=0;
		for(int j=len-1;j>=0;j--){
			ans*=10;
			ans+=a[j];
		}
		cout<<"Case #"<<i<<": "<<ans<<"\n";
	}
}
