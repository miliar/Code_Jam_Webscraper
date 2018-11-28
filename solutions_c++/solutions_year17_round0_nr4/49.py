#include<iostream>
#include<cmath>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int pd[110][110],n,m,ans[110][110];
char ch[110];
int b[210][210],v[210],aim[210],A[210],B[210];
int find(int k){
	for (int i=1;i<=2*n;i++)
		if (b[k][i]&&v[i]==0){
			v[i]=1;
			if (aim[i]==0||find(aim[i])){
				aim[i]=k; return 1;
			}
		}
	return 0;
}
void solve(){
	scanf("%d%d",&n,&m);
	memset(pd,0x00,sizeof pd);
	int an=0;
	for (;m;m--){
		int x,y;
		scanf("%s%d%d",ch+1,&x,&y);
		if (ch[1]=='o') pd[x][y]=3,an+=2; else if (ch[1]=='+') pd[x][y]=1,an++; else pd[x][y]=2,an++;
	}
	memcpy(ans,pd,sizeof pd);
	
	memset(A,0x00,sizeof A);
	memset(B,0x00,sizeof B);
	memset(b,0x00,sizeof b);
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
			if (pd[i][j]&2) A[i]=1,B[j]=1;
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
			if (A[i]==0&&B[j]==0) b[i][j]=1;
	memset(aim,0x00,sizeof aim);
	for (int i=1;i<=n;i++){
		memset(v,0x00,sizeof v);
		if (find(i)) an++;
	}
	for (int i=1;i<=n;i++)
		if (aim[i]) ans[aim[i]][i]|=2;
		
	memset(A,0x00,sizeof A);
	memset(B,0x00,sizeof B);
	memset(b,0x00,sizeof b);
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
			if (pd[i][j]&1) A[i+j]=1,B[i-j+n+1]=1;
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
			if (A[i+j]==0&&B[i-j+n+1]==0) b[i+j][i-j+n+1]=1;
	memset(aim,0x00,sizeof aim);
	for (int i=1;i<=n*2;i++){
		memset(v,0x00,sizeof v);
		if (find(i)) an++;
	}
	for (int i=1;i<=n*2;i++)
		if (aim[i]){
			int k1=aim[i],k2=i-n-1;
			ans[(k1+k2)/2][(k1-k2)/2]|=1;
		}
	
	int where=0;
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
			if (pd[i][j]!=ans[i][j]) where++;
	
	for (int a=1;a<=n;a++)
		for (int b=1;b<=n;b++)
			for (int c=1;c<=n;c++)
				for (int d=1;d<=n;d++)
					if (a!=c||b!=d){
						if ((a==c||b==d)&&(ans[a][b]&2)&&(ans[c][d]&2)) cerr<<"fa "<<a<<" "<<b<<" "<<c<<" "<<d<<endl;
						if ((a+b==c+d||a-b==c-d)&&(ans[a][b]&1)&&(ans[c][d]&1)) cerr<<"fa "<<a<<" "<<b<<" "<<c<<" "<<d<<endl;
					}
	printf("%d %d\n",an,where);
	for (int i=1;i<=n;i++)
		for (int j=1;j<=n;j++)
			if (pd[i][j]!=ans[i][j]){
				if (ans[i][j]==3) putchar('o'); else if (ans[i][j]==2) putchar('x'); else putchar('+');
				printf(" %d %d\n",i,j);
			}
}
int main(){
	freopen("Dl.in","r",stdin);
	freopen("Dl.out","w",stdout);
	int t; scanf("%d",&t);
	for (int i=1;i<=t;i++){
		printf("Case #%d: ",i); solve();
	}
	return 0;
}
