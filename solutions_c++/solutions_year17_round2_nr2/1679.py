#include<bits/stdc++.h>
using namespace std;

ifstream goo;
ofstream gle;

string s,s1;

void solve()
{
	int n,r,o,y,g,b,v,a,x; //red, orange, yellow, green, blue, violet
	goo>>n>>r>>o>>y>>g>>b>>v;
	s.clear();
	s1.clear();
	if(r>=y && r>=b)
	{
		s.push_back('R');
		r--;
		x=1;
	}
	else if(y>=b && y>=r)
	{
		s.push_back('Y');
		y--;
		x=2;
	}
	else 
	{
		s.push_back('B');
		b--;
		x=3;
	}
	while(r>0 || y>0 || b>0)
	{
		a=s.size()-1;
		if(s[a]=='G')
		{
			s.push_back('R');
			r--;
			if(r==-1)
			{
				gle<<"IMPOSSIBLE\n";
				return;
			}
			continue;
		}
		if(s[a]=='O')
		{
			s.push_back('B');
			b--;
			if(b==-1)
			{
				gle<<"IMPOSSIBLE\n";
				return;
			}
			continue;
		}
		if(s[a]=='V')
		{
			s.push_back('Y');
			y--;
			if(y==-1)
			{
				gle<<"IMPOSSIBLE\n";
				return;
			}
			continue;
		}
		if(s[a]=='R')
		{
			if(g>0)
			{
				s.push_back('G');
				g--;
				continue;
			}
			if(y==0 && b==0)
			{
				gle<<"IMPOSSIBLE\n";
				return;
			}
			if(y>b)
			{
				s.push_back('Y');
				y--;
			}
			else if(y==b)
			{
				if(x==2)
				{
					s.push_back('Y');
					y--;
				}
				else
				{
					s.push_back('B');
					b--;
				}
			}
			else
			{
				s.push_back('B');
				b--;
			}
		}
		if(s[a]=='Y')
		{
			if(r==0 && b==0)
			{
				gle<<"IMPOSSIBLE\n";
				return;
			}
			if(r>b)
			{
				s.push_back('R');
				r--;
			}
			else if(r==b)
			{
				if(x==1)
				{
					s.push_back('R');
					r--;
				}
				else
				{
					s.push_back('B');
					b--;
				}
			}
			else
			{
				s.push_back('B');
				b--;
			}
		}
		if(s[a]=='B')
		{
			if(r==0 && y==0)
			{
				gle<<"IMPOSSIBLE\n";
				return;
			}
			if(y>r)
			{
				s.push_back('Y');
				y--;
			}
			else if(y==r)
			{
				if(x==2)
				{
					s.push_back('Y');
					y--;
				}
				else
				{
					s.push_back('R');
					r--;
				}
			}
			else
			{
				s.push_back('R');
				r--;
			}
		}
	}
	if(s[0]==s[s.size()-1])
	{
		gle<<"IMPOSSIBLE\n";
		return;
	}
	/*a=-1;
	for(int i=0; i<s.size()-1; i++)
	{
		if(v>=o && v>=g && v>0)
		{
			if(s[i]=='R' && s[i+1]=='B')
			{
				s1.push_back('V');
				v--;
				if(i+1==s.size()-1) a=1;
				i++;
				continue;
			}
			else if(s[i]=='B' && s[i+1]=='R')
			{
				s1.push_back('V');
				v--;
				if(i+1==s.size()-1) a=1;
				i++;
				continue;
			}
		}
		if(o>=v && o>=g && o>0)
		{
			if(s[i]=='R' && s[i+1]=='Y')
			{
				s1.push_back('O');
				o--;
				if(i+1==s.size()-1) a=1;
				i++;
				continue;
			}
			else if(s[i]=='Y' && s[i+1]=='R')
			{
				s1.push_back('O');
				o--;
				if(i+1==s.size()-1) a=1;
				i++; 
				continue;
			}
		}
		if(g>=v && g>=o && g>0)
		{
			if(s[i]=='B' && s[i+1]=='Y')
			{
				s1.push_back('G');
				g--;
				if(i+1==s.size()-1) a=1;
				i++;
				continue;
			}
			else if(s[i]=='Y' && s[i+1]=='B')
			{
				s1.push_back('G');
				g--;
				if(i+1==s.size()-1) a=1;
				i++; 
				continue;
			}
		}
		s1.push_back(s[i]);
	}
	if(a==-1) s1.push_back(s[s.size()-1]);*/
	gle<<s<<"\n";
	return;
}

int main()
{
	goo.open("C:\\Users\\Mateusz\\Desktop\\Testy\\B-small-attempt1 (1).in");
	gle.open("C:\\Users\\Mateusz\\Desktop\\Testy\\tak.out");
	int t;
	goo>>t;
	for(int i=1; i<=t; i++)
	{
		gle<<"Case #"<<i<<": ";
		solve();
	}
	goo.close();
	gle.close();
	return 0;
}
