#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
	int t;
	scanf("%d",&t);
	for(int m=1;m<=t;m++){
		unsigned long long int n;
		scanf("%llu",&n);
		if(n<10){
			cout<<"Case #"<<m<<": "<<n<<endl;
		}
		else{
			stringstream ss;
			ss << n;
			string str = ss.str();
			//cout<<str<<endl;
			for(int i=str.length()-2;i>=0;i--){
				if(str[i]>str[i+1]){
					str[i]=str[i]-1;
					for(int j=i+1;j<str.length();j++)str[j]='9';
				}			
			}
			//cout<<str<<endl;
			unsigned long long int ans=0,mul=1;
			for(int i=str.length()-1;i>=0;i--){
				ans=ans+(mul*(str[i]-'0'));
				mul*=10;
			}
			cout<<"Case #"<<m<<": "<<ans<<endl;
		}
		
	}
	return 0;
}