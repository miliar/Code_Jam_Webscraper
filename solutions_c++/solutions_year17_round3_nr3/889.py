#include <bits/stdc++.h>
using namespace std;
double thing[55];

int main(){
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.txt","w",stdout);
	int t,n,k;
	double u;
	scanf("%d",&t);
	for(int asd=0;asd<t;asd++){
		scanf("%d%d",&n,&k);
		scanf("%lf",&u);
		for(int i=0;i<n;i++) {scanf("%lf",&thing[i]);}
		sort(thing,thing+n);
		int eendex=-1;
		for(int i=1;i<n;i++){
			if(u<i*(thing[i]-thing[i-1])) {eendex=i;break;}
			u-=i*(thing[i]-thing[i-1]);
			for(int j=0;j<i;j++) {thing[j]=thing[i];}
		}
		if(eendex==-1) eendex=n;
		for(int i=0;i<eendex;i++){
			thing[i]+=(u/eendex);
		}
		double arns=1;
		for(int i=0;i<n;i++) {arns*=thing[i];}
		printf("Case #%d: %.9f\n",asd+1,arns);
	}
}
