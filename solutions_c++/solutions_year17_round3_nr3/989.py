#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
#define max(a,b) (a>b?a:b)
#define ll long long
#include<iostream>
#include<iomanip>
bool cmp(double a,double b){
	return a<b;
}
int main(){
	freopen("C-small-1-attempt1.in","r",stdin);
	freopen("zzz","w",stdout);
	int T;
	scanf("%d",&T);
	for(int xx=1;xx<=T;xx++){
		int n,k;
		double train=0,li[100];
		scanf("%d%d%lf",&n,&k,&train);
		for(int i=0;i<n;i++){
			scanf("%lf",&li[i]);
		}li[n]=1;
		n++;
		std::sort(li,li+n,cmp);
		for(int i=1;i<n;i++){
			// ¨ìi«e¥­§¡
			if(train==0) break;
			if(train<(i*(li[i]-li[i-1]))){
				for(int j=0;j<i;j++){
					li[j]+=(train/i);
				}
				train=0;
			}else{
				train -= (i*(li[i]-li[i-1]));
				for(int j=0;j<i;j++){
					li[j]=li[i];
				}
			}
		//	for(int ii=0;ii<n;ii++){
		//		printf("%f ",li[ii]);
		//	}puts("");
		}
		double P=1;
		for(int i=0;i<n;i++){
			P*=li[i];
		}
		printf("Case #%d: %f\n",xx,P);
	//	std::cout << std::fixed << std::setprecision(9) << fin << std::endl;
	}
	return 0;
}
