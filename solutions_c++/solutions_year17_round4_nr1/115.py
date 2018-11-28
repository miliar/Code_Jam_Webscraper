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

void solve()
{
	int a[4]={},Ans=0,P,n,k=0;
	cin>>n>>P;
	for(int i=1,t;i<=n;i++)
		cin>>t,a[t%P]++,k+=t;
	Ans=a[0];
	if(P==2)
		Ans+=a[1]/2;
	else if(P==3)
		Ans+=min(a[1],a[2])+(max(a[1],a[2])-min(a[1],a[2]))/3;
	else
	{
		Ans+=min(a[1],a[3]);
		a[1]=max(a[1],a[3])-min(a[1],a[3]);
		int t=min(a[1]/2,a[2]);
		a[1]-=2*t;a[2]-=t;
		Ans+=t+a[1]/4+a[2]/2;
	}
	cout<<Ans+(k%P!=0)<<endl;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
#endif
	int t;cin>>t;
	for(int i=1;i<=t;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}

