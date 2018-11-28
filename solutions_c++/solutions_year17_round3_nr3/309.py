#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>

using namespace std;
#define Eps 1e-9

int n, m, Case;
double p[1010], U;

int main(){
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.out","w",stdout);
	scanf("%d",&Case);
	for (int CASE=1; CASE<=Case; CASE++){
		scanf("%d%d",&n,&m);
		scanf("%lf",&U);
		for (int i=0; i<n; i++)
			scanf("%lf",&p[i]);
		sort(p, p+n);
		for (int i=0; i<n-1; i++){
			if ((p[i+1]-p[i])*(i+1) > U){
				for (int j=0; j<=i; j++)
					p[j] += U/(i+1);
				U = 0;
				break;
			}
			U -= (p[i+1]-p[i])*(i+1);
			for (int j=0; j<=i; j++)
				p[j] = p[i+1];
			
		}
		if (U > Eps){
			for (int i=0; i<n; i++){
				if (p[i]>1) p[i] = 1;
				p[i] += U/n;
			}
		}
		double ans = 1;
		for (int i=0; i<n; i++)
			ans *= p[i];
		printf("Case #%d: %.9lf\n",CASE, ans);
	}
	return 0;
}
