#include<iostream>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++){
		string no;
		cin>>no;
		for(int i=0;i<no.length()-1;i++){
			if(no[i]>no[i+1]){
				no[i]--;
				for(int j=i+1;j<no.length();j++){
					no[j]='9';
				}
				i=-1;
			}
		}
		unsigned long long ans=0;
		for(int i=0;i<no.length();i++){
			ans*=10;
			ans+=(no[i]-'0');
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
	return 0;
}
