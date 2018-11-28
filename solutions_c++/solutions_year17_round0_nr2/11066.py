#include<bits/stdc++.h>
using namespace std;

int main(){
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;i++){
		long long int n,temp,ans;
		int dig,ct;
		cin>>n;
		while(n>0){
			temp=n;
			dig=10;
			ct=0;
			while(temp>0){
				if(temp%10<=dig)
					dig=temp%10;
				else{
					ct=1;
					break;				
				}
				temp/=10;			
			}
			if(temp==0){
				ans=n;
				break;
			}
			else if(ct==1)
				n--;
			
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
