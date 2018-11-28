#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<queue>
#include<deque>
#include<string>
#include<string.h>
#include<vector>
#include<set>
#include<map>
#include<stdlib.h>
#include<cassert>
using namespace std;
const long long mod=1000000007;
const long long inf=mod*mod;
const long long d2=500000004;

int main(){
	int T;scanf("%d",&T);
	for(int t=1;t<=T;t++){
		int HD,AD,HK,AK,B,D;
		scanf("%d%d%d%d%d%d",&HD,&AD,&HK,&AK,&B,&D);
		long long ret=inf;
		for(int i=0;i<=100;i++){
			for(int j=0;j<=100;j++){
				int R=HD;
				int K=HK;
				int ad=AD;
				int ak=AK;
				long long tmp=0;
				for(int k=0;k<i;k++){
					if(R-max(0,ak-D)<=0){
						tmp++;
						R=HD-ak;
					}
					ak=max(0,ak-D);
					R-=ak;
					if(R<=0){tmp=-1;break;}
					tmp++;
				}
				if(tmp==-1)continue;
				for(int k=0;k<j;k++){
					if(R-ak<=0){
						tmp++;
						R=HD-ak;
					}
					ad+=B;
					R-=ak;
					if(R<=0){tmp=-1;break;}
					tmp++;
				}if(tmp==-1)continue;
			//	if(j==0)printf("%d %d %d %d\n",R,K,ad,ak);
				while(K>0){
					if(K>ad&&R-ak<=0){
						tmp++;
						R=HD-ak;
					}
					K-=ad;
					if(K>0)R-=ak;
					if(R<=0){tmp=-1;break;}
					tmp++;
				}
				if(tmp==-1)continue;
			//	if(j==0)printf("%d %d: %lld\n",i,j,tmp);
		
				ret=min(tmp,ret);
			}
		}
		if(ret==inf)printf("Case #%d: IMPOSSIBLE\n",t);
		else printf("Case #%d: %lld\n",t,ret);
	}
}