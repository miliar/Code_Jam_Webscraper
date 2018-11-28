#include <bits/stdc++.h>
using namespace std;
#define N 30
int n,m;
char a[N][N];
int main(){
	freopen("A-large.in","r",stdin); freopen("A.out","w",stdout);
	int t; scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%d %d",&n,&m);
		for(int i=0;i<n;i++) scanf("%s",a[i]);
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if (a[i][j]=='?') continue;
				for(int k=j+1;k<m && (a[i][k]=='?' || a[i][k]==a[i][j]);k++) a[i][k]=a[i][j];
				for(int k=j-1;k>=0 && (a[i][k]=='?' || a[i][k]==a[i][j]);k--) a[i][k]=a[i][j];
			}
		}
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				if (a[i][j]=='?') continue;
				//if (i<n-1 && a[i+1][j]=='?') a[i+1][j]=a[i][j];
				//if (i>0 && a[i-1][j]=='?') a[i-1][j]=a[i][j];
				for(int k=i+1;k<n && (a[k][j]=='?' || a[k][j]==a[i][j]);k++) a[k][j]=a[i][j];
				for(int k=i-1;k>=0 && (a[k][j]=='?' || a[k][j]==a[i][j]);k--) a[k][j]=a[i][j];
			}
		}
		printf("Case #%d:\n",tc);
		for(int i=0;i<n;i++) puts(a[i]);
	}
}
