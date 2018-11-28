#include <iostream>
#include <string>

using namespace std;

int main(){
	int T;
	cin>> T;
	for(int t=1;t<=T;t++){
		string N;
		char a[20]={0,};
		cin>>N;
		a[N.length()-1]=N[N.length()-1];
		for(int i=N.length()-1;i>0;i--){
			a[i-1]=N[i-1];
			if(a[i]<a[i-1]){
				for(int j=N.length()-1;j>=i;j--){
					a[j]='9';
				}
				a[i-1]--;
			}
		}
		long long int ans=0;
		for(int i=0;i<N.length();i++){
				ans=ans*10+a[i]-'0';
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}
		
