#include <iostream>
#include <string>
using namespace std;
int t;
int main() {
	cin>>t;
	for (int test = 1; test <= t; test++){
		string s;
		int len, k, result = 0;
		bool flag = true;
		cin>>s;
		len = s.length();
		cin>>k;
		for(int i=0;i<len;i++){
			if(s[i] == '-' && i+k-1 < len){
				result++;
				for(int j=i;j<i+k;j++)
					s[j] = s[j] == '-'?'+':'-';
			}
		}
		for(int i=0;i<len;i++)
			if(s[i] == '-')
				flag = false;
		cout<<"Case #"<<test<<": ";
		if(flag)
			cout<<result<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}
	return 0;
}