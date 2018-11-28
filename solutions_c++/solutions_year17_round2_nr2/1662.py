#include <bits/stdc++.h>

using namespace std;

typedef long long ll;



void apply(string &s, ll &i, char c, ll r)
{
	for(; r > 0; i+=2, r--)
	{
		if(i >= s.size())
		{
			i = 1;
		}
		s.at(i % s.size()) = c;
		//cout << s << endl;
	}
}


int main()
{
	ll casses;
	cin >> casses;
	for(int caseNum = 0; caseNum < casses; caseNum++)
	{
		ll n,r,o,y,g,b,v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		string sol;
		
		/*bool goodSol = true;
		if(r > y + b)
		{
			goodSol = false;
		}
		if(y > r + b)
		{
			goodSol = false;
		}
		if(b > y + r)
		{
			goodSol = false;
		}
		if(goodSol)
		{
			cout << "Good ";
		}else
		{
			cout << "Bad ";
		}*/
		
		
		
		for(int i = 0; i < n; i++)
		{
			sol += 'X';
		}
		ll i = 0;
		
		if(r >= y && r >= b)
		{
			apply(sol, i, 'R', r);
			if(y >= b)
			{
				apply(sol, i, 'Y', y);
				apply(sol, i, 'B', b);
			}else
			{
				apply(sol, i, 'B', b);
				apply(sol, i, 'Y', y);
			}
		}
		else if(y >= r && y >= b)
		{
			apply(sol, i, 'Y', y);
			if(r >= b)
			{
				apply(sol, i, 'R', r);
				apply(sol, i, 'B', b);
			}else
			{
				apply(sol, i, 'B', b);
				apply(sol, i, 'R', r);
			}
		}
		else if(b >= y && b >= r)
		{
			apply(sol, i, 'B', b);
			if(y >= r)
			{
				apply(sol, i, 'Y', y);
				apply(sol, i, 'R', r);
			}else
			{
				apply(sol, i, 'R', r);
				apply(sol, i, 'Y', y);
			}
		}
		
		/*int i = 0;
		for(; r > 0; i+=2, r--)
		{
			if(i >= sol.size())
			{
				i = 1;
			}
			sol.at(i % sol.size()) = 'R';
			cout << sol << endl;
		}
		
	
		for(; y > 0; i+=2, y--)
		{
			if(i >= sol.size())
			{
				i = 1;
			}
			sol.at(i % sol.size()) = 'Y';
			cout << sol << endl;
		}
		
		
		for(; b > 0; i+=2, b--)
		{
			if(i >= sol.size())
			{
				i = 1;
			}
			sol.at(i % sol.size()) = 'B';
			cout << sol << endl;
		}*/
		
		
		
		
		bool good = true;
		for(int i = 0; i < sol.size(); i++)
		{
			if(sol.at(i) == sol.at((i + 1) % sol.size()))
			{
				good = false;
				cout << "Case #" << caseNum + 1 << ": " << "IMPOSSIBLE" << endl;
				//cout << sol << endl;
				break;
			}
		}
		if(good)
		{
			cout << "Case #" << caseNum + 1 << ": " << sol << endl;
		}
	}
	return 0;
}










