#include<cstdio>
#include<cstring>

int t;
char n[20];

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &t);
	for(int cases=1;cases<=t;cases++){
		scanf("%s", n);
		for(int i=0;i<20;i++){
			for(int j=0;j<strlen(n)-1;j++){
				if(n[j]>n[j+1]){
					n[j]--;
					for(int k=j+1;k<strlen(n);k++) n[k]='9';
					break;
				}
			}
		}
		printf("Case #%d: ", cases);
		int i;
		for(i=0;i<strlen(n);i++) if(n[i]!='0') break;
		for(;i<strlen(n);i++) printf("%c", n[i]);
		puts("");
	}
}
