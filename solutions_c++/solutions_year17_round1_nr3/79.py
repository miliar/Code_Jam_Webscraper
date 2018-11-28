#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<iostream>
using namespace std;

int fight(int  Hd,int Ad,int Hk,int Ak,int B,int D,int bn,int dn)
{
	int H=Hd;
	int cnt=0;
	while(1)
	{
		cnt++;
		if(Hk<=Ad)return cnt;
		if(cnt>=1000)return 100000000;
		int dm=Ak;
		if(dn)dm=max(dm-D,0);
		if(H<=dm)
		{
			H=Hd-Ak;
			if(H<=0)return 100000000;
			continue;
		}
		if(dn)
		{
			dn--;
			Ak=max(0,Ak-D);
			H-=Ak;
			continue;
		}
		if(bn)
		{
			bn--;
			Ad+=B;
			H-=Ak;
			continue;
		}
		Hk-=Ad;
		H-=Ak;
	}
}

int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("c_b.out","w",stdout);
	int T=0;
	scanf("%d",&T);
	for(int qi=1;qi<=T;qi++)
	{
		printf("Case #%d: ",qi);
		int Hd,Ad,Hk,Ak,B,D,ans;
		cin>>Hd>>Ad>>Hk>>Ak>>B>>D;
		ans=100000000;
		for(int i=0;i<=100;i++)
			for(int j=0;j<=100;j++)
				ans=min(ans,fight(Hd,Ad,Hk,Ak,B,D,i,j));
		if(ans>=100000000)puts("IMPOSSIBLE");
		else cout<<ans<<endl;
	}
	return 0;
}

