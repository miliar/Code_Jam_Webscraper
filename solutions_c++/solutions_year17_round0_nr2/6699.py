#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
void check(vector<int>&v,int i)
{
	
	int l=v.size()-1;
	if(i==l)
	{
		v[i]--;
		for(int j=i-1;j>=0;j--)
		{
			v[j]=9;
		}
		return;
	}
	if(v[i]==v[i+1])
	{
		v[i]--;
		if(v[i]==0)
			v[i]=9;
		check(v,i+1);
	}
	else if(v[i]>v[i+1])
		v[i]=v[i]-1;
	return;
}
int main()
{
	ifstream fin("B-small-attempt0.doc",ios::in);
	ofstream fout("a.txt",ios::out);
	int t;
	char ch;
	fin>>t;
	fin.get(ch);
	int w=1;
	while(t--)
	{
		vector<int>v;
		long long int k;
		fin>>k;
		fin.get(ch);
		
		while(k)
		{
			int x=k%10;
			v.push_back(x);
			k=k/10;
		}
		for(int i=v.size()-2;i>=0;i--)
		{
			if(v[i+1]<=v[i])
			{

			}
			else
			{
				for(int j=i;j>=0;j--)
					v[j]=9;
				
				check(v,i+1);
			}
		}
		int l=v.size()-1;
		if(v[l]==0)
			l=l-1;
		fout<< "Case #" << w << ": " ;
		for(l;l>=0;l--)
		{
			fout<<v[l];
		}
		fout<<endl;
		w++;
	}
}