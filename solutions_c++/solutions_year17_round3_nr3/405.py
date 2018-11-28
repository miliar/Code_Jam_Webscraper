#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<queue>
using namespace std;
const int N = 500;
const double eps = 1e-9;
int n,m;
double all;
double a[N];

bool cmp(double a,double b)
{return a<b;}

int main()
{
	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.out","w",stdout);
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		cin>>n>>m;
		cin>>all;
		double tot=1.0*all;
		for(int i=1;i<=n;i++) {cin>>a[i];tot+=a[i];}
		tot/=n;
		sort(a+1,a+1+n,cmp);
		n++;
		a[n]=1.0;
		for(int i=1;i<n;i++)
		{
			double x = a[i+1]-a[i];
			if(i*x>all) 
			{
				for(int j=1;j<=i;j++) a[j]=a[i]+all/i;all=0;
			}
			else 
			{
				for(int j=1;j<=i;j++) a[j]=a[i+1];
				all -= i*x;
			}
			if(all<eps) break;
		}
		
		double ans=1.0;
		for(int i=1;i<=n;i++) 
		{
		//	printf("%.4lf ",a[i]);
			ans*=a[i];
		}
		printf("Case #%d: %lf\n",tt,ans);
	}
}
