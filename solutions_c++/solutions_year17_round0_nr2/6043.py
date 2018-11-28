#include <bits/stdc++.h>
using namespace std;

int main() {
	int t;
	string s;
	cin>>t;
	for(int k=1;k<=t;k++) {
		cin>>s;
		int flg=0,l=s.size(),i;
		for(i=0;i<l-1;i++) {
			if((s[i])>(s[i+1]))	{
				flg=1;
				break;
			}
		}if(flg){
		while(i>0 && (s[i])==(s[i-1])) {
			i--;
		}
		s[i]--;
		i++;
		for(;i<l;i++) {
			s[i]='9';
		}
		}
		printf("Case #%d: ",k);
		if(s[0]!='0')
		cout<<s[0];
		for(i=1;i<l;i++) cout<<s[i];
		cout<<endl;
	}
}