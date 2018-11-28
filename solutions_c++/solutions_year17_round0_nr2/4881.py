#include <iostream>
#include <cmath>
#include <bitset>
#include <sstream>
#include <string>
using namespace std;
int main(){

	string s;
	int a;
	cin>>a;
		int all=a;
	while(a){
		cin>>s;
		long long int n=s.size();

		long long int i=0;

		string res;
		for(i=0;i<n && i>=0;){
			if(i+1<n && s[i+1]<s[i]){
				s[i]--;
				long long int k=1;
				while(i+k<n) s[i+k++]='9';
				i--;
			}else{
				i++;
			}
		}
		auto j=s.begin();	
		//cout<<*j<<endl;	
		while(*j=='0'){
			s.erase(j);
		}

		cout << "Case #" << all-a+1 << ": " << s << endl;
		a--;
		
	}
	return 0;
}
