#include <bits/stdc++.h>

using namespace std;

int n,k;
double u;
double chip[111];

void input(){
	scanf("%d%d",&n,&k);
	scanf("%lf",&u);
	for(int i=0; i<n; i++)cin>>chip[i];
}

void solve(int kase){
	sort(chip,chip+n);

	// for(int i=0; i<n; i++)
	// 	printf("%.2f ",chip[i]);
	// printf("\n");

	for(int i=0; i<n && u>0; i++){
		double diff=0;
		if(i==n-1){
			diff=min(1-chip[i], u/(i+1));
		}else if(chip[i]<chip[i+1]){
			diff=min(chip[i+1]-chip[i], u/(i+1));
			// printf("%d: %.1f\n",i,chip[i+1]-chip[i]);
		}
		if(diff<0)continue;
		for(int j=0; j<=i; j++){
			// printf("%d: %.1f -> %.1f\n",i,chip[j],chip[j]+diff);
			chip[j]+= diff;
		}
		u-=diff*(i+1);
	}
	printf("Case #%d: ",kase+1);
	double ans=1;

	for(int i=0; i<n; i++)
		ans*=(chip[i]);
	printf("%f\n",ans);
	// for(int i=0; i<n; i++)
	// 	printf("%.2f ",chip[i]);
	// printf("\n");
}

int main(){
	int zz;
	scanf("%d",&zz);
	for(int i=0; i<zz; i++){
		input();
		solve(i);
	}
}
