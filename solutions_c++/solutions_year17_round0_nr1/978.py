#include<bits/stdc++.h>
#define rep(ii,x,y) for(int ii=(x);ii<(y);ii++)
using namespace std;
int cas,l,t,ans,k;
char str[2000];

int main(){
#ifdef AKAISORA
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	// freopen("in.txt","r",stdin);
	// freopen("out.txt","w",stdout);
#endif
	scanf("%d",&cas);
	for(int t=1;t<=cas;t++){
		scanf("%s %d",str,&k);
		printf("Case #%d: ",t);
		l=strlen(str);
		ans=0;
		rep(i,0,l-k+1){
			if(str[i]=='-'){
				ans++;
				rep(j,i,i+k){
					str[j]=str[j]=='+'?'-':'+';
				}
			}
		}
		bool flag=true;
		rep(i,l-k+1,l){
			if(str[i]=='-'){flag=false;break;}
		}
		if(!flag)printf("IMPOSSIBLE\n");
		else printf("%d\n",ans);
	}
	return 0;
}