/*input
3
---+-++- 3
+++++ 4
-+-+- 4
*/
#include <bits/stdc++.h>
#define X first
#define Y second
#define REP(i,n) for(int i=0;i<n;i++)
#define ENDL printf("\n")
using namespace std;
char str[10100];
int a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
int main(){
	scanf(" %d",&t);
	for(l=1;l<=t;l++){
		printf("Case #%d: ",l);
		scanf(" %s %d",str,&k);
		m = strlen(str);
		c = 0;
		for(i=0;i<m-k+1;i++){
			if(str[i]=='-'){
				c++;
				for(j=i;j<=i+k-1;j++){
					if(str[j]=='-')str[j]='+';
					else str[j]='-';
				}
			}
		}
		for(i=0;i<m;i++){
			if(str[i]!='+')break;
		}
		if(i==m)printf("%d\n",c);
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}