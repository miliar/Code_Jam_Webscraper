#include<bits/stdc++.h>

using namespace std;

int main(){
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	int t;
	cin>>t;
	
	for(int tc = 1;tc<=t;tc++){
		string s;
		cin>>s;
		for(int i = 0;i < (s.length() - 1);i++){
			if(s[i] > s[i+1]){
				int j = i;
				while(j>=0 && s[j] == s[i]){
					j--;
				}
				j++;
				s[j]--;
				j++;
				for(;j<s.length();j++){
					s[j] = '9';
				}
				break;
			}
		}
		while(s[0] == '0'){
			s = s.substr(1,s.length()-1);
		}
		cout<<"Case #"<<tc<<": "<<s<<"\n";
	}
	return 0;
}
