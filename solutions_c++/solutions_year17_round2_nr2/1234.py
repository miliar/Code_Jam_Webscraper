#include<cstdio>
#include<string>
#include<iostream>

using namespace std;
		
int main()
{
	int t;
	scanf("%d", &t);
	for(int tt = 1; tt <= t; tt++)
	{
		int n;
		scanf("%d", &n);
		int r, o, y, g, b, v;
		scanf("%d %d %d %d %d %d", &r, &o, &y, &g, &b, &v);
		bool pos = true;
		string s;
		if(r)
		{
			s += 'R';
			r--;
		}
		else if(o)
		{
			s += 'O';
			o--;
		}
		else if(y)
		{
			s += 'Y';
			y--;
		}
		else if(g)
		{
			s += 'G';
			g--;
		}
		else if(b)
		{
			s += 'B';
			b--;
		}
		else if(v)
		{
			s += 'V';
			v--;
		}
		int idx = 0;
		while(pos && idx < n-1)
		{
			if(s[idx] == 'R')
			{
				if(g)
				{
					s += 'G';
					g--;
				}
				else if(b > y)
				{
					s += 'B';
					b--;
				}
				else if(y)
				{
					s += 'Y';
					y--;
				}
				else
				{
					pos = false;
				}
			}
			else if(s[idx] == 'B')
			{
				if(o)
				{
					s += 'O';
					o--;
				}
				else if(r > y)
				{
					s += 'R';
					r--;
				}
				else if(y)
				{
					s += 'Y';
					y--;
				}
				else
				{
					pos = false;
				}
			}
			else if(s[idx] == 'Y')
			{
				if(v)
				{
					s += 'V';
					v--;
				}
				else if(r > b)
				{
					s += 'R';
					r--;
				}
				else if(b)
				{
					s += 'B';
					b--;
				}
				else
				{
					pos = false;
				}
			}
			else if(s[idx] == 'O')
			{
				if(b)
				{
					s += 'B';
					b--;
				}
				else
				{
					pos = false;
				}
			}
			else if(s[idx] == 'G')
			{
				if(r)
				{
					s += 'R';
					r--;
				}
				else
				{
					pos = false;
				}
			}
			else
			{
				if(y)
				{
					s += 'Y';
					y--;
				}
				else
				{
					pos = false;
				}
			}	
			idx++;
		}
		if(pos)
		{
			if(s[idx] == 'R')
			{
				if(s[0] == 'O' || s[0] == 'V')
					pos = false;
				else if(s[0] == 'R')
				{
					if(s[1] == 'Y' && s[2] == 'B')
					{
						s[0] = 'Y';
						s[1] = 'R';
					}
					else if(s[1] == 'B' && s[2] == 'Y')
					{
						s[0] = 'B';
						s[1] = 'R';
					}
					else if(s[idx-1] == 'Y' && s[idx-2] == 'B')
					{
						s[idx] = 'Y';
						s[idx-1] = 'R';
					}
					else if(s[idx-1] == 'B' && s[idx-2] == 'Y')
					{
						s[idx] = 'B';
						s[idx-1] = 'R';
					}
					else
						pos = false;
				}
			}
			else if(s[idx] == 'B')
			{
				if(s[0] == 'G' || s[0] == 'V')
					pos = false;
				else if(s[0] == 'B')
				{
					if(s[1] == 'Y' && s[2] == 'R')
					{
						s[0] = 'Y';
						s[1] = 'B';
					}
					else if(s[1] == 'R' && s[2] == 'Y')
					{
						s[0] = 'R';
						s[1] = 'B';
					}
					else if(s[idx-1] == 'Y' && s[idx-2] == 'R')
					{
						s[idx] = 'Y';
						s[idx-1] = 'B';
					}
					else if(s[idx-1] == 'R' && s[idx-2] == 'Y')
					{
						s[idx] = 'R';
						s[idx-1] = 'B';
					}
					else
						pos = false;
				}
			}
			else if(s[idx] == 'Y')
			{
				if(s[0] == 'O' || s[0] == 'G')
					pos = false;
				else if(s[0] == 'Y')
				{
					if(s[1] == 'B' && s[2] == 'R')
					{
						s[0] = 'B';
						s[1] = 'Y';
					}
					else if(s[1] == 'R' && s[2] == 'B')
					{
						s[0] = 'R';
						s[1] = 'Y';
					}
					else if(s[idx-1] == 'B' && s[idx-2] == 'R')
					{
						s[idx] = 'B';
						s[idx-1] = 'Y';
					}
					else if(s[idx-1] == 'R' && s[idx-2] == 'B')
					{
						s[idx] = 'R';
						s[idx-1] = 'Y';
					}
					else
						pos = false;
				}
			}
			else if(s[idx] == 'G')
			{
				if(s[0] == 'G' || s[0] == 'B' || s[0] == 'Y')
					pos = false;
			}
			else if(s[idx] == 'O')
			{
				if(s[0] == 'O' || s[0] == 'R' || s[0] == 'Y')
					pos = false;
			}
			else
			{
				if(s[0] == 'V' || s[0] == 'R' || s[0] == 'B')
					pos = false;
			}
		}
		printf("Case #%d: ", tt);
		if(!pos)
			printf("IMPOSSIBLE\n");
		else
			cout << s << endl;
	}
	return 0;
}

