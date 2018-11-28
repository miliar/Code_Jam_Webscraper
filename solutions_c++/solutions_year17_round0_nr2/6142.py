#include<iostream>
using namespace std;
int main(){
	int long t,j,k,l;
	string s;
	cin>>t;
	for(l=1;l<=t;l++){
		cin>>s;
		for(j=s.size()-1;j>0;j--){
			if(s[j]<s[j-1]){
				s[j-1]--;
				for(k=j;k<s.size();k++){
					s[k]='9';
				}
			}
		}
		cout<<"Case #"<<l<<": ";
		for(j=0;j<s.size();j++){
			if(j==0){
				if(s[j]!='0')
				cout<<s[j];
			}
			else
			cout<<s[j];
		}
		cout<<endl;
	}
	
	return 0;
}
