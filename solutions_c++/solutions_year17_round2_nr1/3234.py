#include<bits/stdc++.h>
using namespace std;

int tc,n;
double d;

int main(){
	FILE *fout = fopen("output_a.out","w");
	scanf("%d",&tc);
	for(int ii=1;ii<=tc;ii++){
		scanf("%lf %d",&d,&n);
		double ans;
		for(int i=0;i<n;i++){
			double k,v;
			scanf("%lf %lf",&k,&v);
			double temp=(v*d)/(d-k);
			if(i==0) ans=temp;
			else if(temp<ans) ans=temp;
		}
		printf("Case #%d: %.15lf\n",ii,ans);
		fprintf(fout,"Case #%d: %.15lf\n",ii,ans);
	}
	return 0;
}
