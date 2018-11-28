#include<bits/stdc++.h>

using namespace std;

int T, K;
char str[1005];

bool check(char x[]){
	int len = strlen(x);
	for(int i=len-K-1;i<len;i++){
		if (str[i] == '-'){
			return false;
		}
	}
	return true;
}

void reverse(char &x){
	if (x == '+') 
		x = '-';
	else 
		x = '+';
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int ans = 0;
		scanf("%s %d",str,&K);
		int len = strlen(str);
		for(int i=0;i<=len-K;i++){
			if (str[i] == '-'){
				for(int j=0;j<K;j++){
					reverse(str[i+j]);
				}
				ans++;
			}
		}
	//	puts(str);
		printf("Case #%d: ",t);
		if (check(str)){
			printf("%d\n",ans);
		} else {
			puts("IMPOSSIBLE");
		}
	}
	return 0;
}
