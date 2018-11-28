#include <cstdio>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <cstring>
#include <vector>
#include <map>
#include <set>

using namespace std;

#define X first
#define Y second

const double eps=1e-8;

double d,k[1111],s[1111];
int TT,n;
double l,r,mid;

bool check(double spd){
	for (int i=1;i<=n;++i){
		if	(spd < s[i])	continue;
		double t = k[i] / (spd - s[i]);
		if	(t * spd < d)	return false;
	}
	return true;
}

int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&TT);
	for (int T=1;T<=TT;++T){
		cin >>d >>n;
		//printf("%d %.5f\n",n,d);
		for (int i=1;i<=n;++i){
			cin >>k[i] >>s[i];
			//printf("%.5f %.5f\n",k[i],s[i]);
		}
		l = 0; r = 1e16 + 10;
		
		for(int p = 500;p;--p){
			mid = (l + r) / 2.;
			if (check(mid)) l = mid;
			else r = mid;
		} 
		printf("Case #%d: %.6f\n",T,l);
	} 
	return	0;
}

