#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
typedef long long ll;
int main(){
	int T;	cin>>T;
	for(int t=1;t<=T;t++){
		cout<<"Case #"<<t<<": ";
		ll n;	cin>>n;
		string s="";
		while(n){
			s=to_string(n%10)+s;
			n/=10;
		}
		n=s.size();
		if(n==1){
			cout<<s<<endl;
			continue;
		}
		while(true){
			char c=0;
			bool end=true;
			for(int i=0;i<n;i++){
				if(s[i]<c){
					end=false;
					break;
				}
				c=s[i];
			}
			if(end)	break;
			for(int i=1;i<n;i++){
				if(s[i-1]>s[i]){
					int pos=i-1;
					while(s[pos]=='0')	pos--;
					s[pos++]--;
					while(pos<n)	s[pos++]='9';
				}
			}
		}
		while(s[0]=='0')	s.erase(s.begin());
		cout<<s<<endl;
	}
}