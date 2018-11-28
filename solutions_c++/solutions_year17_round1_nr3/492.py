#include <cstdio>
#include <cstring>
#define oo 1000000000
using namespace std;
int Hd,Ad,Hk,Ak,B,D;
int ans;
int simulate(int Bt,int Dt){
	int t = 0;
	int tHd = Hd,tAd = Ad,tHk = Hk,tAk = Ak;
	if(Hk<=Ad)return 1;
	if(Hd<=Ak-D)return oo;
	do{
		t++;

		//printf("%d %d %d %d %d\n",t, tHd,tAd,tHk,tAk);
		if(t>ans)return ans;
		if(t>Hk*5)return ans;
		if(tHd<=0)return oo;
		if(tHk<=tAd)return t;
		//printf("%d %d %d %d %d\n",t, tHd,tAd,tHk,tAk);
		if(tHd<=tAk&&(Dt<=0||tHd<=tAk-D)){
			tHd = Hd;
		}else if(Dt>0){
			tAk-=D;
			if(tAk<0)tAk=0;
			Dt--;
		}else if(Bt>0){
			tAd+=B;
			Bt--;
		}else tHk-=tAd;
		tHd-=tAk;
	}while(1);
	return t;
}
void easy(){
	int i,j,l;
	int k;
	for(i=0;i<=100;i++)
		for(j=0;j<=100;j++){
			//printf("%d %d\n",Hd,Ad);
			k = simulate(i,j);
			//printf("%d %d\n",k,ans);
			if(k<ans)ans=k;
		}
}
int main(){
	int T,tt,n,m,i,j,k,l;
	tt=0;
	scanf("%d",&T);
	while(T--){
		tt++;
		ans = oo;
		scanf("%d%d%d%d%d%d",&Hd,&Ad,&Hk,&Ak,&B,&D);
		if(Hd<=100&&Ad<=100&&Hk<=100&&Ak<=100&&B<=100&&D<=100){
			easy();
			if(ans<oo)printf("Case #%d: %d\n",tt,ans);
			else printf("Case #%d: IMPOSSIBLE\n",tt);
		}
	}
	return 0;
}
