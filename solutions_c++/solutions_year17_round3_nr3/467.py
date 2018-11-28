#include <bits/stdc++.h>

using namespace std;

double u,p[105];
int t,n,k;

int main(){
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&k);
		scanf("%lf",&u);
		for(int j=0;j<n;j++){
			scanf("%lf",&p[j]);
		}
		double left =0.0;
		double right = 1.0;
		double mid;
		int cnt = 1000;
		while(cnt>0){
			mid = (left+right)/2;
			double need = 0.0;
			for(int j=0;j<n;j++)
				if( mid > p[j])
					need += mid-p[j];
			if(need>u){
				right = mid;
			}else left = mid;
			cnt--;
		}
		
		double ans=1.0;
		for(int j=0;j<n;j++)
		{
			if(mid > p[j])
				ans*=mid;
			else ans *=p[j];
		}
		printf("Case #%d: %lf\n",i,ans);
	}
	
	return 0;
}
