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

#ifndef ASSERT
#	define ASSERT(a,...)
#endif

int main()
{
	int t;
	
	cin >> t;
	for(int tt=1; tt<=t; ++tt)
	{
		int h[999] = {0}, v[999] = {0}, d1[999]={0}, d2[999]={0};
		char grid[128][128] = {0};
		
		int n, m;
		cin >> n >> m;
		int ans = 0;
		int no = 0;
		int yo = 0, xo = -1;
		for(int i=0; i<m; ++i)
		{
			char c;
			int x, y;
			cin >> c >> y >> x;
			--x, --y;
			if(c == 'o' || c == '+')
				d1[x+y]++, d2[n+x-y]++;
			if(c == 'o' || c == 'x')
				h[x]++, v[y]++;
			
			grid[y][x] = c;
			
			if(c == 'o')
				ans += 2, no += 1, xo = x;
			else
				ans += 1;
		}
		
		vector<int> rx, ry;
		vector<char> rc;
		
		for(int x=0; x<n; ++x) if(grid[yo][x] == 0)
		{
			rx.push_back(x);
			ry.push_back(yo);
			rc.push_back('+');
			ans += 1;
		}
		
		for(int x=0; x<n; ++x) if(grid[yo][x] == 'x')
		{
			h[x]--, v[yo]--;
			rx.push_back(x);
			ry.push_back(yo);
			rc.push_back('o');
			xo = x;
			++ans;
			++no;
		}
		
		if(!no)
		{
			if(grid[0][0] == '+') {
				d1[0+yo]--, d2[n+0-yo]--;
			}
			for(int i=0; i<rx.size(); ++i) if(rx[i] == 0)
			{
				rx.erase(rx.begin()+i);
				ry.erase(ry.begin()+i);
				rc.erase(rc.begin()+i);
				break;
			}
			
			rx.push_back(0);
			ry.push_back(yo);
			rc.push_back('o');
			xo = 0;
			++no;
			ans += 1;
		}
		
		ASSERT(no == 1);
		for(int x=0; x<n; ++x) if(x != xo)
		{
			if(x < xo) {
				rx.push_back(x);
				ry.push_back(abs(x-xo));
				rc.push_back('x');
				ans += 1;
			}
			else { //if(0 == x || n-1 == x || n-abs(x-xo) != n-1) {
				rx.push_back(x);
				ry.push_back(x);
				rc.push_back('x');
				ans += 1;
			}
		}
		
		yo = n-1;
		for(int x=1; x+1<n; ++x)
		{
			rx.push_back(x);
			ry.push_back(yo);
			rc.push_back('+');
			++ans;
		}
		
		cout << "Case #" << tt << ": " << ans << " " << rc.size() << "\n";
		for(int i=0; i<rx.size(); ++i)
		{
			cout << rc[i] << " " << ry[i]+1 << " " << rx[i]+1 << "\n";
			int x = rx[i];
			int y = ry[i];
			
			char c = rc[i];
			grid[y][x] = c;
			
			if(c == 'o' || c == '+')
				d1[x+y]++, d2[n+x-y]++;
			if(c == 'o' || c == 'x')
				h[x]++, v[y]++;
		}
		for(int y=0; y<n; ++y)
			for(int x=0; x<n; ++x)
			{
				if(grid[y][x] == 'o' || grid[y][x] == '+')
				{
					ASSERT(d1[x+y]==1, "%d,%d", x, y);
					ASSERT(d2[n+x-y]==1, "%d,%d", x, y);
				}
				if(grid[y][x] == 'o' || grid[y][x] == 'x')
				{
					ASSERT(h[x]==1, "%d,%d", x, y);
					ASSERT(v[y]==1, "%d,%d", x, y);
				}
			}
		
		cout.flush();
		ASSERT((n != 1 || ans == 2) && (n == 1 || ans == 3*n-2));
	}

	return 0;
}
