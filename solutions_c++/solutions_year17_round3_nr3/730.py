#include <stdio.h>
#include <vector>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

const int INF=1e9+10;

int main(){
	int t;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		int n,k;
		scanf("%d %d",&n,&k);
		if(n==k){
			double p[100],u;
			scanf("%lf",&u);
			for(int i=0;i<n;i++) scanf("%lf",&p[i]);
			sort(p,p+n);
			p[n]=1000.0;
			double sum=0.0;
			for(int i=0;i<n;i++){
				sum+=p[i];
//				printf("sum==%lf outro==%lf\n",sum+u, ((double)(i+1))*p[i+1] );
				if(sum+u<((double)(i+1))*p[i+1]){
					for(int j=0;j<=i;j++){	
						p[j]=min( (sum+u)/((double)(i+1)) , 1.0 );
//						printf("p[%d]==%lf\n",j,p[j]);
					}
					break;
				}
			}
			double prob=1.0;
			for(int i=0;i<n;i++){
				 prob*=p[i];
//				 printf("p[%d]==%lf\n",i,p[i]);
			}
			printf("Case #%d: %lf\n",tt,prob);
		}
		else{
			//harder
		}
	}
	return 0;
}
