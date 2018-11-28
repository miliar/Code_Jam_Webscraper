#include <iostream>
#include<string>
using namespace std;

int main() {

	// your code goes here
	int t, j, k;
	string s;
	int count;
	int n;
	cin>>t;
	for(int i = 1;i<=t;++i){
		cin>>s>>n;
		count = 0;
		int len = s.length();
		for(j = 0;j<=len-n;++j){
			if(s[j] == '-'){
				++count;
				for(k = j;k<j+n;++k){
					if(s[k] == '-')
						s[k] = '+';
					else
						s[k] = '-';
				}
				//cout<<s<<endl;
			}
		}
		bool flag = true;
		for(j = 0;j<len;++j){
			if(s[j] == '-'){
				flag = false;
				break;
			}
		}
		cout<<"Case #"<<i<<": ";
		if(flag)
			cout<<count;
		else
			cout<<"IMPOSSIBLE";
		cout<<endl;
	}

	return 0;
}