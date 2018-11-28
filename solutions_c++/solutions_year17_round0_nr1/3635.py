#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
		int c=0;
		string s;
		cin>>s;
		int k;
		cin>>k;
		for(int j=0;j<s.length()-k+1;j++){
			if(s[j]=='+')continue;
			for(int l=j;l<j+k;l++){
				if(s[l]=='-')s[l]='+';
				else s[l]='-';
			}
			c++;
		}
		cout<<"Case #"<<i<<": ";
		for(int j=s.length()-k;j<s.length();j++){
			if(s[j]=='-'){
				c=-1;
				// cout<<"IMPOSSIBLE";
				break;
			}
		}
		if(c>=0)cout<<c;
		else cout<<"IMPOSSIBLE";
		cout<<endl;
	}
}