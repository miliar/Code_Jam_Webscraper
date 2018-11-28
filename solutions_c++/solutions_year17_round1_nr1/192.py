#include <cmath>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <vector>
#include <string>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

int main()
{
	int t;
	
	cin >> t;
	for(int tt=1; tt<=t; ++tt)
	{
		int X,Y;
		cin >> Y >> X;
		vector<string> s(Y);
		vector<int> nn(Y,0);
		for(int y=0; y<Y; ++y)
		{
			cin >> s[y];
			for(int x=0; x<X; ++x)
				if(s[y][x]!='?')
					++nn[y];
		}
	
		int y1 = 0;
		for(int yo=0; yo<Y; ++yo)
		{
			int inrow = 0;
			int y2 = Y-1;
			for(int y=yo+1; y<Y; ++y)
				if(nn[y])
					y2 = yo;
			int x1 = 0;
			for(int xo=0; xo<X; ++xo) if(s[yo][xo] != '?')
			{
				for(int y=y1; y<=y2; ++y)
				{
					int x2 = (inrow==nn[yo]-1?X-1:xo);
					for(int x=x1; x<=x2; ++x)
						s[y][x] = s[yo][xo];
				}
				x1 = xo+1;
				++inrow;
			}
			if(nn[yo])
				y1 = yo+1;
		}
		
		int ans = 0;
		
		cout << "Case #" << tt << ":\n";
		for(int y=0; y<Y; ++y)
			cout << s[y] << "\n";
		cout.flush();
	}

	return 0;
}
