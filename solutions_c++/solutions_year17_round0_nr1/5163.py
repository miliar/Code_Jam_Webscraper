#include<cstdio>
#include<cstring>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
int T,n;
char s[1005];
int f[1005][2]/*,a[1005]*/;
void dp(){
	int i,l,j,ans=0;
	l=strlen(s+1);
	/*for(i=1;i<=l;i++){
		if(s[i]=='+') a[i]=1;
		else a[i]=0;
		}*/
	for(i=1;i<=l-n+1;i++){
		if(s[i]=='-'){
			ans++;
			for(j=i;j<i+n;j++){
				if(s[j]=='+') s[j]='-';
				else s[j]='+';
				}
			}
		}
	for(i=l-n+1;i<=l;i++){
		if(s[i]=='-') {puts("IMPOSSIBLE"); return;}
		}
	printf("%d\n",ans);
	return;
	}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("11.out","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		printf("Case #%d: ", i);
		scanf("%s",s+1);
		scanf("%d",&n);
		dp();
		}
	return 0;
	}
