#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<cmath>
using namespace std;

typedef long long ll;

int k,i,j,a[11111],b[11111];

int main(){
	//freopen("1.in","r",stdin);freopen("1.out","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	for(;T;T--){
		printf("Case #%d: ",++ca);
			int D,n;
			scanf("%d%d",&D,&n);
			//printf("%d %d\n",D,n);
			double l,r;

			for(int i=1;i<=n;i++)
			{
				scanf("%d%d",&a[i],&b[i]);
			}
			/*
			if(ca==40){
				printf("no!%d\n",n);
				for(int i=1;i<=n;i++)printf("%d %d\n",a[i],b[i]);
			}
			*/
			l=1e-7,r=1.0*D/((1.0*D-a[1])/b[1]);
			for(int i=1;i<=400;i++){
				double v=(l+r)/2;
				//if(ca==40)printf("%.7lf\n",v);
				double t=D/v;
				bool pd=1;
				for(int i=1;i<=n;i++)
				{
					pd&=(0.0+t*b[i]+a[i] >= D);
				}
				if(pd)l=v;else r=v;
			}
			printf("%.6lf\n",(l+r)/2);
	}

	return 0;
}
