#include <bits/stdc++.h>
#define pi acos(-1.0)
using namespace std;
int n;
char s[1005];
int main(){
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	while(T--){ 
		int n,r,g,b,o,v,y;
		scanf("%d%d%d%d%d%d%d",&n,&r,&o,&y,&g,&b,&v);
		printf("Case #%d: ",++ca );
		if ((r>n/2)||(b>n/2)||(y>n/2)) {puts("IMPOSSIBLE");continue;}
		memset(s,0,sizeof s);
		int rr,bb,yy;
		bb=b;
		yy=y;
		rr=r;
		for (int i=0;i<n;i+=2){
			if (rr == 0) break;
			s[i]='R';
			rr--;
		}
		if (yy>bb){
			for (int i=n-1;i>=0;i-=2){
				if (!yy) break;
				yy--;
				while (s[i]) i--;
				if (!i) break;
				s[i]='Y';
			}
			for (int i=n-1;i>=0;i-=2){
				if (!bb) break;
				bb--;
				while (s[i]) i--;
				if (!i) break;
				s[i]='B';
			}
		}
		else{
			for (int i=n-1;i>=0;i-=2){
				if (!bb) break;
				bb--;
				while (s[i]) i--;
				if (!i) break;
				s[i]='B';
			}
			for (int i=n-1;i>=0;i-=2){
				if (!yy) break;
				yy--;
				while (s[i]) i--;
				if (!i) break;
				s[i]='Y';
			}
		}
		s[n]= 0;
		puts(s);
	}
	return 0;
}