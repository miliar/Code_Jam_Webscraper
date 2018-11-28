#include <bits/stdc++.h>
using namespace std;
#define M_PI           3.14159265358979323846  /* pi */

vector<long long int> xx(1010);
vector<vector<long long int> >  mem(1010,xx);

long long int calculate(vector<vector<long long int> > &r,int n,int k,int open)
{
	//cout << " n " << n << " k " << k << endl;
	if(k==0)
	{
		return 0;
	}
	else if(n<=0)
	{
	//	cout << " yes" << endl;
		return 0;
	}
	else if(mem[n][k]!=-1)
	{
		return mem[n][k];
	}
	else
	{
		if(open==1)
		{
			 long long int c1 = calculate(r,n-1,k,1);
			 mem[n-1][k] = c1;
			 long long int c2 = calculate(r,n-1,k-1,1);
			 mem[n-1][k-1] = c2;
			 long long int c = max(2ll*r[n][0]*r[n][1]+c2,c1);
			 mem[n][k] = c;

		}
		else if(open==0)
		{
			 long long int c1 = calculate(r,n-1,k,0);
			 mem[n-1][k] = c1;
			 long long int c2 = calculate(r,n-1,k-1,1);
			 mem[n-1][k-1] = c2;
			 long long int c = max(2ll*r[n][0]*r[n][1]+c2+r[n][0]*r[n][0],c1);
			 mem[n][k] = c;
		}
		return mem[n][k];

	}
}



int main()
{	
	int tn,ti;
	scanf("%d",&tn);
	long long int ans=0;
	int n;
	int i,j,k,l;


	for(ti=1;ti<=tn;ti++)
	{
		scanf("%d%d",&n,&k);
		vector<long long int> temp(2);
		vector<vector<long long int> > r(n+1,temp);
		
		for(i=0;i<n+10;i++)
		{
			for(j=0;j<k+10;j++)
			{
				mem[i][j] = -1;
			}
		}
		r[0][0] = 0;
		r[0][1] = 0;
		for(i=1;i<=n;i++)
		{
			scanf("%lld%lld",&r[i][0],&r[i][1]);
			
		}	
		sort(r.begin(),r.end());
		ans = calculate(r,n,k,0);

		//cout << ans << endl;
		
		long double ans1 = ans*M_PI;
		printf("Case #%d: ",ti);
		cout << fixed;
   	 	cout << setprecision(9);
    	cout << ans1 << endl;;
	}
	return 0;
}