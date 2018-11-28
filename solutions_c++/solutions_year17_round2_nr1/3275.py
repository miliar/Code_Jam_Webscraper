#include <bits/stdc++.h>
using namespace std;

int main()
{
	int tst;
	scanf("%d",&tst);
	for(int t=1;t<=tst;t++)
	{
		int n;
		double d,k,s,arr[1001];
		scanf("%lf %d",&d,&n);
		for(int i=0;i<n;i++)
		{
			scanf("%lf %lf",&k,&s);
//			cout<<d-k<<" "<<(d-k)/s<<endl;
			arr[i] = (double) (d-k)/s;
		}
		sort(arr,arr+n);
//		cout<<arr[n-1]<<endl;
		printf("Case #%d: %.6lf\n",t,(double) d/arr[n-1]);
	}
	
}
