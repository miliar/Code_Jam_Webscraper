
#include <iostream>
#include<bits/stdc++.h>
using namespace std;

class color{
	public:
	int x;
	int y;
	string z;
	color(int a=0,int b=0)
	{
		x=a;
		y=b;
	}
};
bool operator<(color const & a, color const & b)
{
    return a.x < b.x;
}
int main() {
	int t,i;
	cin>>t;;
	for(i=1;i<=t;i++)
	{
		int n,r,o,y,g,b,v,count=0;
		color c[6];
		string s;
		//cin>>n>>r>>o>>y>>g>>b>>v;
		cin>>n>>c[0].x>>c[1].x>>c[2].x>>c[3].x>>c[4].x>>c[5].x;
		c[0].y=0;c[1].y=1;c[2].y=2;c[3].y=3;c[4].y=4;c[5].y=5;
		c[0].z="R"; c[1].z="O";c[2].z="Y";
		c[3].z="G"; c[4].z="B";c[5].z="V";

		sort(c,c+6);
		if( c[4].x+c[3].x <c[5].x)
		{
			cout<<"Case #"<<i<<": IMPOSSIBLE\n";
			continue;
		}
		int j=0;
		while(count<n)
		{
			if(c[3].x>0)
			{
				s.insert(j++,c[3].z);
				c[3].x--;
				s.insert(j++,c[4].z);
				c[4].x--;
				count+=2;
			}
			else
			{
				if(c[4].x>0)
				{
					s.insert(j++,c[5].z);
					c[4].x--;
					s.insert(j++,c[4].z);
					c[5].x--;
					count+=2;
				}
				else
				{
					j=0;
					while(c[5].x>0 && count<n)
					{
						s.insert(j++,c[5].z);
						c[5].x--;
						count+=1;
						j+=1;
					}
				}
			}
		}
		cout<<"Case #"<<i<<": "<<s<<"\n";
	}
	return 0;
}

