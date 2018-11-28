#include <iostream>
#include <algorithm>
using namespace std;


int main(){
	ios::sync_with_stdio(0);
	int t;
	cin>>t;
	for(int ii=1; ii<=t; ++ii){
		string tmp, s;
		cin>>tmp;
		s="0";
		s+=tmp;
		cout<<"Case #"<<ii<<": ";
		unsigned wsk=0;
		bool ok=false;
		
		for(unsigned i=1; i<s.size(); ++i){
			if(ok){
				s[i]='9';
				continue;
			}
			if(s[i]>s[i-1]){
				wsk=i;
			}
			if(s[i]<s[i-1]){
				s[wsk]--;
				i=wsk;
				ok=true;
			}
		}
		s.erase(s.begin());
		if(s[0]<'1'){
			s.erase(s.begin());
		}
		cout<<s<<"\n";
	}
	
	return 0;
}

