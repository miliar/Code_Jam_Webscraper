#include <iostream>
#include <string.h>
using namespace std;


void solve(int t){
	int n;
	char s[1005];
	cin>>s;
	n=strlen(s);
	for(int i=n-1;i>=1;i--){
		if(s[i]<s[i-1]){
			s[i-1]=max(int(s[i-1]-1),int(s[i]));
			for(int j=i;j<n;j++){
				s[j]='9';
			}
		}
	}
	cout<<"Case #"<<t<<": ";
	if(s[0]=='0')
	cout<<s+1<<endl;
	else
	cout<<s<<endl;
	
}

int main() {
	int t;
	cin>>t;
	for(int i=0;i<t;i++){
		solve(i+1);
	}
	return 0;
}