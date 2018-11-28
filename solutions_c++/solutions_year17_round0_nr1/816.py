#include<cstdio>
#include<cstring>

int t, k, ans;
bool fail;
char s[1005];

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &t);
	for(int cases=1;cases<=t;cases++){
		scanf("%s %d", s, &k);
		ans=0;
		fail=0;
		for(int i=0;i<strlen(s);i++){
			if(s[i]=='-'){
				if(i+k>strlen(s)){
					fail=1;
					break;
				}
				ans++;
				for(int j=i;j<i+k;j++){
					if(s[j]=='-') s[j]='+';
					else s[j]='-';
				}
			}
		}
		printf("Case #%d: ", cases);
		if(fail) puts("IMPOSSIBLE");
		else printf("%d\n", ans);
	}
}
