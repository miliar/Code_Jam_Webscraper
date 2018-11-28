#include <bits/stdc++.h>
using namespace std;
int t,k,ans;
char ch[1005];
bool flag;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	for (int i=1;i<=t;i++){
		ans=0;
		scanf("%s%d",&ch,&k);
		//printf("%s",ch);
		for (int j=0;j<strlen(ch)-k+1;j++){
			if (ch[j]=='-'){
				ans++;
				for (int j1=j;j1<=j+k-1;j1++){
					if (ch[j1]=='-') ch[j1]='+';
					else ch[j1]='-';
				}
			}
		}
		flag=true;
		for (int j=0;j<strlen(ch);j++)
		if (ch[j]=='-') flag=false;
		if (flag) printf("Case #%d: %d\n",i,ans);
		else printf("Case #%d: IMPOSSIBLE\n",i);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
