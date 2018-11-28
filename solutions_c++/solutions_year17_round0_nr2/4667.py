#include <bits/stdc++.h>
using namespace std;
int main(void){
	int t;
	cin>>t;
	for(int l = 1;l<=t;l++){
		string s;
		cin>>s;
		for(int i=0;i<s.size()-1;i++){
			if(s[i+1] < s[i]){

				int j;
				for(j=i+1;j<s.size();j++)
					s[j] = '9';

				j = i;
				while(j>0 && s[j-1] == s[j]){
					s[j] = '9';
					j--;
				}
				s[j]--;
				break;

			}
		}
		cout<<"Case #"<<l<<": ";
		int i=0;
		while(i<s.size() && (s[i] == '0'))
			i++;
		for(int j=i;j<s.size();j++)
			cout<<s[j];
		cout<<"\n";
	}
}