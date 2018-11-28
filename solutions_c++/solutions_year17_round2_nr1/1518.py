#include<bits/stdc++.h>
#define sd(x) scanf("%d",&x)
using namespace std;

int main(){
	freopen("cj.in","r",stdin);
	freopen("cj.out","w",stdout);
	int t;
	sd(t);
	for(int te=1;te<=t;te++){
		int d,n,s,k;
		sd(d);sd(n);
		double mx,tmp;
		mx=0.0;
		for(int i=0;i<n;i++){
			sd(k);sd(s);
			tmp=(double)(d-k)/(double)(s);
			mx=max(mx,tmp);
		}
		double res=double(d)/mx;
		printf("Case #%d: %.10lf\n",te,res);
	}
	return 0;
}
