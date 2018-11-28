#include<iostream>
using namespace std;


int main(){
	int t;
	cin>>t;
	for(int m=1;m<=t;m++){
	string s;
	int k;
	cin>>s>>k;
	int c =0;
	bool flag = true;
	for(int i=0;i<s.length();i++){
		if(s[i] == '-'){
			if(i+k-1>=s.length()){
				cout<<"Case #"<<m<<": "<<"IMPOSSIBLE"<<endl;
				flag = false;
				break;
			}
			for(int j=i;j<i+k;j++){
				if(s[j] == '-')
					s[j] = '+';
				else
					s[j] = '-';
			}
			c++;
		}
	}
	if(flag)
		cout<<"Case #"<<m<<": "<<c<<endl;
}
}
			
				
