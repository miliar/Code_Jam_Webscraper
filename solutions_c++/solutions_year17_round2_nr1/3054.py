#include <bits/stdc++.h>
#define N 1005
using namespace std;
typedef pair<int,int> ii;
#define fi first
#define se second
int d,n;
double max_t;
int main(){
	freopen("A-large.in","r",stdin); freopen("A.out","w",stdout);
	int t; scanf("%d",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%d %d",&d,&n);
		max_t=0;
		for(int i=0;i<n;i++) {
			int p,v; scanf("%d %d",&p,&v);
			max_t=max(max_t,double(d-p)/v);
		}
		printf("Case #%d: %lf\n",tc,d/max_t);
	}
}
