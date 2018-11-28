#include<iostream>
#include<string>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int x=1;x<=t;x++){
		cout<<"Case #"<<x<<": ";
		string s;
		//char c;
		int k;
		cin>>s>>k;
		int l = s.length();
		int a[l];
		for(int i=0;i<l;i++){
			a[i] = (s[i]=='+');
		}
		int pass = 0;
		for(int i=0;i<l-k+1;i++){
			if(a[i]==0){
				pass++;
				for(int j=0;j<k;j++){
					a[i+j] = (1-a[i+j]);
				}
			}
			
		}
		int sum = 0;
		for(int i=0;i<l;i++){
			sum+=a[i];
		}
		if(sum==l){
			cout<<pass;
		}else{
			cout<<"IMPOSSIBLE";
		}
		cout<<endl;
	}
}
