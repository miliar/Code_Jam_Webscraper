#include <bits/stdc++.h>
using namespace std;

double d;
int n;
int tc;
double k[1005], s[1005];

int main(){
	freopen("out.txt","w",stdout);
	
	scanf("%d",&tc);
	for ( int t = 1; t <= tc; t++ ){
		scanf("%lf%d",&d,&n);
		double res = 0;
		for ( int i = 0; i < n; i++ ){
			scanf("%lf%lf",&k[i],&s[i]);
			res = max(res, (d-k[i])/s[i]);
		}
		
		printf("Case #%d: %.9lf\n",t,d/res);
	}
	fclose(stdout);
	return 0;
}
