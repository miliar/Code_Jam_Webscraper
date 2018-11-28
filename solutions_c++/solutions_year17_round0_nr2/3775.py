#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

char lim[111];
char a[111];
int len,n;

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&n);
	for(int T=1;T<=n;++T){
		scanf(" ");
		scanf("%s",&lim);
		printf("Case #%d: ",T);
		len = strlen(lim);
		int po = 0;
		char cmax = '0';
		while (po<len && lim[po] >= cmax){
			cmax = max(cmax, lim[po]);
			po++;
		}
		if	(po == 0 && lim[po]=='1'){
			for	(int i=0; i+1 < len;++i)
				putchar('9');
			printf("\n");
			continue;
		}
		if	(po == len){
			for	(int i=0; i<len;++i)
				putchar(lim[i]);
			printf("\n");
			continue; 
		}
		for (int i = po;i<len;++i)	lim[i]='9';
		lim[--po]--;
		while (po && lim[po-1]>lim[po]){
			lim[--po]--;
		}
		if	(po == 0 && lim[po] == '0'){
			for	(int i=0; i+1 < len;++i)
				putchar('9');
			printf("\n");
			continue;
		}
		for	(int i=0;i<=po;++i)
			putchar(lim[i]);
		for (int i = po + 1; i<len;++i)
			putchar('9');
		printf("\n");
	}
}
