#include<bits/stdc++.h>
using namespace std;
const int N=1005;
char a[N];
int n;
void solve()
{
	scanf("%s",a);n=strlen(a);
	bool isSorted=true;
	for(int i=1; i<n; ++i)
		if(a[i-1]>a[i])
			isSorted=false;
	if(isSorted) 
	{
		puts(a);
		return;
	}
	for(int i=n-1; i>=0; --i) if(a[i]!='1')
	{
		isSorted=true;
		for(int j=1; j<i; ++j)
			if(a[j-1]>a[j])
				isSorted=false;
		if(a[i]-1<a[i-1])
			isSorted=false;
		if(isSorted)
		{
			for(int j=0; j<i; ++j)
				printf("%c",a[j]);
			printf("%c",a[i]-1);
			for(int j=i+1; j<n; ++j)
				printf("9");
			printf("\n");
			return;
		}
	}
	for(int i=0; i<n-1; ++i)
		printf("9");
	printf("\n");
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
