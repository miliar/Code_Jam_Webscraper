#include <iostream>
using namespace std;
int main()
{
	int T, x, R, C, r, c, i, j;
	char cake[25][25];
	cin >> T;
	for(x=1; x<=T; x++)
	{
		cin >> R >> C;
		for(r=0; r<R; r++)
			cin >> cake[r];
		for(c=0; c<C; c++)
		{
			if(cake[0][c]!='?')
				continue;
			for(r=0; r<R && cake[r][c]=='?'; r++);
			if(r==R)
				cake[0][c]='-';
			else
				cake[0][c]=cake[r][c];
		}
		for(r=1; r<R; r++)
		{
			for(c=0; c<C; c++)
			{
				if(cake[0][c]=='-')
					continue;
				if(cake[r][c]=='?')
					cake[r][c]=cake[r-1][c];
			}
		}
		if(cake[0][0]=='-')
		{
			for(c=1; c<C && cake[0][c]=='-'; c++);
			for(r=0; r<R; r++)
				cake[r][0]=cake[r][c];
		}
		for(c=1; c<C; c++)
		{
			if(cake[0][c]!='-')
				continue;
			for(r=0; r<R; r++)
				cake[r][c]=cake[r][c-1];
		}
		cout << "Case #" << x << ":" << endl;
		for(r=0; r<R; r++)
		{
			for(c=0; c<C; c++)
				cout << cake[r][c];
			cout << endl;
		}
	}
	return 0;
}