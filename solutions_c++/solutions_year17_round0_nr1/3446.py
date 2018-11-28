#include<cstdio>
#include<cstring>
bool ok;
int K, ans;
char S[1005];
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	
	int T, len;
	scanf("%d",&T);
	for(int cases=1; cases<=T; cases++){
		printf("Case #%d: ",cases);
		ans = 0; ok = 1;
		scanf("%s %d",S, &K);
		len = strlen(S);
		for(int i=0; i+K-1<len; i++){
			if(S[i] == '+') continue;
			for(int j=i; j<i+K; j++){
				if(S[j] == '-') S[j]='+';
				else S[j]='-';
			}
			ans++;
		}
		for(int i=len-K+1; i<len; i++){
			if(S[i]=='-'){
				ok = 0; break;
			}
		}
		if(ok) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}
