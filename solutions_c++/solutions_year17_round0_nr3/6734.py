#include<iostream>
#include<vector>
using namespace std;
int main()
{
	int t,x=0;
	cin>>t;
	while(t--)
	{
		long long n,k,max,min,flag=0,i=0;
		cin>>n>>k;
		vector<long long>v;
		v.push_back(n);
		
		while(k--)
		{
			if(v[i]%2==1)
			{
				max=v[i]/2;
				min=max;
			}
			else
			{
				max=v[i]/2;
				if(max>0)
				min=max-1;
				else
				min=max;
			}
		//	cout<<max<<" "<<min<<"\n";
			v.push_back(max);
			long long s=v.size();
			while(v[s-2]<v[s-1])
			{
				long long temp=v[s-2];
				v[s-2]=v[s-1];
				v[s-1]=temp;
				s--;
			}
			v.push_back(min);
			s=v.size();
			while(v[s-2]<v[s-1])
			{
				long long temp=v[s-2];
				v[s-2]=v[s-1];
				v[s-1]=temp;
				s--;
			}
			
			if(v[i]==0)
			{
				flag=1;
				break;
			}
			i++;
			
		}
		x++;
		if(flag==1)
		{
			cout<<"Case #"<<x<<": "<<"0"<<" 0\n";
		}
		else
		{
			cout<<"Case #"<<x<<": ";
			//min=v[v.size()-1];
			//max=v[v.size()-2];
			cout<<max<<" "<<min<<"\n";
		}
	}
	return 0;
}
