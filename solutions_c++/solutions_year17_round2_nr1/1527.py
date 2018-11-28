#include <bits/stdc++.h>
using namespace std;

const int N = 1010;
int n , t , finish , start , speed;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);

	cin >> t;
	
	for(int q=1;q<=t;q++)
	{
		cin >> finish >> n;
		
		double mx = 0 , ans = 0;
		
		for(int i=0;i<n;i++)
		{
			scanf("%d%d",&start,&speed);
			
			int distance = (finish - start);
			double tt = (double)distance/(double)speed;
			mx = max(mx , tt);
		}
		
		ans = (double)finish / mx;
		
		printf("Case #%d: %.8llf\n",q,ans);
	}
	
	
}