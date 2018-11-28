#include<iostream>
#include<cstdio>
using namespace std;
double mini;
int e[105]={},s[105]={};
int d[105][105]={};
int main(){
	int T,I;
	scanf("%d",&T);
	for(I=0;I<T;I++){
		double time[105];
		int n,q;
		scanf("%d %d",&n,&q);
		int i,j;
		for(i=0;i<n;i++)scanf("%d %d",&e[i],&s[i]);
		for(i=0;i<n;i++){
			time[i]=1e15;
		}
		for(i=0;i<n;i++){
			for(j=0;j<n;j++)scanf("%d",&d[i][j]);
		}
		int u,v;
		for(i=0;i<q;i++){
			scanf("%d %d",&u,&v);
		}
		time[0]=0.0;
		for(i=0;i<n-1;i++){
			double dis=0.0;
			for(j=i+1;j<n;j++){
				if(dis+d[j-1][j]>e[i])break;
				if(1.0*(dis+d[j-1][j])/s[i]+time[i]<time[j]){
					time[j]=1.0*(dis+d[j-1][j])/s[i]+time[i];
				}
				dis+=d[j-1][j];
			}
		}
		printf("Case #%d: ",I+1);
		printf("%lf\n",time[n-1]);
	}
	return 0;
}