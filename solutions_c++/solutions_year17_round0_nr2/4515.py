#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin>>t;
	for (int cs=1; cs<=t; cs++){
		cout<<"Case #"<<cs<<": ";

		string s;
		cin>>s;
		int i1=-1, i2;
		for (int i=0; i<s.length()-1; i++){
			if (s[i]>s[i+1]){
				i1 = i;
				i2 = i+1;
				break;
			}
		}
		if (i1 >= 0){
			if (s[i1] == '1'){
				for (int i=0; i<s.length()-1; i++) cout<<"9";
			} else {
				while (s[i1] == s[i1-1] && i1>0){
					i1--; i2--;
				}
				s[i1]--;
				for (int i=i2; i<s.length(); i++) s[i] = '9';
				cout<<s;
			}
		} else {
			cout<<s;
		}
		

		cout<<endl;
	}
}