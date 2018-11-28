#include <bits/stdc++.h>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int z=1;z<=t;z++){
		string s;
		cin >> s;
		int len=s.length();
		for(int i=len-2;i>=0;i--){
			if(s[i]>s[i+1]){
				s[i]-=1;
				for(int j=i+1;j<len;j++)
					s[j]='9';
			}
		}
		if(s[0]=='0'){
			cout << "Case #" << z << ": ";
			for(int i=1;i<len;i++)
				cout << s[i];
			cout << endl;
		}
		else{
			cout << "Case #" << z << ": " << s << endl;
		}
	}	
	return 0;
}