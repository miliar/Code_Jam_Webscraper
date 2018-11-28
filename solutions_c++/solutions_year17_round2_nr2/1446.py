#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <iomanip>
using namespace std;

int main()
{
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		int r,o,y,g,b,v;
		cin>>r>>o>>y>>g>>b>>v;
		int count=0;
		if(r>0) count++;
		if(y>0) count++;
		if(b>0) count++;
		int s=r+y+b;
		int m=max(r,y);m=max(m,b);
		cout<<"Case #"<<i+1<<": ";
		if(m>s-m) cout<<"IMPOSSIBLE"<<endl;
		else
		{
			int c1,c2,c3;
			char c1c,c2c,c3c;
			if(r>=y && y>=b)
			{
				c1=r;
				c2=y;
				c3=b;
				c1c='R';
				c2c='Y';
				c3c='B';
			}
			if(y>=r && r>=b)
			{
				c2=r;
				c1=y;
				c3=b;
				c2c='R';
				c1c='Y';
				c3c='B';
			}
			if(r>=b && b>=y)
			{
				c1=r;
				c3=y;
				c2=b;
				c1c='R';
				c3c='Y';
				c2c='B';
			}
			if(y>=b && b>=r)
			{
				c3=r;
				c1=y;
				c2=b;
				c3c='R';
				c1c='Y';
				c2c='B';
			}
			if(b>=y && y>=r)
			{
				c3=r;
				c2=y;
				c1=b;
				c3c='R';
				c2c='Y';
				c1c='B';
			}
			if(b>=r && r>=y)
			{
				c2=r;
				c3=y;
				c1=b;
				c2c='R';
				c3c='Y';
				c1c='B';
			}//cout<<c1c<<" "<<c2c<<" "<<c3c<<" ";
			vector<char> v;
			for(int j=0;j<c1;j++)
			{
				v.push_back(c1c);
				v.push_back('.');
				v.push_back('.');
			}
			int l=0;
			for(int j=0;l<c2;j+=3)
			{
				v[j+1]=c2c;
				l++;
			}
			int p=v.size();
			l=0;
			for(int j=0;l<c3;j+=3)
			{
				v[p-j-1]=c3c;
				l++;
			}
			for(int j=0;j<p;j++)
			{
				if(v[j]!='.')
					cout<<v[j];
			}
			cout<<endl;

		}

	}
	
	
}
	
