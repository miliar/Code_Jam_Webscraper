#include <iostream>
using namespace std;


bool tidy (string s){
	for (int i=0; i<s.size()-1; i++){
		if (s[i]>s[i+1]) return false;
		}
	return true;
}

string substract (string s, int p){
	if (s[p]!='0') s[p]--;
	else {
		s[p]='9';
		s=substract(s,p-1);
	}
	return s;
}

int main(){
	int n;
	while (cin>>n){
		for(int i=1; i<=n; i++){
			string s;
			cin>>s;
			int r=0;
			
			while (not tidy(s)) 				s=substract(s, s.size()-1);
	for (int j=0; j<s.size() and r==0; j++){
	if (s[j]=='0') s.erase(s.begin());
	else r=1;
	}
	cout<<"Case #"<<i<<": "<<s<<endl;
}
}
}
	
