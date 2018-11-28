#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() 
{
	int t,i,j;
	bool flag;
	long long int n;
	cin>>t;
	vector<int> v;
	for(j=1;j<=t;j++)
	{
		
		flag=0;
		cout<<"Case #"<<j<<": ";
		cin>>n;
		while(n>0)
		{
			v.push_back(n%10);
			n/=10;
		}
		reverse(v.begin(),v.end());
		for(i=0;i<v.size()-1;i++)
		{
			if(v[i]>v[i+1])
			{
				if(v[i]==1)
					flag=1;
				else
				{
					j=i;
					while(j>0&&(v[j]<=v[j-1]))
						j--;
					v[j]--;
					while(j++<v.size()-1)
						v[j]=9;
				}
				break;
			}
		}
		if(flag)
		{
			for(i=0;i<v.size()-1;i++)
				cout<<"9";
		}
		else
			for(i=0;i<v.size();i++)
				cout<<v[i];
		cout<<"\n";
		v.clear();
	}
	return 0;
}
