#include<algorithm>
#include<cstdio>
#include<cmath>
using namespace std;
int need[55];
int n,m;
int a[55][55],pnt[55];
int main(){
	int _,t;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		scanf("%d%d",&n,&m);
		for(int i=0; i<n; i++)
			scanf("%d",&need[i]);
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++)
				scanf("%d",&a[i][j]);
			sort(a[i],a[i]+m);
			pnt[i] = 0;
		}
		int res = 0;
		for(int run=1; run<=2000000; run++){
			bool flag = false;
			while(1){
				bool fnd = true;
				for(int i=0; i<n; i++){
					long long int lo = (long long int)(ceil(0.9 * run * need[i]) + .5);
					long long int hi = (long long int)(floor(1.1 * run * need[i]) + .5);
					while(pnt[i] < m && a[i][pnt[i]] < lo)pnt[i] ++;
					if(pnt[i] == m){
						flag = true;
						break;
					}
					if(a[i][pnt[i]] > hi)fnd = false;
				}
				if(flag)break;
				if(fnd){
					res++;
					for(int i=0; i<n; i++)
						pnt[i] ++;
				}else
					break;
			}
			if(flag)break;
		}
		printf("Case #%d: %d\n",t,res);
	}
	return 0;
}
