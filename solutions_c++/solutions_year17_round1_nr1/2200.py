#include <bits/stdc++.h>
#define pi acos(-1.0)
using namespace std;
int n,m;
char cake[100][100];
int a[100][100];
int upb[100],lob[100],leb[100],rib[100];
int cnt[100];
int main(){
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	while(T--){
		int n,m;
		scanf("%d%d",&n,&m);
		for (int i=0;i<n;i++)
			scanf("%s",cake[i]);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=m;j++)
				a[i][j]=((cake[i-1][j-1]=='?')?(0):(cake[i-1][j-1]-'A'+1));

		printf("Case #%d:\n",++ca );
		for (int i=1;i<=n;i++){
			int cntt = 0;
			for (int j=1;j<=m;j++)
				if (!a[i][j]) a[i][j]=a[i][j-1];
				else cntt++;
			for (int j=m;j;j--)
				if (!a[i][j]) a[i][j]=a[i][j+1];

			if (cntt == 0)
				for (int j=1;j<=m;j++)
					a[i][j]=a[i-1][j];
		}
		for (int i=n-1;i;i--)
			if (!a[i][1])
				for (int j=1;j<=m;j++)
					a[i][j]=a[i+1][j];
		for (int i=1;i<=n;i++){
			for (int j=1;j<=m;j++){
				if (a[i][j]) printf("%c", 'A'+a[i][j]-1);
			}
			puts("");
		}
	}
	return 0;
}