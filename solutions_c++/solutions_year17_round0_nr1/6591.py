#include <cstdio>
#include <cstring>
int T, K;
char str[1005];
char flip(char ch){
	return ch=='-'?'+':'-';
}
int main(){
	int ca=0, i;
	scanf("%d", &T);
	while(T--){
		scanf(" %s %d", str, &K);
		// printf("%s %d\n", str, K);

		int len=strlen(str), ans=0;
		for(i=0;i<len;i++){
			if(str[i]=='-' && i+K<=len){
				for(int j=0; j<K; j++){
					str[i+j]=flip(str[i+j]);
				}
				// puts(str);
				ans++;
			}
		}
		for(i=0;i<len;i++){
			if(str[i]=='-')break;

		}
		printf("Case #%d: ", ++ca);
		if(i<len){
			puts("IMPOSSIBLE");
		}
		else{
			printf("%d\n", ans);
		}

	}

}