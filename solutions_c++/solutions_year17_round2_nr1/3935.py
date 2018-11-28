#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int te=1; te<=t; te++){
		long long int d,n;
		scanf("%lld %lld",&d,&n);
		pair<long long int,long long int> p[n];
		for(int i=0; i<n; i++){
			scanf("%lld%lld",&p[i].first,&p[i].second);
		}
		double ans;
		sort(p,p+n);
		if(n == 1){
			double t = ((double)(d-p[0].first))/p[0].second;
			ans = (double)d/t;
			printf("Case #%d: %.8lf\n",te,ans);
		}
		else if(n==2){
			if(p[0].second > p[1].second){
				double t = ((double)(p[1].first-p[0].first))/(p[0].second-p[1].second);
				double dist = (double)(p[0].first + p[0].second*t);
				if(dist >= d){
					double t = ((double)(d-p[0].first))/p[0].second;
					ans = (double)d/t;
					printf("Case #%d: %.8lf\n",te,ans);
				}
				else{
					double t = ((double)(d-p[1].first))/p[1].second;
					ans = (double)d/t;
					printf("Case #%d: %.8lf\n",te,ans);
				}	
			}
			else{
				double t = ((double)(d-p[0].first))/p[0].second;
				ans = (double)d/t;
				printf("Case #%d: %.8lf\n",te,ans);
			}
		}
	}
	return 0;
}
