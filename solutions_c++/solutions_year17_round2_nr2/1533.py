#include <bits/stdc++.h>
using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	
	for(int ii = 1; ii <= T; ii++)
	{
		cout << "Case #" << ii << ": ";
		
		int n;
		cin >> n;
		
		int r, o, y, g, b, v;
		cin >> r >> o >> y >> g >> b >> v;
		
		int mx = max(r, max(y, b));
		
		if(2 *mx > n)
		{
			cout << "IMPOSSIBLE" << endl;
			continue;
		}
		
		map <char, int> M;
		char ans[n];
		
		if(mx == r)
		{
			ans[0] = 'R';
			r--;
		}
		
		else if(mx == y)
		{
			ans[0] = 'Y';
			y--;
		}
		
		else
		{
			ans[0] = 'B';
			b--;
		}
		
		M['R'] = r;
		M['Y'] = y;
		M['B'] = b;
		
		char curr[3] = {'R', 'Y', 'B'};
		bool flag = 1;
		for(int i = 1; i < n; i++)
		{
			char put = '-';
			int cnt = 0;
			
			for(int j = 0; j < 3; j++)
			{
				if(curr[j] != ans[i -1])
				{
					if(M[curr[j]] > cnt)
					{
						cnt = M[curr[j]];
						put = curr[j];
					}
				}
			}	
			
			if(put == '-')
			{
				flag = 0;
				break;
			}
			
			ans[i] = put;
			M[put]--;
		}
		
		if(flag)
		{
			if(ans[0] == ans[n -1])
				flag = 0;
			
			else
			{
				for(int i = 0; i < n; i++)
					cout << ans[i];
			
				cout << endl;
				continue;
			}
		}
		
		if(flag == 0)
		{
			M['R'] = r;
			M['Y'] = y;
			M['B'] = b;
			flag = 1;
			
			for(int i = 1; i < n; i++)
			{
				char put = '-';
				int cnt = 0;
		
				for(int j = 0; j < 3; j++)
				{
					if(curr[j] != ans[i -1])
					{
						if(M[curr[j]] > 0 && M[curr[j]] >= cnt)
						{
							cnt = M[curr[j]];
							put = curr[j];
						}
					}
				}	
		
				if(put == '-')
				{
					flag = 0;
					cout << "IMPOSSIBLE" << endl;
					break;
				}
		
				ans[i] = put;
				M[put]--;
			}
		
			if(flag)
			{
				if(ans[0] == ans[n -1])
					cout << "IMPOSSIBLE" << endl;
			
				else
				{
					for(int i = 0; i < n; i++)
						cout << ans[i];
					cout << endl;
				}
			}
		}
	}
	return 0;
}
