#include <bits/stdc++.h>
using namespace std;

char s[1020];
int a[1020], x[1010];
int n,m;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	int Case;
	scanf("%d",&Case);
	for (int o=1;o<=Case;o++){
		scanf(" %s %d", s, &m);
		n=strlen(s);
		for (int i=0;i<n;i++)
			a[i]=s[i]=='-';
		x[0]=a[0];
		for (int i=1;i<m;i++)
			x[i]=a[i]^a[i-1];
		for (int i=m;i<n-m+1;i++)
			x[i]=a[i]^a[i-1]^x[i-m];

		int sum=0;
		for (int i=0;i<n-m+1;i++)
			sum+=x[i];
		int flag=1;
		for (int i=0;i<n-m+1;i++){
			for (int j=0;j<m;j++)
				a[i+j]^=x[i];
		}
		for (int i=0;i<n;i++)
			if (a[i]==1){
				flag=0;
				break;
			}
		if (flag)
			printf("Case #%d: %d\n", o, sum);
		else
			printf("Case #%d: IMPOSSIBLE\n", o);
	}
	return 0;
}