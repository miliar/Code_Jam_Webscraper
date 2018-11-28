#include <bits/stdc++.h>
using namespace std;

struct node{
	double r,h;
};

int tc;
node f[1005];
int n,k;
double dp[1005][1005];
bool vs[1005][1005];
double pi = acos(-1);

bool cmp( node a, node b){
	return a.r > b.r;
}

double area( int a ){
	return pi * f[a].r * f[a].r;
}

double height( int a ){
	return 2 * pi * f[a].r * f[a].h;
}

double rek( int p, int k){
	if ( p == n ) {
		if ( k == 0 ) return 0;
		return -1000000000;
	}
	
	double &res = dp[p][k];
	if ( vs[p][k] != 0 ) return res;
	vs[p][k] = 1;
	res = 0;
	res = max(res, rek(p+1,k));
	if ( k > 0 ) {
		res = max(res, rek(p+1,k-1) + height(p) );
	}
	return res;
}

int main(){
	
	freopen("out.txt","w",stdout);
	scanf("%d",&tc);
	for ( int t = 1; t <= tc; t++ ){
		memset(vs,0,sizeof(vs));
		scanf("%d%d",&n,&k);
		for ( int i = 0; i < n; i++ ) scanf("%lf%lf",&f[i].r,&f[i].h);
		sort(f,f+n,cmp);
		f[n].r = f[n].h = 0;
		
		double res = 0;
		for ( int i = 0; i < n; i++ ){
			res = max(res, rek(i+1,k-1) + area(i) + height(i));
		}
		
		printf("Case #%d: %.9lf\n",t,res);
	}
	
	fclose(stdout);
	return  0;
}
