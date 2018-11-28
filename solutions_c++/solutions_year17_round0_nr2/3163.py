#include <bits/stdc++.h>

using namespace std;

void solvre(){
	string s;
	cin>>s;
	int inicio = 0;
	for(int g = 0; g<30; g++){
		inicio = 0;
		while(inicio<s.length() && s[inicio]=='0') inicio++;
		for(int i = inicio+1; i<s.length(); i++){
			if(s[i]<s[i-1]){
				s[i-1]--;
				for(int j = i; j<s.length(); j++){
					s[j] = '9';
				}
			}
		}
	}
	inicio = 0;
	while(inicio<s.length() && s[inicio]=='0') inicio++;
	if(inicio == s.length()){
		printf("0\n");
		return;
	}

	for(int i = inicio; i<s.length(); i++){
		printf("%c", s[i]);
	}
	printf("\n");
}

int main(){
	int t;
	cin>>t;
	for(int i = 1; i<=t; i++){
		printf("Case #%d: ", i);
		solvre();
	}

}