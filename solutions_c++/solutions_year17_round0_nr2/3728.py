#include <iostream>
#include <cstring>

using namespace std;
int main(){
	int i,test,j,k;
	string s;
	cin>>test;
	k=1;
	while(test--){
		cin>>s;
		for(i=s.size()-1;i>0;i--){
			if(int(s[i]) < int(s[i-1])){
				for(j=i;j<s.size();j++){
					s[j] = '9';
				}
				s[i-1] = char(int(s[i-1]) - 1);
			}
		}
		i = 0 ;
		while(s[i]=='0')i++;
		cout<<"Case #"<<k<<": ";
		for(;i<s.size();i++)cout<<s[i];
		cout<<endl;
		k++;
	}
	return 0;
}