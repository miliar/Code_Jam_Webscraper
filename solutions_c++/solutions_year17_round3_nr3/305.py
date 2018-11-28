#include <bits/stdc++.h>
using namespace std;
#define maxn 1440

int tc;
int n,m,k;
double U;
double f[55];
double res;

bool can( double x ){
	double sum = U;
	double tmp = 1;
	for ( int i = 0; i < n; i++ ){
		double y = max((double)(0), x-f[i]);
		if ( y > sum ) return 0;
		sum -= y;
		tmp = tmp * max(x,f[i]);
	}
	//cout <<x << " " << tmp << endl;
	res = max(res, tmp);
	return 1;
}

double bs( double l, double r ){
	double mid;
	res = 0;
	for ( int i = 0; i < 1000; i++ ){
		mid = (l+r)/2;
		if ( can(mid) ) l = mid;
		else r = mid;
	}
	return res;
}

int main(){
	
	freopen("out.txt","w",stdout);
	scanf("%d",&tc);
	for ( int t = 1; t <= tc; t++ ){
		scanf("%d%d",&n,&k);
		scanf("%lf",&U);
		for ( int i = 0; i < n; i++ ) scanf("%lf",&f[i]);
		printf("Case #%d: %.9lf\n",t,bs(0,1));
	}
	
	fclose(stdout);
	return  0;
}
