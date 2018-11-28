#include<bits/stdc++.h>
using namespace std;

void flip(char* s, int i){
	if(s[i] == '-')
		s[i] = '+';
	else
		s[i] = '-';
}

int main(){

	int t,r=1;
	cin>>t;
	while(r<=t){
		char s[1008]; int k;
		cin>>s>>k;
		int n = strlen(s);
		int i,j,ans = 0; bool flag = 1;
		for(i=0; i<=n-k; i++){
			if(s[i] == '-'){
				ans++;
				for(j=i; j<i+k; j++){
					flip(s,j);
				}
			}
		}
		for(i=n-k; i<n; i++){
			if(s[i] == '-'){
				flag = 0;
				break;
			}
		}
		if(flag)
			cout<<"Case #"<<r<<": "<<ans<<endl;
		else
			cout<<"Case #"<<r<<": IMPOSSIBLE"<<endl;
		r++;
	}
	return 0;
}
