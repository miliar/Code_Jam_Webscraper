#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <set>
#include <queue>
#include <map>
#include <string>
#include <unordered_map>
#include <unordered_set>

using namespace std;

int d[101][101][101];

int rec(int i,int j,int k)
{
	if(d[i][j][k]!=-1)
		return d[i][j][k];
	if(!i && !j && !k)
		return d[i][j][k]=0;
	int ans=1;
	if(i && k)
		ans=max(ans,rec(i-1,j,k-1)+1);
	if(j>=2)
		ans=max(ans,rec(i,j-2,k)+1);
	if(i>=2 && j)
		ans=max(ans,rec(i-2,j-1,k)+1);
	if(i>=4)
		ans=max(ans,rec(i-4,j,k)+1);
	if(k>=4)
		ans=max(ans,rec(i,j,k-4)+1);
	if(j && k>=2)
		ans=max(ans,rec(i,j-1,k-2)+1);
	return d[i][j][k]=ans;
}

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T,n,p,i,u[5],ts,ans,j,k;
	scanf("%d",&T);
	for(ts=1;ts<=T;ts++)
	{
		scanf("%d%d",&n,&p);
		for(i=0;i<p;i++)
			u[i]=0;
		while(n--)
		{
			scanf("%d",&i);
			u[i%p]++;
		}
		printf("Case #%d: ",ts);
		if(p==2)
		{
			printf("%d\n",u[0]+(u[1]+1)/2);
			continue;
		}
		if(p==3)
		{
			ans=u[0];
			i=min(u[1],u[2]);
			ans+=i;
			u[1]-=i;
			u[2]-=i;
			printf("%d\n",ans+(u[1]+2)/3+(u[2]+2)/3);
			continue;
		}
		for(i=0;i<=u[1];i++)
			for(j=0;j<=u[2];j++)
				for(k=0;k<=u[3];k++)
					d[i][j][k]=-1;
		printf("%d\n",rec(u[1],u[2],u[3])+u[0]);
	}
	return 0;
}