#include<bits/stdc++.h>
using namespace std;

bool is_sorted(vector<int> &v)
{
	int n=v.size();

	for(int i=0;i<n-1;i++)
	{
		if(v[i]<v[i+1])
			return false;
	}
	return true;
}


int main()
{
int t;
	cin>>t;
	for(int in=0;in<t;in++)
	{
		unsigned long long int n,m,i;
		cin>>n;

		for(i=n;i>=1;i--)
		{
			vector<int> v(0);
			m=i;
			while(m>0)
			{
				v.push_back(m%10);
				m/=10;
			}

			if(is_sorted(v))
			break;
		}
		cout<<"Case #"<<in+1<<": ";
		
		cout<<i<<endl;
		
	}
return 0;
}