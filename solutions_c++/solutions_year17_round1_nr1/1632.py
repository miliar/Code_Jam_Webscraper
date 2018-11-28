#include <iostream>
#include <algorithm>

using namespace std;

int r,c;
string g[26],tmp[26];

void solve(int t)
{
	cin >> r >> c;
	for (int i=0; i<r; i++)
		cin >> g[i];

	copy(g,g+r,tmp);

	for (int i=0; i<r; i++)
		for (int j=0; j<c; j++)
			if (g[i][j]!='?')
			{
//				cout << i << " " << j << endl;
				for (int k=j-1; k>=0; k--)
					if (g[i][k]=='?') g[i][k]=g[i][j];
					else break;
				for (int k=j+1; k<c; k++)
					if (g[i][k]=='?') g[i][k]=g[i][j];
					else break;
			}
	if (g[0][0]=='?')
		for (int i=r-2; i>=0; i--)
			if (g[i][0]=='?')
				g[i]=g[i+1];
	for (int i=1; i<r; i++)
		if (g[i][0]=='?')
			g[i]=g[i-1];


	cout << "Case #" << t << ": " << endl;
	for (int i=0; i<r; i++)
		cout << g[i] << endl;
}

int main()
{
	int t;
	cin >> t;

	for (int i=1; i<=t; i++)
		solve(i);

//	solve(1);
}
