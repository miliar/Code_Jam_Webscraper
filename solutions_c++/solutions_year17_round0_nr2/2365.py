#include<bits/stdc++.h>
using namespace std;

bool ck(long long n)
{
	vector<int> vc;

	while(n)
	{
		vc.push_back(n%10);
		n/=10;
	}

	for(int i=vc.size()-2;i>=0;i--)
	{
		if(vc[i]<vc[i+1])
			return false;
	}

	return true;

}

long long gg(long long n)
{
	vector<int> vc;

	while(n)
	{
		vc.push_back(n%10);
		n/=10;
	}	

	vector<int> bc;

	for(int i=vc.size()-1;i>=0;i--) bc.push_back(vc[i]);

		int oo;

	int i;
	
	for(i=1;i<bc.size();i++)
	{
		if(bc[i]<bc[i-1])
		{
			oo=bc[i-1];
			break;
		}
	}

	for(int j=i;j<bc.size();j++)
	{
		bc[j]=oo;
	}

	long long m=0;

	for(int i=0;i<bc.size();i++)
	{
		m=m*10+bc[i];
	}

	return m;
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);


	int t;
	cin>>t;

	long long n;


	for(int trm=1;trm<=t;trm++)
	{
		cout<<"Case #"<<trm<<": ";

		cin>>n;

		long long low= 1;
		long long high= n;

		long long ans;

		while(low<=high)
		{
			
			long long mid = (low+high)/2;

			

			if(ck(mid))
			{
				ans=mid;
				low=mid+1;
			}
			else
			{
				if(gg(mid)<=high)
				{
					low=mid+1;
				}
				else
				{
					high=mid-1;
				}
			}

		}

		cout<<ans<<endl;

	}
}