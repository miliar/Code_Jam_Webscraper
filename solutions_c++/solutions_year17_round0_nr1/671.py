#include <stdio.h>
#include <cstring>

char str[1010];
int n,k;
int main() {
	int test;
	scanf("%d", &test);
	for(int tc=1;tc<=test;tc++) {
		scanf("%s %d",str, &k);
		n=strlen(str);

		int cnt=0;
		for(int i=0;i<=n-k;i++) {
			if(str[i]=='-') {
				for(int j=i;j<i+k;j++){
					if(str[j]=='-') str[j]='+';
					else str[j]='-';
				}
				cnt++;
			}
		}

		bool flag=false;
		for(int i=0;i<n;i++){
			if(str[i]=='-') {
				flag=true;
				break;
			}
		}

		printf("Case #%d: ",tc);
		if(flag) printf("IMPOSSIBLE\n");
		else printf("%d\n",cnt);
	}
	return 0;
}