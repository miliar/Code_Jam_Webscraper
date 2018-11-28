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

const int N=55;

char s[N][N];
int n,m,ok[N];

void fillall(int i)
{
	int pos=-1;
	for(int j=0;j<m;j++)
		if(s[i][j]!='?')
		{
			pos=j;break;
		}
	for(int j=0;j<pos;j++)
		s[i][j]=s[i][pos];
	for(int j=pos;j<m;j++)
		if(s[i][j]=='?')
			s[i][j]=s[i][j-1];
}

void copy(int i,int ii)
{
	for(int j=0;j<m;j++)
		s[ii][j]=s[i][j];
}

void solve()
{
	cin>>n>>m;
	int pos=-1;
	for(int i=0;i<n;i++)
	{
		cin>>s[i];
		ok[i]=0;
		for(int j=0;j<m;j++)
			if(s[i][j]!='?')
				ok[i]=1;
		if(ok[i])
			pos=i;
	}
	fillall(pos);
	for(int i=pos-1;i>=0;i--)
		if(ok[i])
			fillall(i);
		else
			copy(i+1,i);
	for(int i=pos+1;i<n;i++)
		if(ok[i])
			fillall(i);
		else
			copy(i-1,i);
	for(int i=0;i<n;i++)
		cout<<s[i]<<endl;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
#endif
	int T;cin>>T;
	for(int i=1;i<=T;i++)
		printf("Case #%d:\n",i),solve();
	return 0;
}

