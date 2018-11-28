#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
bool increasing(vector<int> n)
{
	int i,j=n.size();
	for(i=0;i<j-1;i++)
	{
		if(n[i]<=n[i+1]);
		else
			return false;
	}
	return true;
}
void display(vector<int> n)
{
	int i;
	for(i=0;i<n.size();i++)
	{
		cout<<n[i];
	}
	cout<<"\n";
}
vector<int> getAns(vector<int> n)
{
	if(n.size()<1)
		return n;
	if(increasing(n))
		return n;
	int i=0;
	while(i<=n.size()-1)
	{
		if(n[i]<=n[i+1])
			i++;
		else
		{
			n[i]=n[i]-1;
			i++;
			while(i!=n.size())
			{
				n[i]=9;
				i++;
			}
		}
	}
	if(increasing(n))
		return n;
	else 
		return getAns(n);
}
int main()
{ 
	int t;
	std::cin >> t;
	int i;
	for(i=0;i<t;i++)
	{
		string n;
		cin >> n;
		vector<int> t;
		int j;
		bool flag1=true;
		for(j=0;j<n.size();j++)
		{
			
			int temp= n.at(j)-'0';
			if(flag1 && temp==0);
			else
				flag1=false;
			if(!flag1)
				t.push_back(temp);
		}
		cout<<"Case #"<<i+1<<": ";
		vector<int> k = getAns(t);
		//display(k);
		bool flag=true;
		for(j=0;j<k.size();j++)
		{
			if(flag && k[j]==0);
			else
				flag=false;
			if(!flag)
				cout<<k[j];
				
		}
		cout<<"\n";
	}
	return 0;
}
