#include <bits/stdc++.h>

char st[2000];


int main(){
	int tc=1,t,k;
	scanf("%d%*[\r\n]",&t);
	while(tc<=t){
		scanf("%s %d",st,&k);
		int l = strlen(st),ans = 0,fg = 0;
		for (int i = 0; i < l; ++i)
		{
			if(st[i] == '-'){
				if(i+k>l){
					fg = 1;
					break;
				}
				for (int j = i; j < i+k; ++j)
				{
					if(st[j] == '+')st[j] = '-';
					else st[j] = '+';
				}
				ans++;
			}
		}
		if(!fg)printf("Case #%d: %d\n",tc,ans );
		else printf("Case #%d: IMPOSSIBLE\n",tc,ans );
		tc++;
	}
}