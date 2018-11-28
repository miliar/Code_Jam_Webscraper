#include<algorithm>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include  <stdio.h>
#include   <math.h>
#include   <time.h>
#include   <vector>
#include   <bitset>
#include    <queue>
#include      <set>
#include      <map>
using namespace std;

const int N=1005;

char str[N];
int k,n;

void solve()
{
	cin>>str>>k;
	n=strlen(str);
	int Ans=0;
	for(int i=0;i<=n-k;i++)
		if(str[i]=='-')
		{
			Ans++;
			for(int j=0;j<k;j++)
				if(str[i+j]=='-')
					str[i+j]='+';
				else
					str[i+j]='-';
		}
	for(int i=0;i<n;i++)
		if(str[i]=='-')
		{
			puts("IMPOSSIBLE");
			return;
		}
	printf("%d\n",Ans);
}

int main()
{
//#ifndef ONLINE_JUDGE
//	freopen("A.in","r",stdin);
//	freopen("A.out","w",stdout);
//#endif
	int T;cin>>T;
	for(int i=1;i<=T;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}

