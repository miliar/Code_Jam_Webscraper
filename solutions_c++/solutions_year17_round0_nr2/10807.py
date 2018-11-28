#include<iostream>
using namespace std;

int main(){
	int t;
	cin>>t;
	int x=t;
	while(t--){
		int n;
		cin>>n;
		if(n==1000){
			cout<<"Case #"<<x-t<<": 999"<<endl;
		}
		else{
			int a[]={0,0,0};
			for(int i=2;i>=0;i--){
				a[i]=n%10;
				n=n/10;
			}
			if(a[2]<a[1]){
				if(a[0]>=a[1]){
					a[0]--;
					a[1]=9;
					a[2]=9;
				}else{
					a[1]--;
					a[2]=9;
				}
			}else{
				if(a[0]>a[1]){
					a[0]--;
					a[1]=9;
					a[2]=9;
				}
			}
			cout<<"Case #"<<x-t<<": "<<100*a[0]+10*a[1]+1*a[2]<<endl;
		}
	}
	return 0;
}