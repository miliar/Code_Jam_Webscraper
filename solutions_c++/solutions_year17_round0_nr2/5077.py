#include<bits/stdc++.h>
using namespace std;

vector<unsigned long long> sortlarge(unsigned long long n)
{
		vector<unsigned long long>a;
		unsigned long long temp=n;
		while(temp)
		{
			a.push_back(temp%10);
			temp/=10;
		}
		reverse(a.begin(),a.end());
		int p=0;
		for(unsigned long long i=0;i<a.size();)
		{
			if(i==0)
			{
				i++;
				continue;
			}
			if( a[i]==0||a[i]<a[i-1] ) 
			{
				for(int j=i;j<a.size();j++)
				{
					a[j]=9;
					p=1;
				}
				a[i-1]-=1;
				if(a[i-1]==0)
				{
					i--;
					continue;
				}
				else if(i-2>=0 && a[i-1]<a[i-2])
				{
					i--;
					continue;
				}
				else
				{
					if(p)
						break;
				}
			}
			else if(p)
				break;
			i++;
		}
return a;
}
int main()
{
	int t;
	cin>>t;
	int count=1;
	while(t--)
	{
		unsigned long long n;
		cin>>n;
		vector<unsigned long long> m;
		m=(sortlarge(n)); 	
		cout<<"Case #"<<count<<": ";	
		for(int i=0;i<m.size();i++)
		{
			if(m[i]!=0)
				cout<<m[i];
		}
		cout<<"\n";
		count++;
		//for(int i=0;i<m.size();i++)
		//	cout<<m[i];
	}
}




		
