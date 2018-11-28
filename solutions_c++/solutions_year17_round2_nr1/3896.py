#include <bits/stdc++.h>
typedef long long ll;
#define MOD 1000000007
using namespace std;
bool a[100005];
int main()
{
	ios::sync_with_stdio(false), cin.tie(0);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		int d,n;
		cin>>d>>n;
		pair<int,int>p[n];
		for(int i=0;i<n;i++)
		{
			cin>>p[i].first>>p[i].second;
		}
		sort(p,p+n);
		cout<<"Case #"<<t<<": ";
		if(n==1)
		{
			double a=(d-p[0].first)/(double)p[0].second;
			double v=d/(double)a;
			cout<<fixed<<setprecision(6)<<v<<endl;
			continue;
		}

		double st=0,e=1e18,m;
		double mn=1e18;
		for(int i=0;i<1000;i++)
		{
			m=(st+e)/2.0;
			pair<double,double>s[n];
			for(int j=0;j<n;j++)
			{
				s[j].first=(double)p[j].first+(double)(m*(double)p[j].second);
			}
			int c=1;
			for(int j=n-2;j>=0;j--)
			{
				if(s[j+1].first<=s[j].first)
				{
					s[j].first=s[j+1].first;
					c++;
				}
			}
			double y=-1;

			for(int j=0;j<n;j++)
			{
				if(s[j].first<=d)
				{
					y=s[j].first;

				}
			}
//			if(c==n)
//			{
//				e=m;
//								mn=min(mn,m);
//			}
//			else
//			{
//				st=m;
//			}
			bool k=false;
			for(int j=0;j<n;j++)
			{
				if(s[j].first<=d&&s[j].first!=y)
				{
					k=true;
					break;
				}
			}
			if(y==-1)
			{
				st=m;
				continue;
			}
			if(k)
			{
				st=m;
			}
			else
			{
				e=m;
				mn=min(mn,m);
			}
		}
//		cout<<"mn: "<<mn<<endl;
		if(mn==1e18)
		{
			double a=0;
			for(int i=0;i<n;i++)
			{
				a=max(a,(d-p[i].first)/(double)p[i].second);
			}
			double v=d/(double)a;
			cout<<fixed<<setprecision(6)<<v<<endl;
		}
		else
		{
			pair<double,double>s[n];
			for(int j=0;j<n;j++)
			{
				s[j].first=(double)p[j].first+(double)(mn*(double)p[j].second);
			}
			for(int j=n-2;j>=0;j--)
			{
				if(s[j+1].first<=s[j].first)
				{
					s[j].first=s[j+1].first;
					s[j].second=min(p[j].second,p[j+1].second);
				}
			}
			double y=-1,l=-1;
			for(int j=0;j<n;j++)
			{
				if(s[j].first<=d)
				{
					y=s[j].first;
					l=s[j].second;
				}
			}
			if(y==-1)
			{
				double a=0;
				for(int i=0;i<n;i++)
				{
					a=max(a,(d-p[i].first)/(double)p[i].second);
				}
				double v=d/(double)a;
				cout<<fixed<<setprecision(6)<<v<<endl;
			}
			else
			{
				double a=(d-y)/(double)l;
				double v=d/(double)(mn+a);
				cout<<fixed<<setprecision(6)<<v<<endl;
			}
		}
	}
	return 0;
}


