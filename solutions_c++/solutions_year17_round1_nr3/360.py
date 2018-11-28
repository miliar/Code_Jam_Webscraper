#include <bits/stdc++.h>
using namespace std;
int Hd,Ad,Hk,Ak,B,D;

void fuck()
{
	int i;
	int r1,r2,r3;
	int hd,ad,hk,ak;
	int ans=1000;
	scanf("%d%d%d%d%d%d",&Hd,&Ad,&Hk,&Ak,&B,&D);
	for(r1=0;r1<=200;r1++){
		hd=Hd;ad=Ad;hk=Hk;ak=Ak;
		for(i=1;i<=r1;i++){
			int next_ak=max(ak-D,0);
			if(hd-next_ak<=0) hd=Hd;
			else ak=next_ak;
			hd-=ak;
			if(hd<=0) break;
		}
		if(i<=r1) continue;
		for(r2=0;r2<=200;r2++){
			int hd1=hd,ad1=ad,hk1=hk,ak1=ak;
			for(i=1;i<=r2;i++){
				int next_ad=ad1+B;
				if(hd1-ak1<=0) hd1=Hd;
				else ad1=next_ad;
				hd1-=ak1;
			}
			for(i=1;i<=200;i++){
				int next_hk=hk1-ad1;
				if(next_hk<=0) break;
				if(hd1-ak1<=0) hd1=Hd;
				else hk1=next_hk;
				hd1-=ak1;
			}
			if(i<=200) ans=min(ans,r1+r2+i);
		}
	}
	if(ans>=1000) printf("IMPOSSIBLE\n");
	else printf("%d\n",ans);
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,t;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		printf("Case #%d: ",i);
		fuck();
	}
 return 0;
}

