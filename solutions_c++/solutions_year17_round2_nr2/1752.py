#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <set>
#include <string>
#include <iomanip>
using namespace std;
const int MAX_N=2000;
const int INF=1000000000;
string ans,s;
int rec(int i,int x[],int n)
{
	if (i+1==n)
	{
		if (s[0]!=s[n-1])
		{
			ans=s;
			return 1;
		}
		return 0;
	}
	if (s[i]=='R')
	{
		if (x[1]==x[2]&&x[1]>0)
		{
			x[1]--;
			s.push_back('Y');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[1]++;

			x[2]--;
			s.push_back('B');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[2]++;
		}
		if (x[1]>x[2])
		{
			x[1]--;
			s.push_back('Y');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[1]++;
		}
		if (x[2]>x[1])
		{
			x[2]--;
			s.push_back('B');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[2]++;
		}
	}
	if (s[i]=='Y')
	{
		if (x[0]==x[2]&&x[0]>0)
		{
			x[0]--;
			s.push_back('R');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[0]++;

			x[2]--;
			s.push_back('B');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[2]++;
		}
		if (x[0]>x[2])
		{
			x[0]--;
			s.push_back('R');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[0]++;
		}
		if (x[2]>x[0])
		{
			x[2]--;
			s.push_back('B');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[2]++;
		}
	}
	if (s[i]=='B')
	{
		if (x[1]==x[0]&&x[1]>0)
		{
			x[1]--;
			s.push_back('Y');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[1]++;

			x[0]--;
			s.push_back('R');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[0]++;
		}
		if (x[1]>x[0])
		{
			x[1]--;
			s.push_back('Y');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[1]++;
		}
		if (x[0]>x[1])
		{
			x[0]--;
			s.push_back('R');
			if (rec(i+1,x,n)==1)
				return 1;
			s.pop_back();
			x[0]++;
		}
	}
	return 0;
}
int main() 
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
	int q1,n,r,o,y,g,b,v,i,z;
	cin>>q1;
	for (int q=0;q<q1;q++)
	{
		cin>>n>>r>>o>>y>>g>>b>>v;
		s.clear();
		ans.clear();
		int x[3];
		x[0]=r;
		x[1]=y;
		x[2]=b;
		if (b>r+y||r>b+y||y>r+b)
		{
			cout<<fixed<<setprecision(15)<<"Case #"<<q+1<<": IMPOSSIBLE"<<endl;
			continue;
		}
		if (x[0]>0)
		{
			x[0]--;
			s.push_back('R');
			z=rec(0,x,n);
			s.pop_back();
			x[0]++;
			if (z==1)
			{
				cout<<fixed<<setprecision(15)<<"Case #"<<q+1<<": "<<ans<<endl;
			}
			else
			{
				cout<<fixed<<setprecision(15)<<"Case #"<<q+1<<": IMPOSSIBLE"<<endl;
			}
			continue;
		}
		if (x[1]>0)
		{
			x[1]--;
			s.push_back('Y');
			z=rec(0,x,n);
			s.pop_back();
			x[1]++;
			if (z==1)
			{
				cout<<fixed<<setprecision(15)<<"Case #"<<q+1<<": "<<ans<<endl;
			}
			else
			{
				cout<<fixed<<setprecision(15)<<"Case #"<<q+1<<": IMPOSSIBLE"<<endl;
			}
			continue;
		}
		if (x[2]>0)
		{
			x[2]--;
			s.push_back('B');
			z=rec(0,x,n);
			s.pop_back();
			x[2]++;
			if (z==1)
			{
				cout<<fixed<<setprecision(15)<<"Case #"<<q+1<<": "<<ans<<endl;
			}
			else
			{
				cout<<fixed<<setprecision(15)<<"Case #"<<q+1<<": IMPOSSIBLE"<<endl;
			}
			continue;
		}
	}
	return 0;
}