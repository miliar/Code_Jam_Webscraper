#include<iostream>
#include<cstdio>
#include<vector>
using namespace std;
vector<int> vec;

vector<int> send(vector<int> v,int size)
{
	int flag=0;
	int k;
	for(int i=size-1;i>0;i--)
	{
		if(v[i]>v[i-1])
		{
			v[i-1]++;
			for(k=0;k<size;k++)
			{
				if(vec[k]<v[k])
				{
					flag=1;
					break;
				}
				else if(vec[k]>v[k])
				{
					break;
				}
			}
			if(flag==1)
			{
				v[i-1]--;
				break;
			}
		}
		
	}
	return v;
}
			



vector<int> f(vector<int> v)
{
	int size=v.size();
	vector<int> v2;
	for(int i=0;i<size-1;i++)
	{
		if(v[i]<v[i+1])
		{
		
		}
		else
		{
			v[i]=v[i]-1;
			v[i+1]=9;
		}
	}
	v2=send(v,size);
	return v2;
}





int main()
{
	freopen("B-small-attempt2.in","r",stdin);
	freopen("output2.out","w",stdout);
	
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		string a;
		cin>>a;
		int j;
		int size=a.length();
		vec.resize(size);
		for(j=0;j<size;j++)
		{
			vec[j]=a[j]-'0';
		}
		
		for(j=0;j<size-1;j++)
		{
			if(vec[j]<=vec[j+1])
			{
				continue;
				
			}
			else
			{
				//flag=0;
				vec=f(vec);
			}
		}
		cout<<"Case #"<<i+1<<": ";
		for(int ij=0;ij<size;ij++)
		{
			if(ij==0&&vec[ij]==0)
			{
				continue;
			}
			cout<<vec[ij];
		}
		cout<<endl;
	}
}
