#include<bits/stdc++.h>
using namespace std;

vector<unsigned long long> v(unsigned long long n)
{
		vector<unsigned long long>extra;
		unsigned long long x=n,i;
		int j;
		while(x)
		{
			extra.push_back(x%10);
			x/=10;
		}
		reverse(extra.begin(),extra.end());
		int k=0;
		for(i=0;i<extra.size();)
		{
			if(i==0)
			{
				i++;
				continue;
			}
			if( extra[i]==0||extra[i]<extra[i-1] ) 
			{
				for(j=i;j<extra.size();j++)
				{
					extra[j]=9;
					k=1;
				}
				extra[i-1]-=1;
				if(extra[i-1]==0)
				{
					i--;
					continue;
				}
				else if(i-2>=0 && extra[i-1]<extra[i-2])
				{
					i--;
					continue;
				}
				else
				{
					if(k)
						break;
				}
			}
			else if(k)
				break;
			i++;
		}
return extra;
}
int main()
{
	int t;
	cin>>t;
	int s=0;
	while(t--)
	{
		s++;
		unsigned long long n;
		cin>>n;
		vector<unsigned long long> a;
		a=(v(n)); 	
		cout<<"Case #"<<s<<": ";	
		for(int i=0;i<a.size();i++)
		{
			if(a[i]!=0)
				cout<<a[i];
		}
		cout<<"\n";
		
		
	}
}




		
