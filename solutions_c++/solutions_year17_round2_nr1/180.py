#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<map>
#include<cmath>
#define ll long long
using namespace std;
int t;
int k[1100],s[1100],n,d;
double x,y,z;
int fail(double p){
	for (int i=1;i<=n;i++){
		if (fabs(p-s[i])<1e-9) continue;
		double t=k[i]/(p-s[i]);
		if (t>=0 && t*p<d) return 1;
	}
	return 0;
}
int main(){
	scanf("%d",&t);
	for (int I=1;I<=t;I++){
		scanf("%d%d",&d,&n);
		for (int i=1;i<=n;i++){
			scanf("%d%d",&k[i],&s[i]);
		}
		x=0;y=1e18;
		for (int i=1;i<=4000;i++){
			z=(x+y)/2;
			if (fail(z)) y=z;
			else x=z;
		}
		printf("Case #%d: %.9f\n",I,z);
	}
    return 0;
}

