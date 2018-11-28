#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mp make_pair
typedef long long ll;
int n,m,d;
int A[100010];
int B[100010];
int main()
{
	int i,j,x;
	int t,temp;
	scanf("%d",&t);
	temp=t;
	while(t--)
	{
		
		double mx=0;
		scanf("%d%d",&d,&n);
		for(i=0;i<n;i++)
			scanf("%d%d",&A[i],&B[i]);		
		for(i=0;i<n;i++)
		{
			mx=max(mx,(double)(d-A[i])/(double)B[i]);
		}
		printf("Case #%d: ",temp-t);
		printf("%f\n",d/(double)mx);
	}
	return 0;
}
