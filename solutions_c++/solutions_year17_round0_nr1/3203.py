#include <bits/stdc++.h>

using namespace std;

void solvre(){
	string s;
	int k;
	cin>>s>>k;
	int ans = 0;
	int tam = s.length()-k;
	for(int i = 0; i<=tam; i++){
		if(s[i]=='-'){
			ans++;
			for(int j = 0; j<k; j++){
				if(s[j+i]=='-') s[j+i] = '+';
				else s[j+i] = '-';
			}
		}
		// cout<<s<<endl;
	}
	for(int i = tam + 1; i<s.length(); i++){
		if(s[i]=='-'){
			printf("IMPOSSIBLE\n");
			return;
		}
	}
	printf("%d\n", ans);

}

int main(){
	int t;
	cin>>t;
	for(int i = 1; i<=t; i++){
		printf("Case #%d: ", i);
		solvre();
	}

}