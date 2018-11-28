#include <bits/stdc++.h>
typedef long long ll;
#define MOD 1000000007
using namespace std;
int main()
{
	ios::sync_with_stdio(false), cin.tie(0);
	freopen("C-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		long long n,k,x,y,a=1,b=1;
		cin>>n>>k;
		vector<pair<long long,long long> > p;
		x=((n-1)/2)+((n-1)%2);
		y=((n-1)/2);
		p.push_back(make_pair(x,a));
		p.push_back(make_pair(y,b));
		while(x!=0&&y!=0)
		{
			if(x==y&&x%2==0)
			{
				y=(x-1)/2;
				x=y+1;
				int temp=a;
				a+=b;
				b+=temp;
			}
			else if(x==y&&x%2==1)
			{
				y=(x-1)/2;
				x=y;
				int temp=a;
				a+=b;
				b+=temp;
			}
			else if(x!=y&&x%2==0)
			{
				y=(x-1)/2;
				x=y+1;
				b+=(a+b);
			}
			else if(x!=y&&x%2==1)
			{
				x=(y-1)/2;
				x++;
				y=x-1;
				a+=(a+b);
			}
			p.push_back(make_pair(x,a));
			p.push_back(make_pair(y,b));
		}
//		for(int i=0;i<p.size();i+=2)
//		{
//			cout<<"<"<<p[i].first<<","<<p[i].second<<"> "<<"<"<<p[i+1].first<<","<<p[i+1].second<<">\n";
//		}

		if(k==1)
		{
			x=n/2;
			y=(n-1)/2;
			cout<<"Case #"<<t<<": ";
			cout<<x<<" "<<y<<"\n";
		}
		else
		{
			long long p2=2;
			int level=0;
			while(p2<=k)
			{
				p2*=2;
				level++;
//				cout<<p2-1<<" "<<level<<"\n";
			}
			level--;
			p2/=2;
			k-=(p2);
			cout<<"Case #"<<t<<": ";
			if(p[level*2].second>k)
			{
				x=p[level*2].first/2;
				y=(p[level*2].first-1)/2;
				cout<<x<<" "<<y<<"\n";
			}
			else
			{
				x=p[level*2+1].first/2;
				y=(p[level*2+1].first-1)/2;
				cout<<x<<" "<<y<<"\n";
			}
		}
	}
	return 0;
}


