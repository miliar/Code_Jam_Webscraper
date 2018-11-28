#include<cstdio>
using namespace std;
double test()
{
	int n,d;
	scanf("%d%d",&d,&n);
	double max_time=0.0;
	for(int i=0;i<n;i++)
	{
		int k,s;
		scanf("%d%d",&k,&s);
		double time=(d-k)*1.0/s;
		if(time>max_time)max_time=time;
	}
	return d/max_time;

}
int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		auto res=test();
		printf("Case #%d: %.6f\n",i,res);
	}
}
