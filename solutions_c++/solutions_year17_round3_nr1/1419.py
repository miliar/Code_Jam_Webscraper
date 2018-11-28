#include<bits/stdc++.h>
using namespace std;
#define PI 3.14159265358979323
#define maxs 2000
#define pb push_back
#define mp make_pair


double height[maxs];
double radius[maxs];

double dp[maxs][maxs];

bool func(pair<double,double> a, pair<double,double> b)
{
	if(a.first>b.first)return 1;
	if(a.first==b.first and a.second>=b.second)return 1;
	return 0;
}

int main()
{
	int t;
	cin>>t;
	int cased=1;
	while(t--)
	{
		int n,k;
		cin>>n>>k;
		vector< pair<double,double> > arr;
		vector<double> mul;
		
		for(int i=0;i<n;i++)
		{	cin>>radius[i]>>height[i];
			arr.pb(mp(radius[i]*height[i],i));
		}
		
		sort(arr.begin(),arr.end(),func);
		
		double ans=0;
		for(int i=0;i<n;i++)
		{	double maxrad=-1;
			double sum=0;
			int count=0;
			maxrad = max(maxrad,radius[i]);
			for(int j=0;j<arr.size();j++)
			{	int ind = arr[j].second;
				if(count==k-1)break;
				maxrad =  max(maxrad,radius[ind]);
				if(ind!=i)
				{	count++;
					sum+=arr[j].first;
				}
			}
			if(count+1==k)
			{	sum+=(radius[i]*height[i]);
				sum=sum*2*PI;
				sum+=PI*maxrad*maxrad;
				if(sum>=ans)
					ans=sum;
			}
		}
		
		cout<<"Case #"<<cased<<": ";
		printf("%.9f\n",ans);
		cased++;
		
		}
}
