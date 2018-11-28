#include<iostream>
#include<sstream>
#include<cstring>
#include<algorithm>
using namespace std;

bool isTidy(unsigned long long n){

	ostringstream op_stream;
	op_stream<<n;
	string s= op_stream.str();
	int len= s.length();
	for(int i=0;i<len-1;i++)
		if(s[i]>s[i+1])
			return false;
	return true;
}
int main(){
	int t;
	cin>>t;
	for(int test=1;test<=t;test++){
		unsigned long long n;
		cin>>n;
		string result;
		for(unsigned long long tidy=n;tidy>=0;){
			if(isTidy(tidy)){
				reverse(result.begin(),result.end());
				cout<<"Case #"<<test<<": ";
				if(tidy!=0)
					cout<<tidy;
				cout<<result<<endl;
				break;
			}
			result+='9';
			tidy= tidy/10;
			tidy--;
		}
	}
	return 0;
}
