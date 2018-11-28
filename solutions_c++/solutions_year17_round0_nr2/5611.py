#include <iostream>
#include <conio.h>
#include <stdio.h>
#include <string>
#include <vector>
#include <fstream>
using namespace std;

unsigned long long int g(vector<int> v, int u);
int count(unsigned long long int);
unsigned long long int tidy(vector<int>,int);
unsigned long long int f(unsigned long long int,int);
int main()
{
	unsigned long long int x;
	ifstream F("B-large.in");
	ofstream Fil("outpus.txt");
	int T;
	F>>T;
	vector<unsigned long long int> v;
	for(int i=0;i<T;i++)
	{
		F>>x;
		int t=count(x);
		int j=t-1;
		vector<int> digi(t);
		unsigned long long int y=x;
		while(y!=0)
		{
			digi[j]=y%10;
			j--;
			y/=10;
		}
		v.push_back(tidy(digi,t));
	}
	for(int i=0;i<T;i++)
		Fil<<"Case #"<<i+1<<": "<<v[i]<<endl;
	return 0;
	F.close();
	Fil.close();
}
int count(unsigned long long int x)
{
	int i=0;
	while(x!=0)
	{
		i++;x/=10;
	}
	return i;
}
unsigned long long int tidy(vector<int> v,int t)
{
	unsigned long long int x=0;
	int i=0;
	if(v[0]==0) return 0;
	else 
		for(int j=0;j<t;j++)
		{
			if(i<=v[j])
			{
				x=x*10+v[j];
				i=v[j];
			}
			else
			{
				int u=count(x);
				int r=u-1;
				vector<int> digi(u);
				unsigned long long int y=x;
				while(y!=0)
				{
					digi[r]=y%10;
					r--;
					y/=10;
				}
				x=g(digi,u);
				x=f(x,t-j);
				break;
			}
		}
		return x;
}
unsigned long long int f(unsigned long long int x, int y)
{
	for(int i=0;i<y;i++)
		x=x*10+9;
	return x;
}
unsigned long long int g(vector<int> v, int u)
{
	int i=u-2;
	int x=v[i+1];
	while(x==v[i])
	{
		v[i+1]=9;
		i--;
	}
	v[i+1]=x-1;
	unsigned long long t=0;
	for(int j=0;j<u;j++)
		t=t*10+v[j];
	return t;
}
