#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
#define pi 3.141592654

		
int main()
{
//freopen("3.in","r",stdin);
//freopen("3.out","w",stdout);
	int T;
	scanf("%d",&T);
	int t;
	for(int t = 1; t < T+1; t++)
	{
		printf("Case #%d: ",t);
		int n,k;
		scanf("%d %d",&n, &k);
		
		double u;
		scanf(" %lf",&u);
		double a[100];
		double sum = 0, rem =0;
		for(int i = 0; i < n; i++)
		{
			scanf("%lf",&a[i]);
			sum += a[i];
			rem += 1-a[i];
		}
		
		if(rem < u) u = rem;
		sum+=u;
		double ave = (sum)/n;
	//	printf("ave %lf\n",ave);
		int cnt = n;
		double ans = 1;
		for(int i = 0; i < n; i++)
		{
			if(a[i]>ave)
			{
				sum-=a[i];
				cnt--;
				ans *= a[i];
		//		printf("ans %lf %lf\n",ans, a[i]);
			}
		}
		
		ave = sum/cnt;
		for(int i = 0;i < cnt; i++)
		{
			ans*=ave;
		//	printf("ans %lf %lf\n",ans, ave);
		}
		printf("%lf\n",ans);
		
		
	}
}

