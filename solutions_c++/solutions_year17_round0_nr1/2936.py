#include <bits/stdc++.h>

using namespace std;

int main(){
	int u,k,t,cont;
	string s;
	cin>>t;
	for(int i=0; i<t; i++){
		cin>>s>>k;
		cont=0;
		for(int j=0; j<s.size()-k+1; j++){
			if(s[j]=='-'){
				cont++;
				for(int l=0; l<k; l++){	
					if(s[j+l]=='-') {
						s[j+l]='+';
					}
					else s[j+l]='-';
				}
			}
		}
		bool b=true;
		for(int w=0; w<s.size(); w++) if(s[w]!='+') b=false;
		if(b) cout<<"Case #"<<i+1<<": "<<cont<<"\n";
		else cout<<"Case #"<<i+1<<": IMPOSSIBLE\n";
	}
	return 0;
}
