#include <cstdio>

char s[1010];
int t,n,i,j,k,l,ans;

int main()
{
//	freopen("output.txt","w",stdout);

	scanf("%d",&n);

	for(t=1;t<=n;t++){
		scanf("%s%d",s,&k);
		for(ans=l=0;s[l]!='\0';l++);
		for(i=0;i<=l-k;i++){
			if(s[i] == '-'){
				for(j=0;j<k;j++) s[i+j] = '+'+'-'-s[i+j];
				ans++;
			}
		}
		for(i=l-k;i<l;i++) if(s[i] == '-') break;
		if(i<l) printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %d\n",t,ans);
	}
	return 0;
}