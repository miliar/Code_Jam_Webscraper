# include <bits/stdc++.h>

using namespace std;


int main() 
{
	int cases;

	cin>>cases;

	for(int t=1;t<=cases;t++)
	{
		cout<<"Case #"<<t<<":";

		int n,q;
		double dis[100][100],e[100],s[100];
		int u,v;

		cin>>n>>q;

		for(int i=0;i<n;i++)
			cin>>e[i]>>s[i];

		for(int i=0;i<n;i++)
		{
			for(int j=0;j<n;j++)
				cin>>dis[i][j];
		}

		for(int x=0;x<q;x++)
		{
			cin>>u>>v;

			double times[100]={0};

			for(int i=1;i<n;i++)
				times[i] = 1000000000000000ll;

			//to change
			for(int i=0;i<n;i++)
			{
				double travelled = 0;
				for(int j=i+1;j<n;j++)
				{
					travelled += dis[j-1][j];
					double ct = (travelled/s[i]);

					if(travelled <= e[i])
					{
						times[j] = min(times[j],times[i]+ct);
					}
					else
						break;
				}
			}

			printf(" %.8f", times[n-1]);
		}

		cout<<endl;
	}

	return 0;
}