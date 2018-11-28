#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
using namespace std;

const int Maxn=1000;

double D;
int n;

double pos[Maxn+5],spe[Maxn+5];

inline void solve(int T){
	scanf("%lf%d",&D,&n);
	for (int i=1;i<=n;i++) scanf("%lf%lf",&pos[i],&spe[i]);
	double maxTime=0;
	for (int i=1;i<=n;i++) maxTime=max(maxTime,(D-pos[i])/spe[i]);
	printf("Case #%d: %.8f\n",T,D/maxTime);
}

int main(){
	freopen("A-large.in.txt","r",stdin);
	freopen("A.out","w",stdout);
	int T=0;scanf("%d",&T);
	for (int i=1;i<=T;i++) solve(i);
	return 0;
}