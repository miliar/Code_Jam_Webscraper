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

int Hd,Ad,Hk,Ak,B,D;

void solve()
{
	cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
	int Ans=-1;
	for(int i=0;i<=100;i++)
		for(int j=0;j<=100;j++)
		{
			int hd=Hd,ad=Ad,hk=Hk,ak=Ak,cishu=0,t=i;
			while(t--)
			{
				if(hd-max(0,ak-D)<=0)
					hd=Hd-ak,cishu++;
				if(hd-max(0,ak-D)<=0)
				{
					cishu=-1;
					break; 
				}
				ak=max(0,ak-D);hd-=ak;cishu++;
			}
			if(cishu==-1)
				continue;
			t=j;
			while(t--)
			{
				if(hd-ak<=0)
					hd=Hd-ak,cishu++;
				if(hd-ak<=0)
				{
					cishu=-1;
					break; 
				}
				ad+=B;hd-=ak;cishu++;
			}
			if(cishu==-1)
				continue;
			t=100;
			while(t--)
			{
				if(hk<=ad)
				{
					hk-=ad,cishu++;break;
				}
				if(hd-ak<=0)
					hd=Hd-ak,cishu++;
				if(hd-ak<=0)
				{
					cishu=-1;
					break; 
				}
				hk-=ad;hd-=ak;cishu++;
			}
			if(hk<=0&&cishu!=-1&&(Ans==-1||Ans>cishu))
				Ans=cishu;
		}
	if(Ans==-1)
		cout<<"IMPOSSIBLE"<<endl;
	else
		cout<<Ans<<endl;
}

int main()
{
#ifndef ONLINE_JUDGE
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
#endif
	int T;cin>>T;
	for(int i=1;i<=T;i++)
		printf("Case #%d: ",i),solve();
	return 0;
}

