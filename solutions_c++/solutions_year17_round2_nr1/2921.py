#include"bits/stdc++.h"
#define fast ios_base::sync_with_stdio(false);cin.tie(0);
#define pb push_back
#define mp make_pair
#define ll long long int
#define vi vector<int>
#define vii vector<pair< int,int> >
#define pii pair<int,int>
#define plli pair<ll,ll>
#define ff first
#define ss second
#define MOD 1000000007
using namespace std;
int main()
{
	fast;
	int t=1,cases=1;
	cin>>t;
	while(t--)
	{
		int i,j;
		long long int d,n;
		cin>>d>>n;
		double minn=0;
		double answer=d;
		for(i=0;i<n;i++)
		{
			int x,y;
			cin>>x>>y;
			double speed=(d-x)/y;
			minn=max(speed,minn);
		//	cout<<speed<<endl;	
		}
		 answer=min(1.0*d,1.0*d/minn);
		
		
		
		
		
		
		cout<<"Case #"<<cases<<": "<< setprecision(7)<< fixed <<answer<<endl;
		cases++;
	}
}		
		
		