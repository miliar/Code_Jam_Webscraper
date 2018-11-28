#include<bits/stdc++.h>
using namespace std;
struct elem{
	int st; int sp;	
};

int T,N,D;
elem arr[2000];
double ans;

int main(){
	freopen("cruise.in","r",stdin);
	freopen("cruise.out","w",stdout);
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
		scanf("%d%d",&D,&N);
		ans=-1;
		for (int j=1;j<=N;j++){
			scanf("%d%d",&arr[j].st,&arr[j].sp);
			if (arr[j].sp==0) ans=0;
			double tmp=double(D)/(double(D-arr[j].st)/double(arr[j].sp));
			if (tmp<ans||ans<0) ans=tmp;
		}
		printf("Case #%d: %lf\n",i,ans);
	}
	return 0;
}
