#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("output.txt", "w", stdout);
	ifstream fin;
	fin.open ("input.txt");
	
	int t;
	fin>>t;
	for(int mcase=1;mcase<=t;mcase++)
	{
		int n,r,o,y,g,b,v;
		fin>>n>>r>>o>>y>>g>>b>>v;
		
		if((r+y)<b||(r+b)<y||(y+b)<r)
		{
			cout<<"Case #"<<mcase<<": ";
			cout<<"IMPOSSIBLE"<<endl;
		}
		else
		{
			cout<<"Case #"<<mcase<<": ";
			int x = 0;
			int prev = -1;
			//0 - r, 1 - y, 2 - b
			if(r>y&&r>b)
			{
				if(y>b)
				{
					cout<<"Y";
					prev = 1;
					y--;
				}
				else
				{
					cout<<"B";
					prev = 2;
					b--;
				}
				x++;
			}
			while(x++<n)
			{
				if(r>max(y,b))
				{
					if(prev!=0)
					{
						cout<<"R";
						prev = 0;
						r--;
					}
					else if(y>b)
					{
						cout<<"Y";
						prev = 1;
						
						y--;
					}
					else
					{
						cout<<"B";
						prev = 2;
						b--;
					}
					continue;	
				}
				if(y>b)
				{
					if(prev!=1)
					{
						cout<<"Y";
						prev = 1;
						y--;
					}
					else if(b>r)
					{
						cout<<"B";
						prev = 2;
						b--;
					}
					else
					{
						cout<<"R";
						prev = 0;
						r--;
					}
				}
				else
				{
					if(prev!=2)
					{
						cout<<"B";
						prev = 2;
						b--;
					}
					else if(r>y)
					{
						cout<<"R";
						prev = 0;
						r--;
					}
					else
					{
						cout<<"Y";
						prev = 1;
						y--;
					}
				}
			}
			cout<<endl;
		}
	}
}
