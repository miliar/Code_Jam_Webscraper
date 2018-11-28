#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

int T, k;
char s[11111];

int main(){
	scanf("%d\n", &T);
	for(int c=1; c<=T; c++){
		scanf("%s %d\n", s, &k);
		int n = strlen(s), ans=0;
		for(int i=0; i<=n-k; i++){
			if(s[i]=='-'){
				for(int j=i; j<i+k; j++){
					s[j] = ((s[j]=='+')?'-':'+');
				}
				ans++;
			}
		}
		bool imp = false;
		for(int i=0; i<n; i++){
			if(s[i]=='-'){
				imp = true;
			}
		}
		printf("Case #%d: ", c);
		if(imp){
			printf("IMPOSSIBLE\n");
		}
		else{
			printf("%d\n", ans);
		}
	}
	return 0;
}
