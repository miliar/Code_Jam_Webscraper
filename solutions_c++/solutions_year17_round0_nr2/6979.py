#include <iostream>
#include <cstring>

using namespace std;

char s[30];
char x[30];

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;i++){
		scanf("%s", s+1);

		int n = strlen(s+1);
		for(int i=n-1;i>=1;i--){
			if(s[i] > s[i+1]){
				s[i]--;
				for(int j=i+1;j<=n;j++) s[j] = '9';
			}
		}

		int a = 0;
		int j = 0;
		for(int i=1;i<=n;i++){
			if(!a && s[i] != '0') a=1;
			if(a) x[j++] = s[i];
		}
		x[j]='\0';
		printf("Case #%d: %s\n", i, x);
	}
}