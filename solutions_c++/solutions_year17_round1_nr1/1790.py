#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
using namespace std;
char S[55][55],C[27];
int A[27][2];
int main(){
	int T,n,m,num;
	freopen("A-large.in.txt","r",stdin);
	freopen("A-large.out.txt","w",stdout);
	scanf("%d",&T);
	for (int cases=1;cases<=T;cases++){
		scanf("%d%d",&n,&m);
		memset(A,-1,sizeof(A));
		num=0;
		for (int i=0;i<n;i++) scanf("%s",S[i]); 
        for (int j=0;j<m;j++)
        	for (int i=0;i<n;i++)
				if (S[i][j]!='?'){ 
					A[num][0]=i;
					A[num][1]=j; 
					C[num]=S[i][j];
					num++;
				}  
		for (int t=0;t<num;t++){
			int y=A[t][0],x=A[t][1],y0,x0,y1=y,x1=x; 
			for (y0=y-1;y0>=0 && S[y0][x]=='?';y0--); 
			y0++;
			for (y1=y+1;y1<n && S[y1][x]=='?';y1++);
			y1--;
			for (x0=x;x0>=0;x0--){
				bool f=true;
				for (int i=y0;i<=y1;i++)
					for (int j=x0;j<=x;j++){
						if (i==y && j==x) continue;
						if (S[i][j]!='?') f=false;
					}
				if (!f) break;
			}
			x0++; 
			for (x1=x;x1<m;x1++){
				bool f=true;
				for (int i=y0;i<=y1;i++)
					for (int j=x0;j<=x1;j++){
						if (i==y && j==x) continue;
						if (S[i][j]!='?') f=false;
					}
				if (!f) break;						
			}
			x1--;
			//printf("%c: %d %d %d %d\n",'A'+t,y0,x0,y1,x1);
			for (int i=y0;i<=y1;i++)
				for (int j=x0;j<=x1;j++)
					S[i][j]=C[t];
		}
		printf("Case #%d:\n",cases);
		for (int i=0;i<n;i++)
			printf("%s\n",S[i]);
	}
	return 0;
}