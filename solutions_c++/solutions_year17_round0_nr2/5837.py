#include<bits/stdc++.h>
using namespace std;

int main(){

	int t,r=1;
	cin>>t;
	while(r<=t){
		char s[20];
		cin>>s; int n = strlen(s);
		bool flag = 0; int i;
		for(i=0; i<n-1; i++){
			if(s[i] > s[i+1]){
				flag = 1;
				break;
			}
		}
		if(flag){
			while(i>0){
				if(s[i] != s[i-1])
					break;
				i--;
			}
			s[i] = s[i] - 1;
			if(s[i] == '0'){
				i--;
				s[n-1] = '\0';
			}
			for(i++; s[i]!='\0'; i++){
				s[i] = '9';
			}
		}
		cout<<"Case #"<<r<<": "<<s<<endl;
		r++;
	}
	return 0;
}
