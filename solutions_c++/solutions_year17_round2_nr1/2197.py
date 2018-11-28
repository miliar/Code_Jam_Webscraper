#include <iostream>
using namespace std;
int k[1005],s[1005];
double t[1005];
int main()
{
	int T,n,d,i,j;
	double max,ans;
	cin>>T;

	
	int test=1;
	while(T--)
	{
		cin>>d>>n;
		for(i=0;i<n;i++)
		{
			cin>>k[i]>>s[i];
			t[i]=(double)(d-k[i])/s[i];
		}
		max=t[0];
		for(i=1;i<n;i++)
		{
			if(t[i]>max)
			{
				max=t[i];
			}	
		}
		ans=d/max;
		printf("Case #%d: %.6lf\n",test,ans);
		test++;
		
	}
	return 0;
}