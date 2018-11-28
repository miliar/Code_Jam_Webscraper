#include<bits/stdc++.h>
using namespace std;
const int N=10000005;
char a[N];
int n,k;
void solve()
{
	scanf("%s%d",a,&k);n=strlen(a);
	int moves=0;
	for(int i=0; i+k-1<n; ++i)
	{
		if(a[i]=='-')
		{
			moves++;
			for(int j=i; j<=i+k-1; ++j)
				if(a[j]=='+')
					a[j]='-';
				else
					a[j]='+';
		}	
	}
	bool czy=true;
	for(int i=0; i<n; ++i)
		if(a[i]=='-')
			czy=false;
	if(!czy)
		puts("IMPOSSIBLE");
	else
		printf("%d\n",moves);
}
int main()
{
	int te; scanf("%d", &te);
	for(int i=1; i<=te; ++i)
	{
		printf("Case #%d: ",i);
		solve();
	}
	return 0;
}
