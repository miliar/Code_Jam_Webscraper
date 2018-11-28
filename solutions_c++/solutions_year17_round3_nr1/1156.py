#include <iostream>
#include <vector>
#include <map>
#include <iterator>
#include <functional>
#include <algorithm>
double PI =3.14159265358979323846;
using namespace std;
class sole
{
	int n,k;
	vector<pair<long long,long long> > Z;
	vector<long long> R,H;
	vector<vector<long long> > dp;
	long long ans(int i,int r)
	{
		if(dp[i][r]!=-1)
			return dp[i][r];
		if(r==0)
		{
			dp[i][r]= 0;
			return dp[i][r];
		}	
		long long val=0,ad;
		if(r==k)
			ad=1;
		else
			ad=0;
		for(int I=i+1;I<=n-r+1;I++)
		{
			val=max(val,ans(I,r-1)+2*R[I]*H[I]+R[I]*R[I]*ad);	
		}
		dp[i][r]=val;
		return dp[i][r];
	}
	public:
	sole()
	{
		cin >> n >> k ;
		R.resize(n+1);
		H.resize(n+1);
		Z.resize(n);
		dp.resize(n+1 ,vector<long long>(k+1,-1));
		for(int i=0;i<n;i++)
		{
			cin >> Z[i].first >> Z[i].second;
		}
		sort(Z.begin(),Z.end(),greater<pair<long long,long long> >());
		for(int i=0;i<n;i++)
			R[i+1]=Z[i].first,H[i+1]=Z[i].second;
		long long A=0;
			A=max(A,ans(0,k));
		printf("%.8lf\n",static_cast<double>(A)*PI);

	}
};
int main()
{
	int t;
cin >> t;
for(int i=1;i<=t;i++)
{
	printf("Case #%d: ",i);
	new sole;
}
	return 0;
}