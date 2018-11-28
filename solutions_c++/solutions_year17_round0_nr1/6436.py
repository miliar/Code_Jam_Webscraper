#include <iostream>
#include <algorithm>
using namespace std;

char odwrot(char x){
	if(x=='+')
		return '-';
	return '+';
}

int main(){
	ios::sync_with_stdio(0);
	int t;
	cin>>t;
	for(int ii=1; ii<=t; ++ii){
		string s;
		int k, wyn=0;
		cin>>s>>k;
		cout<<"Case #"<<ii<<": ";
		for(unsigned i=0; i<=s.size()-k; i++){
			if(s[i]=='-'){
				wyn++;
				for(unsigned j=i; j<i+k; j++){
					s[j]=odwrot(s[j]);
				}
			}
		}
		bool ok=true;
		for(auto it=s.begin(); it!=s.end(); ++it){
			if(*it=='-'){
				ok=false;
				break;
			}
		}
		if(ok==false)
			cout<<"IMPOSSIBLE\n";
		else
			cout<<wyn<<"\n";
	}
	
	return 0;
}
