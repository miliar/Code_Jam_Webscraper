#include <bits/stdc++.h>

using namespace std;

int main()
{
	int tc, n;
	scanf("%d",&tc);

	double d, tmax=-1.0, k, s, t;
	for(int i=1;i<=tc;i++){
		tmax=-1.0;
		scanf("%lf %d",&d,&n);
		for(int j=0;j<n;j++){
			scanf("%lf %lf",&k,&s);
			t = (d-k)/s;
			if(t>tmax) tmax=t;
		}
		double ans = d / tmax;
		printf("Case #%d: %.6lf\n",i,ans );
	}
	return 0;
}