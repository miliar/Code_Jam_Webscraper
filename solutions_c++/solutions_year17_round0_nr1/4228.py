#include <bits/stdc++.h>

using namespace std;

int k;
char ch[1010];

int main(){
	int T;
	scanf("%d",&T);
	for (int ti=1;ti<=T;ti++){
		scanf("%s%d",ch, &k);
		int l = strlen(ch);
		int ans=0;
		for (int i=0;i<l;i++){
			if (i+k-1>=l) break;
			if (ch[i]=='-'){
				for (int j=0;j<k;j++)
					if (ch[i+j]=='-') ch[i+j]='+';
						else ch[i+j]='-';
				ans++;
			}
		}
		for (int i=0;i<l;i++)
			if (ch[i]=='-') ans=-1;
		printf("Case #%d: ", ti);
		if (ans==-1) printf("IMPOSSIBLE\n");
			else printf("%d\n", ans);
	}
	return 0;
}
