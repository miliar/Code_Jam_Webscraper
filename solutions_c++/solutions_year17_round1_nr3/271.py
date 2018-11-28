#include<bits/stdc++.h>
using namespace std;
int T,Hd,Ad,Hk,Ak,B,D,ans,p,H,t,i,tt,A,cnt,j,hd,ad,hk,ak,s;
int main(){
	freopen("1.in","r",stdin);
	freopen("2.out","w",stdout);
	scanf("%d",&T);
	for(int tec=1;tec<=T;tec++){
		ans=2e9;
		scanf("%d%d%d%d%d%d",&Hd,&Ad,&Hk,&Ak,&B,&D);
		for(i=0;i<=(B?(Hk-Ad)/B+1:0);i++)
			for(j=0;j<=(D?Ak/D+1:0);j++)
			{
				//printf("%d %d\n",i,j);
				hd=Hd;ad=Ad;hk=Hk;ak=Ak;
				t=i;s=j;cnt=0;
				for(;hk>0;cnt++)
				if(s){
					if(hd-ak+D<=0){
						hd=Hd-ak;
						if(hd-ak+D<=0)break;
					}else ak=max(0,ak-D),hd-=ak,s--;
				}else if(t){
					if(hd-ak<=0){
						hd=Hd-ak;
						if(hd-ak<=0)break;
					}else ad+=B,hd-=ak,t--;
				}else if(hd-ak<=0&&hk-ad>0){
					hd=Hd-ak;
					if(hd-ak<=0)break;
				}else hk-=ad,hd-=ak;
				if(hk>0)continue;
				//printf("%d %d %d\n",i,j,cnt);
				ans=min(ans,cnt);
			}
		printf("Case #%d: ",tec);
		if(ans<2e9)printf("%d\n",ans);
		else puts("IMPOSSIBLE");
	}
}
