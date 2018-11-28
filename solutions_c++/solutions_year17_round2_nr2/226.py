
#include <iostream>
#include <string>
#include <cmath>
#include <bitset>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
double eps = 1e-15;

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		int N, R, O, Y, G, B, V;
		cin >> N >> R >> O >> Y >> G >> B >> V;
		string x = "";
		char tie;
		B -= O;
		Y -= V;
		R -= G;
		if (1 == 1)
		{
			int most = max(R, max(Y, B));
			if (most == 0)
			{
				tie = 'R';
			}
			else if (R == most)
			{
				x += 'R';
				R--;
				tie = 'R';
			}
			else if (Y == most)
			{
				x += 'Y';Y--; tie = 'Y';
			}
			else
			{
				x += 'B';B--; tie = 'B';
			}
		}
		int k = x.length();
		while (R>0||B>0||Y>0)
		{
			if (x[k - 1] == 'R')
			{
				if (Y > B)
				{
					x += 'Y';
					Y--;
				}
				else if (B > Y)
				{
					x += 'B';
					B--;
				}
				else if (tie == 'Y')
				{
					x += 'Y';
					Y--;
				}
				else
				{
					x += 'B';
					B--;
				}
			}
			if (x[k - 1] == 'Y')
			{
				if (R > B)
				{
					x += 'R';
					R--;
				}
				else if (B > R)
				{
					x += 'B';
					B--;
				}
				else if (tie == 'R')
				{
					x += 'R';
					R--;
				}
				else
				{
					x += 'B';
					B--;
				}
			}
			if (x[k - 1] == 'B')
			{
				if (Y > R)
				{
					x += 'Y';
					Y--;
				}
				else if (R > Y)
				{
					x += 'R';
					R--;
				}
				else if (tie == 'Y')
				{
					x += 'Y';
					Y--;
				}
				else
				{
					x += 'R';
					R--;
				}
			}
			k++;
		}
		for (int j = 0; j < V; j++)
		{
			if (x.length() == 0)
			{
				x = "VY";
				continue;
			}
			for (int i = 0; i < x.length(); i++)
			{
				if (x[i] == 'Y')
				{
					x.insert(i + 1, "VY");
					break;
				}
			}
		}
		for (int j = 0; j < O; j++)
		{
			if (x.length() == 0)
			{
				x = "OB";
				continue;
			}
			for (int i = 0; i < x.length(); i++)
			{
				if (x[i] == 'B')
				{
					x.insert(i + 1, "OB");
					break;
				}
			}
		}
		for (int j = 0; j < G; j++)
		{
			if (x.length() == 0)
			{
				x = "GR";
				continue;
			}
			for (int i = 0; i < x.length(); i++)
			{
				if (x[i] == 'R')
				{
					x.insert(i + 1, "GR");
					break;
				}				
			}
		}
		cout << "Case #" << tc << ": ";
		if (Y != 0 || R != 0 || B != 0|| (x[0] == 'R'&&x[(x.length() - 1)] == 'R') || (x[0] == 'Y'&&x[(x.length() - 1)] == 'Y')|| (x[0] == 'B'&&x[(x.length() - 1)] == 'B')||
			x.length()!=N||(x[0]=='V'&&x[(x.length() - 1)]!='Y')|| (x[0] == 'O'&&x[(x.length() - 1)] != 'B')|| (x[0] == 'G'&&x[(x.length() - 1)] != 'R')) cout << "Impossible" << endl;
		else cout << x << endl;	
	}

}