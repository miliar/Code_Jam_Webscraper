#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	int ti,t,i,next,prev;
	cin>>t;
	for(ti = 1;ti<=t;ti++)
	{
		int n;
		cin>>n;
		int r,o,y,g,b,v;
		cin>>r>>o>>y>>g>>b>>v;
		if((r == 0 || y == 0 || b == 0) && (n&1) && (n>1))
		{
			cout<<"Case #"<<ti<<": IMPOSSIBLE\n";
			continue;
		}
		if(n == 1)
		{
			if(r == 1)
			{
				cout<<"Case #"<<ti<<": R\n";
				continue;
			}
			if(y == 1)
			{
				cout<<"Case #"<<ti<<": Y\n";
				continue;
			}
			if(b == 1)
			{
				cout<<"Case #"<<ti<<": B\n";
				continue;
			}
		}
		if(r>n/2 || y>n/2 || b>n/2)
		{
			cout<<"Case #"<<ti<<": IMPOSSIBLE\n";
			continue;
		}
		pair<int,char> arr[7];
		arr[1] = make_pair(r,'R');
		arr[2] = make_pair(y,'Y');
		arr[3] = make_pair(b,'B');
		sort(arr+1,arr+4);
		cout<<"Case #"<<ti<<": ";
		if(arr[1].first == 0)
		{
			for(i = 1;i<=n;i+=2)
			{
				cout<<arr[2].second;
				cout<<arr[3].second;
			}
		}
		else
		{
			//cout<<arr[1].second<<", "<<arr[2].second<<" "<<arr[3].second<<"\n";
			next = 2;
			int count = 0;
			for(;count<n;)
			{
				if(next == 1)
				{
					if(arr[1].first>0)
					{
						cout<<arr[1].second;
						arr[1].first--;
						count++;
					}
					prev = 1;
					next = 3;
				}
				else if(next == 2)
				{
					if(arr[2].first>0)
					{
						cout<<arr[2].second;
						arr[2].first--;
						count++;
					}
					if(arr[2].first<arr[1].first)
					{
						prev = 2;
					}
					else
					{
						prev = 1;
					}
					next = 3;
				}
				else
				{
					if(arr[3].first>0)
					{
						cout<<arr[3].second;
						arr[3].first--;
						count++;
					}
					if(prev == 1)
					{
						next = 2;
					}
					else
					{
						next = 1;
					}
				}
			}
		}
		cout<<endl;
	}
}
