//hi
#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
typedef long long int LL;
char s[1001];
char ans[1001];
pair<int,char> p[4];
int main(void){
    int t;
    scanf("%d",&t);
    for(int hh=1;hh<=t;hh++){
		int n;
		scanf("%d",&n);
		int i,j;
		int r,o,y,g,b,v;
		scanf("%d%d%d%d%d%d",&r,&o,&y,&g,&b,&v);
		p[0].F=r; p[0].S='R';
		p[1].F=y; p[1].S='Y';
		p[2].F=b; p[2].S='B';
		sort(p,p+3);
		//printf("%d %d %d\n",p[2].F, p[1].F, p[0].F);
		if(p[2].F>p[0].F+p[1].F) printf("Case #%d: IMPOSSIBLE\n",hh);
		else{
			int r;
			for(i=1,j=0;j<p[2].F;i+=2,j++) s[i]=p[2].S, r=i;
			for(i=0,j=0;j<p[1].F;i+=2,j++) s[i]=p[1].S;
			int x=p[1].F*2;
			for(i=x;i<r+1 && p[0].F>0;i+=2) s[i]=p[0].S, p[0].F--;
			for(i=0;i<n;i++) ans[i]=s[i];
			if(p[0].F>0){
				int e=0;
				for(i=0;i<n;i++){
					if(p[0].F>0 && i%2==0) ans[i]=p[0].S, p[0].F--;
					else ans[i]=s[e++];  
				}
			}
			ans[n]='\0';
			printf("Case #%d: %s\n",hh,ans);
		}
	}
    return 0;
}
